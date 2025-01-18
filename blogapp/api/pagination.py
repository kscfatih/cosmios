from rest_framework.pagination import *

class BlogPagination(PageNumberPagination):
    page_size=3
    page_query_param = 'page_blog'

    def get_paginated_response(self, data):
        return Response({
            'toplam_blog_sayisi': self.page.paginator.count,
            'sonraki': self.get_next_link(),
            'önceki': self.get_previous_link(),
            'yanıtlar': data,
        })

class AuthorPagination(LimitOffsetPagination):
    default_limit = 3