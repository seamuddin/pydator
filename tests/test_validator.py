import pytest
from pydator.rules import (
    RequiredRule, StringRule, NumberRule, MinRule, MaxRule, EmailRule, BooleanRule,
    InRule, RegexRule, DateRule, FloatRule, UrlRule, IntegerRule, ContainsRule
)


def test_required():
    assert RequiredRule()("value")[0] is True
    assert RequiredRule()("")[0] is False
    assert RequiredRule()(None)[0] is False


def test_string():
    assert StringRule()("text")[0] is True
    assert StringRule()(123)[0] is False


def test_number():
    assert NumberRule()(123)[0] is True
    assert NumberRule()("123")[0] is False


def test_min_rule():
    assert MinRule()(5, 3)[0] is True
    assert MinRule()(2, 3)[0] is False


def test_max_rule():
    assert MaxRule()(2, 3)[0] is True
    assert MaxRule()(5, 3)[0] is False


def test_email():
    assert EmailRule()("test@example.com")[0] is True
    assert EmailRule()("invalid-email")[0] is False


def test_boolean():
    assert BooleanRule()(True)[0] is True
    assert BooleanRule()("True")[0] is False


def test_in_rule():
    assert InRule()("apple", "apple", "banana")[0] is True
    assert InRule()("cherry", "apple", "banana")[0] is False


def test_regex():
    assert RegexRule()("abc123", r"^[a-z]+\d+$")[0] is True
    assert RegexRule()("123abc", r"^[a-z]+\d+$")[0] is False


def test_date():
    assert DateRule()("2025-04-24")[0] is True
    assert DateRule()("24-04-2025")[0] is False


def test_float_rule():
    assert FloatRule()(3.14)[0] is True
    assert FloatRule()("3.14")[0] is False


def test_url():
    assert UrlRule()("https://example.com")[0] is True
    assert UrlRule()("not-a-url")[0] is False


def test_integer():
    assert IntegerRule()(10)[0] is True
    assert IntegerRule()(10.5)[0] is False


def test_contains():
    assert ContainsRule()("hello world", "world")[0] is True
    assert ContainsRule()("hello", "world")[0] is False
