from typing import Tuple

import pytest

from liketext import md_decoration


@pytest.mark.parametrize(
    "testcause,values,result",
    [
        ("link", ("hello", "https://some.org"), "[hello](https://some.org)"),
        ("bold", ("hello",), "*hello*"),
        ("italic", ("hello",), "_hello_"),
        ("code", ("hello",), "`hello`"),
        ("pre", ("hello",), "```\nhello\n```"),
        ("pre_language", ("hello", "world"), "```world\nhello\n```"),
        ("underline", ("hello",), "__hello__"),
        ("strikethrough", ("hello",), "~hello~"),
        ("spoiler", ("hello",), "|hello|"),
        ("custom_emoji", ("hello", "world"), "[hello](tg://emoji?id=world)"),
        ("quote", ("[hello]",), "\\[hello\\]"),
    ],
)
def test_md_decoration(testcause: str, values: Tuple[str], result: str) -> None:
    assert getattr(md_decoration, testcause)(*values) == result
