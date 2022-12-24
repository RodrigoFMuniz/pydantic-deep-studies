from pydantic import BaseModel, ValidationError
from typing import Optional, Union

class Person(BaseModel):
    first_name:str
    last_name:Optional[Union[str,None]]
    age:int | None


if __name__=="__main__":

    try:
        p1 = Person(first_name='Foo', last_name="Boo",age=100)
        # print(p1.dict())
        # print(p1.dict(exclude={'first_name', 'age'}))
        # print(p1.json())
        # print(p1.json(include={'first_name', 'age'}))
        print(p1.json(include={'first_name', 'age'}, indent=4))
        # print(p1)
    
    except ValidationError as err:
        print(err)



