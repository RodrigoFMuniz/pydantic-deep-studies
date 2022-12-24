from pydantic import BaseModel, ValidationError

class Person(BaseModel):
    first_name:str
    last_name:str
    age:int


if __name__=="__main__":

    try:
        p1 = Person(first_name="Foo", last_name="Boo", age="error")
    
    except ValidationError as err:
        # print(err)
        print(err.json())


