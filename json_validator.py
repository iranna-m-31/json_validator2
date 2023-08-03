
from typing import Union


json_schema={
            "type": "object",
            "properties": {
                "name": {
                "type": "string",
                "minLength": 1
                },
                "age": {
                "type": "integer",
                "minimum": 0,
                "maximum": 120
                },
                "email": {
                "type": "string",
                },
                "isMarried": {
                "type": "boolean"
                },
                "hobbies": {
                    "type":"string",
                    "enum":["travel","photography"]
                },
                "minItems": 1
                },
                "address": {
                "type": "object",
                "properties": {
                    "street": {
                    "type": "string"
                    },
                    "city": {
                    "type": "string"
                    },
                    "zipCode": {
                    "type": "string"
                    }
                },
                "required": ["street", "city"]
                },
        
            "required": ["name", "age"]
            }

json_data={

        "name":"Iranna",
        "age":20,
        "email":"ksjksjksjfj",
        "isMarried":False,
        "hobbies":"travel",
        "address":{
            "street":"oni",
            "city":"gld",
            "zipCode":"989898"
        }


}
def _validate_maximum_minimum_exmax_exmin(json_data: Union[str, int, bool], conditions: dict[str, Union[int, str]]) -> bool:
   """Method will validate the below properties of json json_schema
   1. MINIMUM
   2. MAXIMUM
   3. EXCLUSIVE_MINIMUM
   4. EXCLUSIVE_MAXIMUM
   """

   is_valid: bool = True
   if conditions['minimum'] is not None:
      is_valid &= (json_data >= conditions['minimum'])
   if conditions['maximum'] is not None:
      is_valid &= (json_data <= conditions['maximum'])
   if conditions['exclusiveMinimum'] is not None:
      is_valid &= (json_data > conditions['exclusiveMinimum'])
   if conditions['exclusiveMaximum'] is not None:
      is_valid &= (json_data < conditions['exclusiveMaximum'])
   return is_valid

def integer_maximum_minimum_check(json_data,json_schema):
   
   conditions: dict[str, Union[str, int, float]] = {
      "minimum": json_schema.get("minimum"),
      "maximum": json_schema.get("maximum"),
      "exclusiveMinimum": json_schema.get("exclusiveMinimum"),
      "exclusiveMaximum": json_schema.get("exclusiveMaximum"),
   }
   return _validate_maximum_minimum_exmax_exmin()(json_data, conditions)
def anyOf_allOf_oneOf_check(json_schema,json_data):
   if "anyOf" in json_schema:
         is_condition_satisfied: bool = False
         for inner_json_schema in json_schema["anyOf"]:
            is_condition_satisfied |= (json_data_validator(inner_json_schema,json_data))
         return is_condition_satisfied
   elif "allOf" in json_schema:
         is_condition_satisfied: bool = True
         for inner_json_schema in json_schema["allOf"]:
            is_condition_satisfied &= (json_data_validator(inner_json_schema,json_data))
         return is_condition_satisfied
   elif "oneOf" in json_schema:
         is_condition_satisfied = 0
         for inner_json_schema in json_schema["oneOf"]:
            is_condition_satisfied += (json_data_validator(inner_json_schema,json_data))
         if is_condition_satisfied==1:
             return True
         else:
             return False
   else:
       return True

def enum_check(json_schema,json_data):
    if "enum" in json_schema:
      if json_data in json_schema["enum"]:
         return True
      else:
         return False
    else:
         return True 
def required_list_check(json_schema,json_data,key):
   if "required" in json_schema:
       if key in json_schema["required"]:
          return True
       else:
          return False
   else:
      return True

def object_type_data_checker(json_schema,json_data):
    for key in json_schema:
        return type_check(json_schema,json_data)and anyOf_allOf_oneOf_check(json_schema,json_data) and required_list_check(json_schema,json_data)
def type_check(json_schema,json_data):
    breakpoint()
    if  json_schema["type"]=="object":
            for key in json_schema["properties"]:
                if isinstance(json_schema["properties"][key],dict) and required_list_check(json_schema,json_data,key) :
                        try:
                            if object_type_data_checker(json_schema["properties"][key],json_data[key]):
                                continue
                            else:
                                return False
                        except:
                            return False
                else:
                    continue
            return True
    elif json_schema["type"]=="string":
        if isinstance(json_data,str):
            return enum_check(json_schema,json_data)
        else:
           return False  
    elif json_schema["type"]=="integer":
        if isinstance(json_data,int):
            return integer_maximum_minimum_check(json_data,json_schema) and enum_check(json_schema,json_data)
        else:
           return False 
    elif json_schema["type"]=="boolean":
        if isinstance(json_data,bool):
            return True
        else:
            return False
    elif json_schema["type"]=="number":
        if isinstance(json_data,int) or isinstance(json_data,float):
            return integer_maximum_minimum_check(json_data,json_schema) and enum_check(json_schema,json_data)
        else:
            return False
def json_data_validator(json_schema,json_data):
    return type_check(json_schema,json_data) 

if json_data_validator(json_schema,json_data):
   print("Json json_data is valid against given JSON json_schema")
else:
   print("Json json_data is not valid against given JSON json_schema")