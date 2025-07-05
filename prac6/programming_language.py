"""
programming_language.py

Estimated time: 30 minutes

Actual time: minutes
"""
class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing.lower() == "dynamic"