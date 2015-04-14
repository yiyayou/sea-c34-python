#!/usr/bin/env python

"""
Python class example.

"""


class Element(object):
    """Components of a webpage"""
    tag = u""
    indent = u"    "
    content = ""

    def __init__(self, content=None):
        self.content = self.indent + str(self.content) if content else ""

    def append(self, string):
        """Append string to content."""
        self.content += (
            u"{indent}{str}\n".format(indent=self.indent, str=str(string))
        )

    def render(self, file_out, ind=""):
        """Render the tag and strings in content."""
        output = (
            u"{indent}<{tag}>\n"
            "{indent}{content}"
            "{indent}</{tag}>"
            .format(indent=ind, tag=self.tag, content=self.content)
        )
        file_out.write(output)


class Html(Element):
    """HTML tag."""

    tag = u"html"

    def render(self, file_out, ind=""):
        file_out.write("<!DOCTYPE html>\n")
        Element.render(self, file_out, ind)


class Body(Element):
    tag = u"body"


class P(Element):
    tag = u"p"

"""
class Head(Element):
    tag = u"head"

class Ul(Element):
    tag = u"ul"


class Li(Element):
    tag = u"li"
"""
