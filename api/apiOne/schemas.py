from api.apiOne import api
from flask_restx import fields

complex_schema = api.model(
    "complex_schema",
    {
        "val_one": fields.String(
            required=True,
            description="val_one",
            help="val_one cannot be blank.",
        ),

        "val_two": fields.String(
            required=False,
            description="val_two",
            help="val_two can be blank.",
        ),

        "val_three": fields.Integer(
            required=True,
            description="val_three",
            help="val_three cannot be blank.",
        ),

    },
)

simple_schema = api.model(
    "simple_schema", 
    {
        "val_only": fields.String(
            required=True,
            description="val_only",
            help="val_only cannot be blank"
        )
    }

)