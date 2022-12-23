from pydantic import BaseModel

class Person(BaseModel):
    first_name:str
    last_name:str
    age:int


if __name__=="__main__":
    p1 = Person(first_name="Foo", last_name="Boo", age=1)

    p2 = Person(first_name=200, last_name="test", age=10) # it will works beacuse of python's capability to cast data.

    p3 = Person(first_name=200, last_name="test", age='hi') 

    print(p1.first_name)
    print(p1.last_name)
    print(p1.age)

    print(p2.first_name)
    print(p2.last_name)
    print(p2.age)

    print(p3.first_name)
    print(p3.last_name)
    print(p3.age)