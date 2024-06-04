from django.conf import settings
from rest_framework import pagination


class OnePaginator(pagination.PageNumberPagination):
    page_size = settings.REST_FRAMEWORK["PAGE_SIZE"]
