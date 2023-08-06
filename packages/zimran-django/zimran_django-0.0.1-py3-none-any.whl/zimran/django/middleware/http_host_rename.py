from typing import Callable

from django.http import HttpRequest


class HttpHostRenameMiddleware:
    def __init__(self, get_response: Callable) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        request.META['HTTP_HOST'] = self._rename_http_host(request.META['HTTP_HOST'])
        return self.get_response(request)

    @staticmethod
    def _rename_http_host(http_host: str) -> str:
        return http_host.replace('_', '-')
