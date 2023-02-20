#!/usr/bin/env python3
""" Simpler helper function """


def index_range(page, page_size):
    """ Returns the range of index for a given page."""
    start_point = (page - 1) * page_size
    end_point = page * page_size
    return start_point, end_point
