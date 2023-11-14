from function import from_number
from function import to_number
from function import executed


def test_from_number():
    assert from_number("1111111111111111") == "1111 11** **** 1111 ->"
    assert from_number('') == ""
    assert from_number('qqqqqqqqqqqqqqqq') == "qqqq qq** **** qqqq ->"
    assert from_number('1111111111111111111111111') == "Счет **1111 ->"
    assert from_number('qqqqqqqqqqqqqqqqqqqqqqqqq') == "Счет **qqqq ->"


def test_to_numbers():
    assert to_number('111111111111') == '**1111'
    assert to_number('') == '**'
    assert to_number('gmhkbjnhyhtyj') == '**htyj'


def test_executed():
    assert executed([{"state": "EXECUTED"}]) == [{"state": "EXECUTED"}]
    assert executed([{"state": "CANCELED"}]) == []
