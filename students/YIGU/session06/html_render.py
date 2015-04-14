#!/usr/bin/env python

"""
Python class example.

"""


class Element(object):
    """An HTML element."""
    tag = u"html"
    indent = u"    "

    def __init__(self, content=None):
        self.content = self.indent + str(self.content) if content else ""

    def append(self, string):
        """Append string to content."""
    pass

    def render(self, file_out, ind=""):
        """Render the tag and strings in content."""
    pass


class Html(Element):
    """HTML tag."""

    tag = u"html"


class Body(Element):
    """Body tag."""

    tag = u"body"
