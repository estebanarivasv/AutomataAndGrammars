import re

"""
    How it works?
    -
    -
    -
    -
    -
"""

class PasswordMatcher:
    def __init__(self, string):
        self.pattern = r"^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).*$"
        self.string = string

    def get_match(self):
        return re.findall(self.pattern, self.string)


string = "HOLAho2a"
matcher = PasswordMatcher(string)
print(matcher.get_match())