from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class SettingsPageNumberPagination(PageNumberPagination):
    """
    Class for basic page pagination settings

    Attributes:
        page_query_param (str): The name of the page number parameter in the URL.
        page_size_query_param (str): The name of the page size parameter in the URL.
        max_page_size (int): The maximum number of items per page.
        page_size (int): The default number of items per page.
    """
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_size = 10

    def get_paginated_response(self, data):
        """
        Customized pagination response

        Args:
            data (list): The paginated data to be included in the response.

        Returns:
            Response: A customized pagination response containing the following keys:
                - 'results': The paginated data provided as an argument.
                - 'total_pages': The total number of pages in the paginated data.
                - 'count': The total number of items across all pages.
                - 'links': A dictionary containing 'next' and 'previous' links for navigation.
        """
        return Response({
            'results': data,
            'total_pages': self.page.paginator.num_pages,
            'count': self.page.paginator.count,
            'page_size': self.page_size,
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
            }
        })
