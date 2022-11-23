"""
david A. V. gr 405
exercise 1
"""


class StringFoo:
    def __init__(self, message):
        self.message = message

    def print_string(self):
        print(self.message)

david = StringFoo('roger')
print(david.message)
david.print_string()