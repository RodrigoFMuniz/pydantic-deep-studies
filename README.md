# Pydantic

## what it does?

- Data validation and settings management using Python type annotations.

- Pydantic enforces type hints at runtime, and provides user friendly errors when data is invalid.

- Define how data should be in pure, canonical Python; validate it with pydantic.

## Basic use

### Importing

    from pydantic import BaseModel

### Signature

    from pydantic import BaseModel

    class Person(BaseModel):
        first_name:str
        last_name:str
        age:int

### Instance

    p1 = Person(first_name="Foo", last_name="Boo", age=1)

### Use

    if __name__=="__main__":
        p1 = Person(first_name="Foo", last_name="Boo", age=1)

        print(p1.first_name)
        print(p1.last_name)
        print(p1.age)

### Casting

    if __name__=="__main__":

        # it will works beacuse of python's capability to cast data.

        p2 = Person(first_name=200, last_name="test", age='10')

        print(p2.first_name)
        print(p2.last_name)
        print(p2.age)

### Error

    if __name__=="__main__":

        p3 = Person(first_name=200, last_name="test", age='hi')

        print(p3.first_name)
        print(p3.last_name)
        print(p3.age)


    Traceback (most recent call last):
    File "C:\Users\310049453\Documents\Pessoal\python_projects\pydantic\general.py", line 14, in <module>
        p3 = Person(first_name=200, last_name="test", age='hi')
    File "pydantic\main.py", line 342, in pydantic.main.BaseModel.__init__
    pydantic.error_wrappers.ValidationError: 1 validation error for Person
    age
    value is not a valid integer (type=type_error.integer)

### Using block try

    from pydantic import BaseModel, ValidationError

    class Person(BaseModel):
        first_name:str
        last_name:str
        age:int

    if __name__=="__main__":

        try:
            p1 = Person(first_name="Foo", last_name="Boo", age="error")

        except ValidationError as err:
            print(err)


    1 validation error for Person
    age
    value is not a valid integer (type=type_error.integer)

### Returning json structure

    if __name__=="__main__":

        try:
            p1 = Person(first_name="Foo", last_name="Boo", age="error")

        except ValidationError as err:
            # print(err)
            print(err.json())

    [
        {
            "loc": [
            "age"
            ],
            "msg": "value is not a valid integer",
            "type": "type_error.integer"
        }
    ]

### Returning an Array structure

    if __name__=="__main__":

        try:
            p1 = Person(first_name="Foo", last_name="Boo", age="error")

        except ValidationError as err:
            # print(err)
            # print(err.json()
            print(err.errors())


    [{'loc': ('age',), 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]

### Missing parameters

    from pydantic import BaseModel, ValidationError

    class Person(BaseModel):
        first_name:str
        last_name:str
        age:int


    if __name__=="__main__":

        try:
            p1 = Person(first_name="Foo")

        except ValidationError as err:
            print(err)

    # return

    2 validation errors for Person
    last_name
    field required (type=value_error.missing)
    age
    field required (type=value_error.missing)

### Optional parameters

    from pydantic import BaseModel, ValidationError
    from typing import Optional, Union

    class Person(BaseModel):
        first_name:str
        last_name:Optional[Union[str,None]] # using Optional + Union ||| or just Optional[str]
        age:int | None # Using 3.10+ feature "pipe"


    if __name__=="__main__":

        try:
            p1 = Person(first_name="Foo")
            print(p1)

        except ValidationError as err:
            print(err)

    # return

    first_name='Foo' last_name=None age=None

### Returning a dict

    if __name__=="__main__":

        try:
            p1 = Person(first_name="Foo")
            print(p1.dict())

        except ValidationError as err:
            print(err)

    # return

    {'first_name': 'Foo', 'last_name': None, 'age': None}

### Common Serialization

    if __name__=="__main__":

        try:
            p1 = Person(first_name="Foo", last_name="Boo",age=100)
            print(p1.dict(exclude={'first_name', 'age'}))

        except ValidationError as err:
            print(err)


    # return
    {'last_name': 'Boo'}
