import abc
import html
import re
from typing import Dict

from .re import MD_QUOTE_PATTERN


class TextDecoration(abc.ABC):
    _decorations: Dict[str, str]

    def link(self, value: str, link: str) -> str:
        decoration = self._decorations["link"]
        return decoration.format(link=link, value=value)

    def bold(self, value: str) -> str:
        decoration = self._decorations["bold"]
        return decoration.format(value=value)

    def italic(self, value: str) -> str:
        decoration = self._decorations["italic"]
        return decoration.format(value=value)

    def code(self, value: str) -> str:
        decoration = self._decorations["code"]
        return decoration.format(value=value)

    def pre(self, value: str) -> str:
        decoration = self._decorations["pre"]
        return decoration.format(value=value)

    def pre_language(self, value: str, language: str) -> str:
        decoration = self._decorations["pre_language"]
        return decoration.format(language=language, value=value)

    def underline(self, value: str) -> str:
        decoration = self._decorations["underline"]
        return decoration.format(value=value)

    def strikethrough(self, value: str) -> str:
        decoration = self._decorations["strikethrough"]
        return decoration.format(value=value)

    def spoiler(self, value: str) -> str:
        decoration = self._decorations["spoiler"]
        return decoration.format(value=value)

    def custom_emoji(self, value: str, custom_emoji_id: str) -> str:
        decoration = self._decorations["emoji"]
        return decoration.format(custom_emoji_id=custom_emoji_id, value=value)

    @abc.abstractmethod
    def quote(self, value: str) -> str:
        ...


class HTMLDecoration(TextDecoration):
    _decorations: Dict[str, str] = {
        "link": '<a href="{link}">{value}</a>',
        "bold": "<b>{value}</b>",
        "italic": "<i>{value}</i>",
        "code": "<code>{value}</code>",
        "pre": "<pre>{value}</pre>",
        "pre_language": '<pre><code class="{language}">{value}</code></pre>',
        "underline": "<u>{value}</u>",
        "strikethrough": "<s>{value}</s>",
        "spoiler": "<tg-spoiler>{value}</tg-spoiler>",
        "emoji": '<tg-emoji emoji-id="{custom_emoji_id}">{value}</tg-emoji>',
    }

    def quote(self, value: str) -> str:
        return html.escape(value, quote=False)


class MDDecoration(TextDecoration):
    _decorations: Dict[str, str] = {
        "link": "[{value}]({link})",
        "bold": "*{value}*",
        "italic": "_{value}_",
        "code": "`{value}`",
        "pre": "```\n{value}\n```",
        "pre_language": "```{language}\n{value}\n```",
        "underline": "__{value}__",
        "strikethrough": "~{value}~",
        "spoiler": "|{value}|",
        "emoji": "[{value}](tg://emoji?id={custom_emoji_id})",
    }

    def quote(self, value: str) -> str:
        return re.sub(pattern=MD_QUOTE_PATTERN, repl=r"\\\1", string=value)


html_decoration = HTMLDecoration()
md_decoration = MDDecoration()
