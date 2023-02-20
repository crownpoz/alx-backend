#!/usr/bin/env python3
""" Simpler helper function """
import csv
import math
from typing import List


def index_range(page, page_size):
    """ Returns the range of index for a given page."""
    start_point = (page - 1) * page_size
    end_point = page * page_size
    return start_point, end_point


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a new Server instance.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves a page of data.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start_point, end_point = index_range(page, page_size)
        data = self.dataset()
        if start_point > len(data):
            return []
        return data[start_point:end_point]
