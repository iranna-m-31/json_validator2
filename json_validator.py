
from typing import Union


json_schema={
            "type": "object",
            "properties": {
                "name": {
                "type": "string",
                },
                "age": {
                "type": "integer"}
                },
                "isMarried": {
                "type": "boolean"
                }
            }

json_data={

        "name":"Iranna",
        "age":20,
        "isMarried":False,


}

def json_schema_validator(json_schema, json_data):
    
    #main method foe schema validator
      print(json_schema)
      try:
            if json_schema["type"]=="object":
                     for key in json_schema["properties"]:#checking for subschemas
                        if isinstance(json_schema["properties"][key],dict):
                            return True
                        else:
                            return False 
            elif json_schema["type"]=="string":#if data is of string type
               if isinstance(json_data,str):
                     return True
               else:
                  return False  
            elif json_schema["type"]=="integer":#if data is of integer type
               if isinstance(json_data,int):
                     return True
               else:
                  return False 
            elif json_schema["type"]=="boolean":#if data is of boolean type
               if isinstance(json_data,bool):
                     return True
               else:
                   return False
            elif json_schema["type"]=="number":#if data is ofnumber type
               if isinstance(json_data,int) or isinstance(json_data,float):
                     return True
               else:
                   return False
      except:
          return True        



if json_schema_validator(json_schema,json_data):
   print("Json json_data is valid against given JSON json_schema")
else:
   print("Json json_data is not valid against given JSON json_schema")