from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str()
    # Add other user fields like password, email, etc.

class PlantSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    # care_instructions = fields.Str()
    # Add other plant fields like image, etc.

# Define similar schemas for other models