# Changelog

## [1.2.0] - 2025-04-26
### Added
- Added class-based validation rules (`RequiredRule`, `StringRule`, `NumberRule`, `MinRule`, `MaxRule`, `EmailRule`, `BooleanRule`, `InRule`, `RegexRule`, `DateRule`, `FloatRule`, `UrlRule`, `IntegerRule`, and `ContainsRule`).
- Centralized rule registry (`RULES`).

### Changed
- Refactored Validator class to support dynamic rule registration.
- Improved error message handling.

### Breaking Changes
- Rules must be class-based and registered.

---
