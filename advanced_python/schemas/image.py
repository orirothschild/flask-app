from marshmallow import Schema, fields
from werkzeug.datastructures import FileStorage

"""
this schema is only for desiriasing
so no model for image exists

"""

"""
we can create our own fields for schema using a class
that inheirts from fields

"""


class FileStorageField(fields.Field):
    default_error_messages = {
        "invalid": "Not a valid image"
    }

    def _deserialize(self, value, attr, data, **kwargs) -> FileStorage:
        if value is None:
            return None
        if not isinstance(value, FileStorage):
            self.fail("invalid")  # raise an error for try catch
        return value


class ImageSchema(Schema):
    image = FileStorageField(required=True)
