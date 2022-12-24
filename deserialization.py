from pydantic import BaseModel, ValidationError
from typing import Optional, Union
from datetime import date

class Person(BaseModel):
    first_name:str
    last_name:Optional[Union[str,None]]
    age:int | None
    date_of_birth: date


if __name__=="__main__":

    try:
        # p1 = Person(first_name='Foo', last_name="Boo",age=100, date_of_birth=date(1987,10,10))
        p1 = Person(first_name='Foo', last_name="Boo",age=100, date_of_birth='1987-10-10')
        p = p1.dict()
        print(Person.parse_obj(p))
        
    
    except ValidationError as err:
        print(err)



