from typing import Any

from .text_decorations import html, md


def _join(*content: Any, sep: str = " ") -> str:
    return sep.join(map(str, content))


def text(*content: Any, sep: str = " ") -> str:
    """
    Join all elements with a separator.
    """

    return _join(*content, sep=sep)


def bold(*content: Any, sep: str = " ") -> str:
    """
    Make bold text (Markdown).
    """

    return md.bold(value=md.quote(_join(*content, sep=sep)))


def hbold(*content: Any, sep: str = " ") -> str:
    """
    Make bold text (HTML).
    """

    return html.bold(value=html.quote(_join(*content, sep=sep)))


def italic(*content: Any, sep: str = " ") -> str:
    """
    Make italic text (Markdown).
    """

    return md.italic(value=html.quote(_join(*content, sep=sep)))


def hitalic(*content: Any, sep: str = " ") -> str:
    """
    Make italic text (HTML).
    """

    return html.italic(value=html.quote(_join(*content, sep=sep)))


def code(*content: Any, sep: str = " ") -> str:
    """
    Make mono-width text (Markdown).
    """

    return md.code(value=md.quote(_join(*content, sep=sep)))


def hcode(*content: Any, sep: str = " ") -> str:
    """
    Make mono-width text (HTML).
    """

    return html.code(value=html.quote(_join(*content, sep=sep)))


def pre(*content: Any, sep: str = "\n") -> str:
    """
    Make mono-width text block (Markdown).
    """

    return md.pre(value=md.quote(_join(*content, sep=sep)))


def hpre(*content: Any, sep: str = "\n") -> str:
    """
    Make mono-width text block (HTML).
    """

    return html.pre(value=html.quote(_join(*content, sep=sep)))


def underline(*content: Any, sep: str = " ") -> str:
    """
    Make underlined text (Markdown).
    """

    return md.underline(value=md.quote(_join(*content, sep=sep)))


def hunderline(*content: Any, sep: str = " ") -> str:
    """
    Make underlined text (HTML).
    """

    return html.underline(value=html.quote(_join(*content, sep=sep)))


def strikethrough(*content: Any, sep: str = " ") -> str:
    """
    Make strikethrough text (Markdown).
    """

    return md.strikethrough(value=md.quote(_join(*content, sep=sep)))


def hstrikethrough(*content: Any, sep: str = " ") -> str:
    """
    Make strikethrough text (HTML).
    """

    return html.strikethrough(value=html.quote(_join(*content, sep=sep)))


def link(title: str, url: str) -> str:
    """
    Format URL (Markdown).
    """

    return md.link(value=md.quote(title), link=url)


def hlink(title: str, url: str) -> str:
    """
    Format URL (HTML).
    """

    return html.link(value=html.quote(title), link=url)


def hide_link(url: str) -> str:
    """
    Hide URL (HTML only).
    Can be used for adding an image to a text message.
    """

    return f'<a href="{url}">&#8203;</a>'
