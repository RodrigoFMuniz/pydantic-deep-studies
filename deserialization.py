from pydantic import BaseModel, ValidationError
from typing import Optional, Union
from datetime import date

class Person(BaseModel):
    first_name:str
    last_name:Optional[Union[str,None]]
    age:int | None
    date_of_birth: date


data_json = """
{
    "first_name": "Guilhermo,
    "last_name": "Van Helsing",
    "age": 28,
    "date_of_birth": date(1992,10,10)
}
"""

if __name__=="__main__":

    try:
        # p1 = Person(first_name='Foo', last_name="Boo",age=100, date_of_birth=date(1987,10,10))
        p1 = Person(first_name='Foo', last_name="Boo",age=100, date_of_birth='1987-10-10')
        # p = p1.dict()
        p = p1.json()
        # print(Person.parse_obj(p))
        print(Person.parse_raw(p))
        
    
    except ValidationError as err:
        print(err)



