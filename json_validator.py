from types import MappingProxyType
from typing import Mapping
"""
mapping types 
of json schema to their
actual types
"""
_SCHEMA_TYPE_MAP: Mapping[str, type] = MappingProxyType(
     {
          "string": str,
          "integer": int,
          "boolean": bool,
     }
)
json_schema:dict ={
            # write 
            #your 
            #json
            #schema 
            #here
            "type": "object",
            "properties": {
                "name": {
                "type": "string",
                },
                "age": {
                "type": "integer"
                },
                "isMarried": {
                "type": "boolean"
                }
            }
}

json_data:dict ={
          # write 
            #your 
            #json
            #data
            #here
        "name":"imm",
        "age":8,
        "isMarried":True,


}

def json_schema_validator(json_schema, json_data):
    
      """main method foe 
      schema validator"""
      try:
            if json_schema["type"] == "object":
                     for key in json_schema["properties"]:
                        if isinstance(json_schema["properties"][key], dict):
                                    if json_schema_validator(json_schema["properties"][key],json_data[key]):
                                       continue
                                    else:
                                       return False
                        else:
                           continue
                     return True
            if json_schema["type"] == "number":
                  return isinstance(json_data,int) or isinstance(json_data,float)

            return isinstance(json_data, _SCHEMA_TYPE_MAP[json_schema["type"]])
      except:
          return True      
      
if json_schema_validator(json_schema,json_data):
   val="Valid"
else:
   val="Invalid"

print("Given JSON data is "+ val)