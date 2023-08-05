from typing import Tuple

import pytest

from liketext import html_decoration


@pytest.mark.parametrize(
    "testcause,values,result",
    [
        ("link", ("hello", "https://some.org"), '<a href="https://some.org">hello</a>'),
        ("bold", ("hello",), "<b>hello</b>"),
        ("italic", ("hello",), "<i>hello</i>"),
        ("code", ("hello",), "<code>hello</code>"),
        ("pre", ("hello",), "<pre>hello</pre>"),
        (
            "pre_language",
            ("hello", "world"),
            '<pre><code class="world">hello</code></pre>',
        ),
        ("underline", ("hello",), "<u>hello</u>"),
        ("strikethrough", ("hello",), "<s>hello</s>"),
        ("spoiler", ("hello",), "<tg-spoiler>hello</tg-spoiler>"),
        (
            "custom_emoji",
            ("hello", "world"),
            '<tg-emoji emoji-id="world">hello</tg-emoji>',
        ),
        ("quote", ("<hello>",), "&lt;hello&gt;"),
    ],
)
def test_html_decoration(testcause: str, values: Tuple[str], result: str) -> None:
    assert getattr(html_decoration, testcause)(*values) == result
