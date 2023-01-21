# 3 wrap primitives
from dataclasses import dataclass


class Person:
    name: str
    zipCode: int

    def validate_zip_code():
        pass

# p2 = Person(name="thallys", zipCode=1)

@dataclass
class ZipCode:
    code: int

    def __init__(self, code: str):
        self.validate(code)
        self.code = code

    def validate(self, code):
         print("validated")

@dataclass
class Person2:
    name: str
    zipCode: ZipCode

    def __init__(self, name, code):
        self.name = name
        self.zipCode = code

p = Person2("joao codigos", ZipCode(0))
print(p)
