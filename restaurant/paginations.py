from rest_framework import pagination as pg
from rest_framework.response import Response

class StandardPagination(pg.PageNumberPagination):
    page_size = 20
    page_query_param = "page"
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response(data)