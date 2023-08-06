import json
from typing import Optional, Tuple
from collections import OrderedDict

import coreschema
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.inspectors import PaginatorInspector
from rest_framework.response import Response
from django.template import loader
from django.db.models import QuerySet
from rest_framework.utils.urls import replace_query_param, remove_query_param
from rest_framework.pagination import BasePagination

from velait.velait_django.main.api.responses import APIResponse


class VelaitPagination(BasePagination):
    size: Optional[int] = None
    offset: Optional[int] = None
    __queryset_count: Optional[int] = None
    page_query_param: str = "page"
    request = None

    def _parse_params(self, request) -> Tuple[int, int]:
        try:
            parsed_page = json.loads(request.query_params[self.page_query_param])
            if not isinstance(parsed_page, dict):
                raise TypeError()
            elif parsed_page.get('size') <= 0 or parsed_page.get('offset', 0) < 0:
                raise ValueError()

            return parsed_page['size'], parsed_page['offset']

        except (json.JSONDecodeError, TypeError, ValueError, KeyError) as exc:
            return settings.REST_FRAMEWORK['PAGE_SIZE'], 0

    def paginate_queryset(self, queryset: QuerySet, request, view=None):
        self.size, self.offset = self._parse_params(request)
        self.__queryset_count = queryset.count()
        self.request = request

        limit = self.offset * self.size
        if self.offset == 0:
            limit = self.size

        return queryset[self.offset:limit + self.offset]

    def _get_pagination_configuration(self):
        current_page = self.get_page_number(size=self.size, offset=self.offset)
        max_page = (self.__queryset_count // self.size) - 1
        next_page = current_page + 1

        if next_page >= max_page:
            next_page = max_page

        previous_page = current_page - 1
        if previous_page <= 0:
            previous_page = remove_query_param(
                url=self.request.build_absolute_uri(),
                key=self.page_query_param,
            )
        else:
            previous_page = replace_query_param(
                url=self.request.build_absolute_uri(),
                key=self.page_query_param,
                val=json.dumps({"size": self.size, "offset": previous_page})
            )

        return {
            'totalRecords': self.__queryset_count,
            'totalPages': max_page + 1,
            'first': self.request.build_absolute_uri(),
            'last': replace_query_param(
                url=self.request.build_absolute_uri(),
                key=self.page_query_param,
                val=json.dumps({"size": self.size, "offset": max_page}),
            ),
            'next': replace_query_param(
                url=self.request.build_absolute_uri(),
                key=self.page_query_param,
                val=json.dumps({"size": self.size, "offset": next_page}),
            ),
            'previous': previous_page,
        }

    def get_paginated_response(self, data) -> APIResponse:
        return APIResponse({
            "pagination": self._get_pagination_configuration(),
            "results": data,
            "errors": [],
        })

    def to_html(self):
        template = loader.get_template(self.template)
        return template.render(self._get_pagination_configuration())

    def get_schema_fields(self, view):
        assert coreapi is not None, 'coreapi must be installed to use `get_schema_fields()`'
        assert coreschema is not None, 'coreschema must be installed to use `get_schema_fields()`'
        return [
            coreapi.Field(
                name=self.page_query_param,
                required=False,
                location=self.page_query_param,
                schema=coreschema.Object(
                    properties=[
                        coreschema.Integer(minimum=1),
                        coreschema.Integer(minimum=0),
                    ],
                    description='Page for pagination'
                ),
            )
        ]

    def get_schema_operation_parameters(self, view):
        return [
            {
                'name': self.page_query_param,
                'required': False,
                'in': 'query',
                'description': 'Page',
                'schema': {
                    'type': 'integer',
                    'type': 'integer',
                },
            },
        ]

    def get_page_number(self, size: int, offset: int) -> int:
        page = offset // size
        return page if page > 0 else 1


class VelaitPaginationInspector(PaginatorInspector):
    def get_paginated_response(self, paginator, response_schema):
        return openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "pagination": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'totalRecords': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'totalPages': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'first': openapi.Schema(type=openapi.TYPE_STRING,
                                                format=openapi.FORMAT_URI, x_nullable=True),
                        'last': openapi.Schema(type=openapi.TYPE_STRING,
                                               format=openapi.FORMAT_URI, x_nullable=True),
                        'next': openapi.Schema(type=openapi.TYPE_STRING,
                                               format=openapi.FORMAT_URI, x_nullable=True),
                        'previous': openapi.Schema(type=openapi.TYPE_STRING,
                                                   format=openapi.FORMAT_URI, x_nullable=True),
                    },
                ),
                'results': response_schema,
                'errors': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'name': openapi.Schema(type=openapi.TYPE_STRING),
                            'description': openapi.Schema(type=openapi.TYPE_STRING),
                        },
                    ),
                ),
            },
            required=['results'],
        )
