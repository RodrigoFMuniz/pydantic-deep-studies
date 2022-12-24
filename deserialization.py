from pydantic import BaseModel, ValidationError
from typing import Optional, Union
from datetime import date

class Person(BaseModel):
    first_name:str = None
    last_name:Optional[Union[str,None]]
    age:int | None
    date_of_birth: Optional[date]

class PersonParse(BaseModel):
    first_name:str 
    age: int | None 
        


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
    "date_of_birth": date(1992,10,10)
}


if __name__=="__main__":

    try:
        # p1 = Person(first_name='Foo', last_name="Boo",age=100, date_of_birth=date(1987,10,10))
        # p1 = Person(first_name='Foo', last_name="Boo",age=100, date_of_birth='1987-10-10')
        # p = p1.dict()
        # p = p1.json()
        # print(Person.parse_obj(p))
        dic1 = Person.parse_obj(data_dict)
        dict_serial = dic1.json(include={'first_name','age'}, indent=4)
        print(dict_serial)
        print(PersonParse.parse_raw(dict_serial))
        
    
    except ValidationError as err:
        print(err)



