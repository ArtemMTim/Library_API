from rest_framework.pagination import PageNumberPagination


class PageSize(PageNumberPagination):
    """Пагинатор на 10 объектов на страницу."""
    page_size = 10
    page_size_query = "page_size"
    max_page_size = 50
