"""mapping types of json schema to their actual types"""
from types import MappingProxyType
from typing import Mapping, Union

Json_Schema = dict[str, Union[str, int, bool, list, dict]]
_SCHEMA_TYPE_MAP: Mapping[str, type] = MappingProxyType(
    {
        "string": str,
        "integer": int,
        "boolean": bool,
        "number":Union[int,float]
       
    }
)

json_schema: Json_Schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"},
        "isMarried": {"type": "boolean"},
    },
}

json_data: Json_Schema = {
    "name":"123",
    "age": 45.0,
    "isMarried": True,
}


def json_schema_validator(json_schema: Json_Schema, json_data: Json_Schema) -> bool:
      """main method for schema validator
      Here we are validating
      1.Object
      2.String
      3.Integer
      4.Number
      5.Boolean
      """
      try:
        if json_schema["type"] == "object":
                properties=json_schema["properties"]
                return all(
                    json_schema_validator(
                        json_schema["properties"][key], json_data[key]
                    )
                    for key in properties
                )

        return isinstance(json_data, _SCHEMA_TYPE_MAP[json_schema["type"]])
      except KeyError:
        return True


if json_schema_validator(json_schema, json_data):
    is_valid = "Valid"
else:
    is_valid = "Invalid"

print("Given JSON data is " + val)
