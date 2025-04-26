import re
from datetime import datetime
from urllib.parse import urlparse


def required(value, *args):
    if value is None or (isinstance(value, str) and not value.strip()):
        return False, "This field is required."
    return True, None


def string(value, *args):
    if not isinstance(value, str):
        return False, "Must be a string."
    return True, None


def number(value, *args):
    if not isinstance(value, (int, float)):
        return False, "Must be a number."
    return True, None


def min_rule(value, min_val):
    min_val = int(min_val)
    if isinstance(value, (str, list)) and len(value) < min_val:
        return False, f"Minimum length is {min_val}."
    if isinstance(value, (int, float)) and value < min_val:
        return False, f"Minimum value is {min_val}."
    return True, None


def max_rule(value, max_val):
    max_val = int(max_val)
    if isinstance(value, (str, list)) and len(value) > max_val:
        return False, f"Maximum length is {max_val}."
    if isinstance(value, (int, float)) and value > max_val:
        return False, f"Maximum value is {max_val}."
    return True, None


def email(value, *args):
    if not isinstance(value, str):
        return False, "Must be a valid email address."
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(pattern, value):
        return False, "Invalid email format."
    return True, None


def boolean(value, *args):
    if not isinstance(value, bool):
        return False, "Must be a boolean."
    return True, None


def in_rule(value, *args):
    if value not in args:
        return False, f"Value must be one of: {', '.join(args)}."
    return True, None


def date(value, *args):
    if not isinstance(value, str):
        return False, "Must be a string representing a date."
    try:
        datetime.fromisoformat(value)
        return True, None
    except ValueError:
        return False, "Invalid date format. Expected ISO format (YYYY-MM-DD)."


def url(value, *args):
    if not isinstance(value, str):
        return False, "Must be a string representing a URL."
    parsed = urlparse(value)
    if not all([parsed.scheme, parsed.netloc]):
        return False, "Invalid URL format."
    return True, None


def regex(value, pattern, *args):
    if not isinstance(value, str):
        return False, "Value must be a string to apply regex."
    if not re.match(pattern, value):
        return False, f"Value does not match the required pattern: {pattern}"
    return True, None


def integer(value, *args):
    if not isinstance(value, int):
        return False, "Must be an integer."
    return True, None


def float_rule(value, *args):
    if not isinstance(value, float):
        return False, "Must be a float."
    return True, None


def alpha(value, *args):
    if not isinstance(value, str):
        return False, "Must be a string."
    if not value.isalpha():
        return False, "Must contain only alphabetic characters."
    return True, None


def alphanumeric(value, *args):
    if not isinstance(value, str):
        return False, "Must be a string."
    if not value.isalnum():
        return False, "Must contain only alphanumeric characters."
    return True, None


def starts_with(value, prefix):
    if not isinstance(value, str):
        return False, "Must be a string."
    if not value.startswith(prefix):
        return False, f"Must start with '{prefix}'."
    return True, None


def ends_with(value, suffix):
    if not isinstance(value, str):
        return False, "Must be a string."
    if not value.endswith(suffix):
        return False, f"Must end with '{suffix}'."
    return True, None


def contains(value, substring):
    if not isinstance(value, str):
        return False, "Must be a string."
    if substring not in value:
        return False, f"Must contain '{substring}'."
    return True, None


RULES = {
    "required": required,
    "string": string,
    "number": number,
    "min": min_rule,
    "max": max_rule,
    "email": email,
    "boolean": boolean,
    "in": in_rule,
    "regex": regex,
    "date": date,
    "float": float_rule,
    "url": url,
    "integer": integer,
    "contains": contains
}
