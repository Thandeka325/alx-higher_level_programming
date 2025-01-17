#!/usr/bin/python3
"""This script finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds a peak in list_of_integers."""

    if list_of_integers is None or list_of_integers == []:
        return None

    lo = 0
    hi = len(list_of_integers) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if ((mid == 0 or
             list_of_integers[mid] >= list_of_integers[mid - 1]) and
            (mid == len(list_of_integers) - 1 or
             list_of_integers[mid] >= list_of_integers[mid + 1])):
            return list_of_integers[mid]

        elif (mid < len(list_of_integers) - 1 and
              list_of_integers[mid] < list_of_integers[mid + 1]):
            lo = mid + 1

        else:
            hi = mid - 1

    return None
