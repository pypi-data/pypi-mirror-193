from typing import Any, Callable, Optional, Tuple

import pytest

from liketext import (
    bold,
    code,
    hbold,
    hcode,
    hide_link,
    hitalic,
    hlink,
    hpre,
    hstrikethrough,
    hunderline,
    italic,
    link,
    pre,
    strikethrough,
    text,
    underline,
)


@pytest.mark.parametrize(
    "testfunction,args,sep,excepted",
    [
        (text, ("test", "test"), " ", "test test"),
        (text, ("test", "test"), None, "test test"),
        (bold, ("test", "test"), " ", "*test test*"),
        (hbold, ("test", "test"), " ", "<b>test test</b>"),
        (italic, ("test", "test"), " ", "_test test_"),
        (hitalic, ("test", "test"), " ", "<i>test test</i>"),
        (code, ("test", "test"), " ", "`test test`"),
        (hcode, ("test", "test"), " ", "<code>test test</code>"),
        (pre, ("test", "test"), " ", "```\ntest test\n```"),
        (hpre, ("test", "test"), " ", "<pre>test test</pre>"),
        (underline, ("test", "test"), " ", "__test test__"),
        (hunderline, ("test", "test"), " ", "<u>test test</u>"),
        (strikethrough, ("test", "test"), " ", "~test test~"),
        (hstrikethrough, ("test", "test"), " ", "<s>test test</s>"),
        (link, ("test", "https://some.org"), None, "[test](https://some.org)"),
        (hlink, ("test", "https://some.org"), None, '<a href="https://some.org">test</a>'),
        (hide_link, ("https://some.org",), None, '<a href="https://some.org">&#8203;</a>'),
    ],
)
def test_formatter(
    testfunction: Callable[..., Any], args: Tuple[str], sep: Optional[str], excepted: str
) -> None:
    kwargs = {} if sep is None else {"sep": sep}
    assert testfunction(*args, **kwargs) == excepted
