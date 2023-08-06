from typing import Union

from sqlalchemy.orm import Query
from sqlalchemy_pagination import paginate


class Paginator:
    """Tools to query a database using sqlalchemy with pagination."""
    DATA = 'data'
    PAGINATION = 'pagination'
    REQUESTED_PAGE = 'requested_page'
    MAX_ITEMS_PER_PAGE = 'max_items_per_page'
    TOTAL_PAGE_COUNT = 'total_page_count'
    TOTAL_ITEM_COUNT = 'total_item_count'

    DEFAULT_PAGINATION = {
        REQUESTED_PAGE: 1,
        MAX_ITEMS_PER_PAGE: 100
    }

    @staticmethod
    def yield_pages(unpagined_partial_query: Query, chunk_size: int):
        """Execute a given query until the paginated result is empty."""
        current_page = 1
        while True:
            pagination = Paginator._get_pagination_param(current_page, chunk_size)
            query_result = Paginator.process(unpagined_partial_query, pagination)
            yield query_result[Paginator.DATA]
            if current_page >= query_result[Paginator.PAGINATION][Paginator.TOTAL_PAGE_COUNT]:
                break
            current_page += 1

    @staticmethod
    def process(query, pagination: Union[dict, None] = None) -> dict:
        """Perform a database query in pagination mode.

        :param query: query to be executed by sqlalchemy
        :param pagination: Pagination settings in the form ``{"requested_page": 1, "max_items_per_page": 10}``
        :return: Required paginated results with pagination details::

            {
                "data": [...],
                "pagination_out": {
                    "total_number_of_pages": 4,
                    "total_number_of_items": 48
                }
            }
        """
        if pagination is None:
            pagination = Paginator.DEFAULT_PAGINATION

        page = paginate(
            query,
            pagination[Paginator.REQUESTED_PAGE],
            pagination[Paginator.MAX_ITEMS_PER_PAGE]
        )

        return {
            Paginator.DATA: page.items,
            Paginator.PAGINATION: {
                Paginator.TOTAL_PAGE_COUNT: page.pages,
                Paginator.TOTAL_ITEM_COUNT: page.total
            }
        }

    @staticmethod
    def _get_pagination_param(requested_page: int, max_items_per_page: int):
        """Build pagination settings input."""
        return {
            Paginator.REQUESTED_PAGE: requested_page,
            Paginator.MAX_ITEMS_PER_PAGE: max_items_per_page
        }
