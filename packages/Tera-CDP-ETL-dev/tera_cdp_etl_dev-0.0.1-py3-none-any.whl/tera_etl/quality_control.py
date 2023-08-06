from tera_etl.utils.schema import get_event_schema
from tera_etl.validations.schema_validation import validate
from enum import Enum


class QualityControlResult(Enum):
    ACCEPTED = 'ACCEPTED'
    REJECTED = 'REJECTED'


def classify_data(**kwargs) -> QualityControlResult:
    data_chunk, schema = kwargs  
    return QualityControlResult.ACCEPTED if __is_accepted(data_chunk, schema) else QualityControlResult.REJECTED


def __is_accepted(chunk, schema):
    if not __has_valid_schema(chunk, schema):
        return False
    return True


def __has_valid_schema(data, schema):
    ## TODO Phuoc:
    ## Move the schema validation from batch ingest into this
    return True if not validate(schema=schema, data=data) else False
