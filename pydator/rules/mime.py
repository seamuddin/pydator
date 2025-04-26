import filetype

from pydator.base_rule import BaseRule  # Assuming BaseRule is your base class for validation rules


class MimeTypeRule(BaseRule):
    def __call__(self, value, *allowed_types):
        mime_type = get_mime_type(value)

        """ Check if the mime type is in allowed types  """
        if allowed_types and mime_type not in allowed_types:
            return False, self.message("mime_type", ", ".join(allowed_types))

        return True, None

    def message(self, field, *args):
        return f"Invalid file type. Allowed types: {args[0]}"


def get_mime_type(filepath):
    kind = filetype.guess(filepath)
    if kind is None:
        return "unknown/unknown"
    return kind.mime
