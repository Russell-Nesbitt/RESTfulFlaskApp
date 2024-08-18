from api.apiTwo import api
from flask_restx import fields

full_schema = api.model(
    "full_schema",
    {
        "val_id": fields.Integer(
            required=True,
            description="val_int",
            help="val_int cannot be blank"
        ),

        "val_one": fields.String(
            required=True,
            description="val_one",
            help="val_one cannot be blank.",
        ),

        "val_two": fields.String(
            required=True,
            description="val_two",
            help="val_two cannot be blank.",
        ),

    },
)

partial_schema = api.model(
    "partial_schema",
    {
        "val_id": fields.Integer(
            required=True,
            description="val_int",
            help="val_int cannot be blank"
        ),

        "val_one": fields.String(
            required=False,
            description="val_one",
            help="val_one can be blank.",
        ),

        "val_two": fields.String(
            required=False,
            description="val_two",
            help="val_two can be blank.",
        ),

    },
)

id_schema = api.model(
    "id_schema", 
    {
        "val_id": fields.Integer(
            required=True,
            description="val_int",
            help="val_int cannot be blank"
        )
    }

)