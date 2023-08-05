from djangorestframework_camel_case.render import CamelCaseJSONRenderer


class VelaitAPIRenderer(CamelCaseJSONRenderer):
    def render(self, data, *args, **kwargs):
        if not (isinstance(data, dict) and data.get('pagination') is not None) and data.get('errors') is None:
            data = {
                "results": data,
                "pagination": {
                    'totalRecords': 1,
                    'totalPages': 1,
                    'first': None,
                    'last': None,
                    'next': None,
                    'previous': None,
                },
                "errors": [],
            }

        return super(VelaitAPIRenderer, self).render(data, *args, **kwargs)


__all__ = ['VelaitAPIRenderer']
