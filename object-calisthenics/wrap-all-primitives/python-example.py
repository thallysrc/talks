"""

Not wrapping the zip_code example,
wrap behavior for a primitive inside a class

"""
from dataclasses import dataclass


class Person:
    name: str
    zip_code: int

    def validate_zip_code(self):
        if not self.zip_code:
            print("invalid")


"""

Wrapping the behavior of zip_code inside their own class, so Person2,
no longer need to be responsible for zip_code behavior

"""

@dataclass
class ZipCode:
    code: int

    def __init__(self, code: int):
        self.validate(code)
        self.code = code

    @staticmethod
    def validate(code):
        if not code:
            print("invalid")

@dataclass
class Person2:
    name: str
    zip_code: ZipCode

    def __init__(self, name, code):
        self.name = name
        self.zip_code = code

p = Person2("jaskier codes", ZipCode(0))
