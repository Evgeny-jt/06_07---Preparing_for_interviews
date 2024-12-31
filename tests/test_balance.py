import pytest

import balance


@pytest.mark.parametrize(
    'str_bracket, expected',
    (
            ["(((([{}]))))", "Сбалансированно"],
            ["[([])((([[[]]])))]{()}", "Сбалансированно"],
            ["{{[()]}}", "Сбалансированно"],
            ["}{}", "Несбалансированно"],
            ["{{[(])]}}", "Несбалансированно"],
            ["[[{())}]", "Несбалансированно"],

            ["{(])}", "Несбалансированно"],
            ["{(([(]))}{[]}", "Несбалансированно"],
            ["((({}))", "Несбалансированно"],
    )
)
def test_task_secretary(str_bracket, expected):
    result = balance.balance(str_bracket)
    assert result == expected
