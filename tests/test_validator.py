import pytest
from pydator.rules import (
    required, string, number, min_rule, max_rule, email, boolean,
    in_rule, regex, date, float_rule, url, integer, contains
)

def test_required():
    assert required("value")[0] is True
    assert required("")[0] is False
    assert required(None)[0] is False

def test_string():
    assert string("text")[0] is True
    assert string(123)[0] is False

def test_number():
    assert number(123)[0] is True
    assert number("123")[0] is False

def test_min_rule():
    assert min_rule(5, 3)[0] is True
    assert min_rule(2, 3)[0] is False

def test_max_rule():
    assert max_rule(2, 3)[0] is True
    assert max_rule(5, 3)[0] is False

def test_email():
    assert email("test@example.com")[0] is True
    assert email("invalid-email")[0] is False

def test_boolean():
    assert boolean(True)[0] is True
    assert boolean("True")[0] is False

def test_in_rule():
    assert in_rule("apple", "apple", "banana")[0] is True
    assert in_rule("cherry", "apple", "banana")[0] is False

def test_regex():
    assert regex("abc123", r"^[a-z]+\d+$")[0] is True
    assert regex("123abc", r"^[a-z]+\d+$")[0] is False

def test_date():
    assert date("2025-04-24")[0] is True
    assert date("24-04-2025")[0] is False

def test_float_rule():
    assert float_rule(3.14)[0] is True
    assert float_rule("3.14")[0] is False

def test_url():
    assert url("https://example.com")[0] is True
    assert url("not-a-url")[0] is False

def test_integer():
    assert integer(10)[0] is True
    assert integer(10.5)[0] is False

def test_contains():
    assert contains("hello world", "world")[0] is True
    assert contains("hello", "world")[0] is False
