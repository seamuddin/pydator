# Pydator

[![CI](https://github.com/seamuddin/pydator/workflows/CI/badge.svg?event=push)](https://github.com/seamuddin/pydator/actions?query=event%3Apush+branch%3Amain+workflow%3ACI)
[![Coverage](https://img.shields.io/codecov/c/github/seamuddin/pydator)](https://codecov.io/gh/seamuddin/pydator)
[![PyPI version](https://img.shields.io/pypi/v/pydator.svg)](https://pypi.org/project/pydator/)
[![Conda-Forge](https://img.shields.io/conda/v/conda-forge/pydator.svg)](https://anaconda.org/conda-forge/pydator)
[![Downloads](https://pepy.tech/badge/pydator/month)](https://pepy.tech/project/pydator)
[![Python Versions](https://img.shields.io/pypi/pyversions/pydator.svg)](https://pypi.org/project/pydator/)
[![License](https://img.shields.io/github/license/seamuddin/pydator.svg)](https://github.com/seamuddin/pydator/blob/main/LICENSE)

Pydator is a lightweight, easy-to-use validation library for Python. It provides a clean and intuitive way to validate data using predefined rules.

## Installation

```bash
# Using pip
pip install pydator

# Using conda
conda install -c conda-forge pydator
```

## Quick Start

```python
from pydator.validator import Validator

# Data to validate
data = {
    "username": "john_doe123",
    "email": "john@example.com",
    "age": 30
}

# Define validation rules
rules = {
    "username": ["required", "string", "min:3", "max:20"],
    "email": ["required", "email"],
    "age": ["required", "integer", "min:18"]
}

# Create validator
validator = Validator(data, rules)

# Validate data
if validator.validate():
    print("All validations passed!")
else:
    print("Validation errors:", validator.errors)
```

## Features

- Simple and intuitive API
- Multiple validation rules per field
- Custom error messages
- Extensive built-in validation rules
- Easy to extend with custom rules

## Available Validation Rules

| Rule | Description | Example |
|------|-------------|---------|
| `required` | Field must be present and not empty | `"name": ["required"]` |
| `string` | Field must be a string | `"name": ["string"]` |
| `number` | Field must be a number (integer or float) | `"price": ["number"]` |
| `min:value` | Minimum value for numbers, minimum length for strings | `"age": ["min:18"]` |
| `max:value` | Maximum value for numbers, maximum length for strings | `"bio": ["max:200"]` |
| `email` | Field must be a valid email address | `"email": ["email"]` |
| `boolean` | Field must be a boolean value | `"active": ["boolean"]` |
| `in:val1,val2,val3` | Field value must be in the specified list | `"status": ["in:pending,active,completed"]` |
| `regex:pattern` | Field must match the regular expression pattern | `"username": ["regex:^[a-zA-Z0-9_]+$"]` |
| `date` | Field must be a valid date string | `"birth_date": ["date"]` |
| `float` | Field must be a float number | `"weight": ["float"]` |
| `url` | Field must be a valid URL | `"website": ["url"]` |
| `integer` | Field must be an integer | `"age": ["integer"]` |
| `contains:value` | Field must contain the specified value | `"description": ["contains:important"]` |

## Advanced Usage

### Custom Error Messages

You can customize error messages for specific rules:

```python
data = {
    "username": "",
    "email": "invalid-email"
}

rules = {
    "username": ["required", "string"],
    "email": ["required", "email"]
}

messages = {
    "username.required": "Username is required!",
    "email.email": "Please provide a valid email address."
}

validator = Validator(data, rules, messages)

if not validator.validate():
    print(validator.errors)
    # Output: {'username': ['Username is required!'], 'email': ['Please provide a valid email address.']}
```

### Complete Example

Here's a comprehensive example showing most features:

```python
from pydator.validator import Validator

data = {
    "username": "john_doe123",
    "email": "john@example.com",
    "age": 30,
    "is_active": True,
    "website": "https://example.com",
    "signup_date": "2025-04-24",
    "bio": "Software developer with 10 years of experience.",
    "password": "SecurePass123!",
    "confirm_password": "SecurePass123!",
    "referral_code": "ABC123XYZ",
}

rules = {
    "username": ["required", "string", "min:3", "max:20", "regex:^[a-zA-Z0-9_]+$"],
    "email": ["required", "email"],
    "age": ["required", "integer", "min:18", "max:65"],
    "is_active": ["required", "boolean"],
    "website": ["required", "url"],
    "signup_date": ["required", "date"],
    "bio": ["string", "max:100"],
    "password": ["required", "string", "min:8"],
    "confirm_password": ["required", "string", "min:8"],
    "referral_code": ["string", "regex:^[A-Z0-9]{9}$"],
    "ip_address": ["required", "string"],
}

messages = {
    "username.required": "Username is required!",
    "username.min": "Username must be at least 3 characters long.",
    "username.max": "Username must not exceed 20 characters.",
    "username.regex": "Username can only contain letters, numbers, and underscores.",
    "email.required": "Email address is required!",
    "email.email": "Please provide a valid email address.",
    "age.required": "Age is required!",
    "age.integer": "Age must be a valid number.",
    "age.min": "You must be at least 18 years old.",
    "age.max": "Age must not exceed 65.",
    "is_active.required": "Please specify if the account is active.",
    "is_active.boolean": "Active status must be a boolean value.",
    "website.required": "Website URL is required!",
    "website.url": "Please provide a valid URL.",
    "signup_date.required": "Signup date is required!",
    "signup_date.date": "Please provide a valid date.",
    "bio.max": "Bio must not exceed 100 characters.",
    "password.required": "Password is required!",
    "password.min": "Password must be at least 8 characters long.",
    "confirm_password.required": "Please confirm your password.",
    "confirm_password.min": "Confirmation password must be at least 8 characters long.",
    "referral_code.regex": "Referral code must be exactly 9 characters long and alphanumeric.",
    "ip_address.required": "IP address is required!",
}

validator = Validator(data, rules, messages)

if validator.validate():
    print("All validations passed!")
else:
    print("Validation errors:", validator.errors)
```

## Extending with Custom Rules

You can create custom validation rules by extending the `rules.py` module:

```python
from pydator.rules import RULES

def phone_number(value):
    import re
    pattern = r'^\+?[1-9]\d{1,14}$'
    if not re.match(pattern, str(value)):
        return False
    return True

# Add your custom rule to the RULES dictionary
RULES["phone"] = phone_number

# Now you can use it in your validation rules
rules = {
    "contact": ["required", "phone"]
}
```

## Why Pydator?

- **Simplicity**: Easy to learn and use with a clean, intuitive API
- **Flexibility**: Validate any data structure with customizable rules
- **Performance**: Lightweight with minimal dependencies
- **Extensible**: Easy to add custom validation rules
- **Readable**: Straightforward validation definitions that are easy to understand

## Comparison with other validation libraries

| Feature | Pydator | Other Validation Libraries |
|---------|---------|---------------------------|
| Learning Curve | Minimal | Often steeper |
| Configuration | Simple dict-based | Various (class-based, schema-based) |
| Custom Rules | Easy to add | Usually requires more code |
| Dependencies | Minimal | Often more dependencies |
| Performance | Lightweight | Can be heavier |

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the terms of the MIT license. See [LICENSE](LICENSE) for more details.