from typing import Any, Callable, Optional, Tuple

import pytest

from liketext import text


@pytest.mark.parametrize(
    "testcause,args,sep,result",
    [
        [text.text, ("test", "test"), " ", "test test"],
        [text.text, ("test", "test"), "\n", "test\ntest"],
        [text.text, ("test", "test"), None, "test test"],
        [text.bold, ("test", "test"), " ", "*test test*"],
        [text.hbold, ("test", "test"), " ", "<b>test test</b>"],
        [text.italic, ("test", "test"), " ", "_test test_"],
        [text.hitalic, ("test", "test"), " ", "<i>test test</i>"],
        [text.code, ("test", "test"), " ", "`test test`"],
        [text.hcode, ("test", "test"), " ", "<code>test test</code>"],
        [text.pre, ("test", "test"), " ", "```\ntest test\n```"],
        [text.hpre, ("test", "test"), " ", "<pre>test test</pre>"],
        [text.underline, ("test", "test"), " ", "__test test__"],
        [text.hunderline, ("test", "test"), " ", "<u>test test</u>"],
        [text.strikethrough, ("test", "test"), " ", "~test test~"],
        [text.hstrikethrough, ("test", "test"), " ", "<s>test test</s>"],
        [text.link, ("test", "https://some.org"), None, "[test](https://some.org)"],
        [
            text.hlink,
            ("test", "https://some.org"),
            None,
            '<a href="https://some.org">test</a>',
        ],
        [
            text.hide_link,
            ("https://some.org",),
            None,
            '<a href="https://some.org">&#8203;</a>',
        ],
    ],
)
def test_formatter(
    testcause: Callable[..., Any], args: Tuple[str], sep: Optional[str], result: str
) -> None:
    assert testcause(*args, **({"sep": sep} if sep is not None else {})) == result
