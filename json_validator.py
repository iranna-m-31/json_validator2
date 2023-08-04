"""mapping types of json schema to their actual types"""
from types import MappingProxyType
from typing import Mapping, Union

Json_Schema = dict[str, Union[str, int, bool, list, dict]]
_SCHEMA_TYPE_MAP: Mapping[str, type] = MappingProxyType(
    {
        "string": str,
        "integer": int,
        "boolean": bool,
    }
)

json_schema: Json_Schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
        "isMarried": {"type": "boolean"},
    },
}

json_data: Json_Schema = {
    "name": "rtry",
    "age": 90,
    "isMarried": True,
}


def json_schema_validator(json_schema: Json_Schema, json_data: Json_Schema) -> bool:
    """main method for schema validator"""
    try:
        if json_schema["type"] == "object":
            for key in json_schema["properties"]:
                return all(
                    json_schema_validator(
                        json_schema["properties"][key], json_data[key]
                    )
                    for key in json_data
                )
        if json_schema["type"] == "number":
            return isinstance(json_data, int) or isinstance(json_data, float)

        return isinstance(json_data, _SCHEMA_TYPE_MAP[json_schema["type"]])
    except:
        return True


if json_schema_validator(json_schema, json_data):
    val = "Valid"
else:
    val = "Invalid"

print("Given JSON data is " + val)
