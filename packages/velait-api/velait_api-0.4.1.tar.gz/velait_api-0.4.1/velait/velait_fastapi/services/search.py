from typing import Optional, Type, Any

from fastapi import Query
from sqlalchemy import column
from assimilator.alchemy.database import AlchemyRepository

from velait.common.services.exceptions import PaginationLimitsError
from velait.common.services.pagination import get_offset_limits, get_page_limits
from velait.common.services.search import Search, SearchError, SearchOperator


class AlchemyRepositorySearch(Search):
    def __init__(
        self,
        model: Type['BaseModel'],
        repository: AlchemyRepository,
        search_: Optional[str] = None,
        query: str = Query(default=None),
        ordering: Optional[str] = None,
        page: Optional[Any] = None,
        default_pagination_size: int = 10,
    ):
        self.repository = repository
        self._page = self._parse_json(page, key_name='page')
        self.default_pagination_size = default_pagination_size
        super(AlchemyRepositorySearch, self).__init__(
            search=search_,
            query=query,
            ordering=ordering,
            model=model,
        )

    def validate(self):
        super(AlchemyRepositorySearch, self).validate()

        if not isinstance(self._page, dict):
            raise SearchError(
                name="page",
                description="Invalid structure of 'page'",
            )

        if self._page.get('offset', 0) <= 0:
            self._page['offset'] = 0

        if self._page.get('size', 0) <= 0:
            self._page['size'] = self.default_pagination_size

    def _parse_ordering(self):
        alchemy_ordering = list(self._ordering)

        for i in range(len(alchemy_ordering)):
            ordering_column = alchemy_ordering[i]
            if ordering_column.startswith('-'):
                ordering_column = f"{ordering_column[1:]} desc"

            alchemy_ordering[i] = column(ordering_column, is_literal=True)

        return alchemy_ordering

    def search(self):
        try:
            filter_spec = self.repository.specifications.filter(*self.parse_query_filters())

            offset, limit = get_page_limits(page=self._page['offset'], page_size=self._page['size'])
            pagination_spec = self.repository.specifications.paginate(offset=offset, limit=limit)

            if self._ordering:
                return self.repository.filter(
                    filter_spec,
                    pagination_spec,
                    self.repository.specifications.order(*self._parse_ordering()),
                    lazy=True,
                )

            return self.repository.filter(filter_spec, pagination_spec, lazy=True)

        except PaginationLimitsError:
            raise SearchError(
                name='page',
                description="'page' parameter contains invalid values",
            )
        except Exception:
            raise SearchError(
                name="search",
                description="Search could not be conducted",
            )

    def _parse_operator(self, field_name: str, operator: str, field_value: str):
        """
        Creates an expression object if all input operators are valid.
        If they are not, raises op an exception
        """

        if operator == "equals":
            return getattr(self.model, field_name) == field_value
        elif operator == "lessOrEqual":
            return getattr(self.model, field_name) <= field_value
        elif operator == "greaterOrEqual":
            return getattr(self.model, field_name) >= field_value
        elif operator == "greater":
            return getattr(self.model, field_name) > field_value
        elif operator == "less":
            return getattr(self.model, field_name) < field_value
        elif operator == "contains":
            return getattr(self.model, field_name).in_(field_value)
        else:
            raise SearchError(
                name="query",
                description=f"Operation '{operator}' is unknown",
            )


__all__ = [
    'SearchError',
    'SearchOperator',
    'AlchemyRepositorySearch',
]
