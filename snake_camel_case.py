from pydantic import BaseModel, ValidationError, Field
from typing import Optional, Union
from datetime import date

class Person(BaseModel):
    first_name:str = Field(default=None, alias="firstName")
    last_name:Optional[Union[str,None]] = Field(alias="lastName")
    age:int | None
    date_of_birth: date = Field(default= None,alias="dateOfBirth")

data_json = '''
{
    "first_name": "Guilhermo",
    "last_name": "Van Helsing",
    "age": 28,
    "date_of_birth": "1992-10-10"
}
'''
data_dict = {
    "first_name": "Guilhermo",
    "last_name": "Van Helsing",
    "age": 28,
    # "date_of_birth": date(1992,10,10)
}
data_dict2 = {
    "firstName": "Guilhermo",
    "lastName": "Van Helsing",
    "age": 28,
    "dateOfBirth": date(1992,10,10)
}

if __name__=="__main__":

    try:
      p = Person.parse_obj(data_dict2)
      p2 = Person(firstName="Newton",lastName="Isaac",  age=1000,dateOfBirth="1788-10-10")
      print(p2.json())
      p2_dict = p2.json()
      p2_des = Person.parse_raw(p2_dict)
      print(p2_des)
    
    except ValidationError as err:
        print(err.json())