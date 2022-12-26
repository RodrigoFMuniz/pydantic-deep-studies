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

### Dict Serialization

    if __name__=="__main__":

        try:
            p1 = Person(first_name="Foo", last_name="Boo",age=100)
            print(p1.dict(exclude={'first_name', 'age'}))

        except ValidationError as err:
            print(err)


    # return
    {'last_name': 'Boo'}

### Json serialization

    if __name__=="__main__":

        try:
            p1 = Person(first_name="Foo", last_name="Boo",age=100)
            print(p1.json(include={'first_name', 'age'}))


        except ValidationError as err:
            print(err)

    # return
    {"first_name": "Foo", "age": 100}

### Json Serialization with indentation

    if __name__=="__main__":

        try:
            p1 = Person(first_name='Foo', last_name="Boo",age=100)
            print(p1.json(include={'first_name', 'age'}, indent=4))

        except ValidationError as err:
            print(err)


    # return

    {
        "first_name": "Foo",
        "age": 100
    }

### Deserialization

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
            p1 = Person(first_name='Foo', last_name="Boo",age=100, date_of_birth=date(1987,10,10))
            p = p1.dict()
            print(Person.parse_obj(p))


        except ValidationError as err:
            print(err)

    # return

    first_name='Foo' last_name='Boo' age=100 date_of_birth=datetime.date(1987, 10, 10)

### Deserialization date cast

    if __name__=="__main__":

        try:
            p1 = Person(first_name='Foo', last_name="Boo",age=100, date_of_birth='1987-10-10')
            p = p1.dict()
            print(Person.parse_obj(p))


        except ValidationError as err:
            print(err)

    # return
    first_name='Foo' last_name='Boo' age=100 date_of_birth=datetime.date(1987, 10, 10)

### Deserialization json via parse_raw

    if __name__=="__main__":

        try:
            p1 = Person(first_name='Foo', last_name="Boo",age=100, date_of_birth='1987-10-10')
            p = p1.json()
            print(Person.parse_raw(p))


        except ValidationError as err:
            print(err)

    # return
    first_name='Foo' last_name='Boo' age=100 date_of_birth=datetime.date(1987, 10, 10)

### Using Camel case style instead of snake_case 

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

    # return 
    first_name=None last_name=None age=1000 date_of_birth=None


### After using Config class to enable features

    class Person(BaseModel):
        first_name:str = Field(default=None, alias="firstName")
        last_name:Optional[Union[str,None]] = Field(alias="lastName")
        age:int | None
        date_of_birth: date = Field(default= None,alias="dateOfBirth")

        class Config:
        allow_population_by_field_name = True
    

    # return 
    {"first_name": "Newton", "last_name": "Isaac", "age": 1000, "date_of_birth": "1788-10-10"}
    first_name='Newton' last_name='Isaac' age=1000 date_of_birth=datetime.date(1788, 10, 10)
