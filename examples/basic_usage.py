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
    "bio": ["string", "max_length:100"],
    "confirm_password": ["required", "string", "min_length:8"],
    "referral_code": ["string", "length:9", "alphanumeric"],
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
    "bio.max_length": "Bio must not exceed 100 characters.",
    "password.required": "Password is required!",
    "password.min_length": "Password must be at least 8 characters long.",
    "password.regex": "Password must contain at least one letter and one number.",
    "confirm_password.required": "Please confirm your password.",
    "confirm_password.min_length": "Confirmation password must be at least 8 characters long.",
    "referral_code.length": "Referral code must be exactly 9 characters long.",
    "referral_code.alphanumeric": "Referral code must be alphanumeric.",
}

validator = Validator(data, rules, messages)

if validator.validate():
    print("All validations passed!")
else:
    print("Validation errors:", validator.errors)