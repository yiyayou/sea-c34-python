#!/usr/bin/env python


def print_series_header(series_num):
    """Print a header for each dict lab series output, to aid in reading."""

    print(u"-------------------")
    print(u"Dict Lab - Series {}".format(series_num))
    print(u"-------------------")


def print_series_step(series_num, step_num, output):
    """Print the current state of the dict list series as a formatted string
    with the series number and step number.
    """

    print(u"{}.{} - {}".format(series_num, step_num, output))


def series1():
    print_series_header(1)
    the_dict = {}
    print_series_step(1, 1, the_dict)
    return the_dict


def series2():
    print_series_header(2)
    pass


def series3(s1_dict):
    print_series_header(3)
    pass


def series4():
    print_series_header(4)
    pass


def series5():
    print_series_header(5)
    pass


if __name__ == "__main__":
    s1_dict = series1()
    series2()
    series3(s1_dict)
    series4()
    series5()