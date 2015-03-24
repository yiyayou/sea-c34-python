#!/usr/bin/env python


def series1():
    return [u"Apples", u"Pears", u"Oranges", u"Peaches"]


def series2(fruitlist):
    pass


def series3(fruitlist):
    pass


def series4(fruitlist):
    pass


if __name__ == "__main__":
    fruitlist = series1()
    series2(fruitlist[:])
    series3(fruitlist[:])
    series4(fruitlist[:])