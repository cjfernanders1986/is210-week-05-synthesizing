#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01"""

import datetime

CURDATE = None


def get_current_date():
    """Docstring to get_current_date function.
    Args:
        This function will give me the current date

    Returns:
            Returns the current date.
    """
    return datetime.date.today()

if __name__ == '__main__':
    CURDATE = get_current_date()
    print CURDATE
