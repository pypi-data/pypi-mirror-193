from tera_etl.utils.schema import get_event_schema
from tera_etl.validations.schema_validation import validate
from enum import Enum


class QualityControlResult(Enum):
    ACCEPTED = 'ACCEPTED'
    REJECTED = 'REJECTED'


def classify_data(data_chunk, schema, **kwargs) -> QualityControlResult:
    is_accepted = __is_accepted(data_chunk, schema)
    return {
        "qc_type": QualityControlResult.ACCEPTED if is_accepted["status"] else QualityControlResult.REJECTED,
        "errors": is_accepted["errors"]
    }


def __is_accepted(chunk, schema):
    return __has_valid_schema(chunk, schema)


def __has_valid_schema(data, schema):
    errors = validate(schema=schema, data=data)
    return {
        "status": True if not errors else False,
        "errors": errors,
    }
