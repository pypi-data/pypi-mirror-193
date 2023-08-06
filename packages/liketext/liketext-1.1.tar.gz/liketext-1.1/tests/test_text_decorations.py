from typing import Text, Tuple

import pytest

from liketext import html, md


@pytest.mark.parametrize(
    "decoration,testfunction,args,excepted",
    [
        (html, "link", ("hello", "https://some.org"), '<a href="https://some.org">hello</a>'),
        (html, "bold", ("hello",), "<b>hello</b>"),
        (html, "italic", ("hello",), "<i>hello</i>"),
        (html, "code", ("hello",), "<code>hello</code>"),
        (html, "pre", ("hello",), "<pre>hello</pre>"),
        (
            html,
            "pre_language",
            ("hello", "world"),
            '<pre><code class="world">hello</code></pre>',
        ),
        (html, "underline", ("hello",), "<u>hello</u>"),
        (html, "strikethrough", ("hello",), "<s>hello</s>"),
        (html, "spoiler", ("hello",), "<tg-spoiler>hello</tg-spoiler>"),
        (
            html,
            "custom_emoji",
            ("hello", "world"),
            '<tg-emoji emoji-id="world">hello</tg-emoji>',
        ),
        (html, "quote", ("<hello>",), "&lt;hello&gt;"),
        (md, "link", ("hello", "https://some.org"), "[hello](https://some.org)"),
        (md, "bold", ("hello",), "*hello*"),
        (md, "italic", ("hello",), "_hello_"),
        (md, "code", ("hello",), "`hello`"),
        (md, "pre", ("hello",), "```\nhello\n```"),
        (md, "pre_language", ("hello", "world"), "```world\nhello\n```"),
        (md, "underline", ("hello",), "__hello__"),
        (md, "strikethrough", ("hello",), "~hello~"),
        (md, "spoiler", ("hello",), "|hello|"),
        (md, "custom_emoji", ("hello", "world"), "[hello](tg://emoji?id=world)"),
        (md, "quote", ("[hello]",), "\\[hello\\]"),
    ],
)
def test_text_decorations(
    decoration: Text, testfunction: str, args: Tuple[str], excepted: str
) -> None:
    assert getattr(decoration, testfunction)(*args) == excepted
