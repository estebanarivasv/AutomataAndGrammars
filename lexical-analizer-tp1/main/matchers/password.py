import re

"""
    How it works?
    (?=^.{8,}$)  -- Matches if the string is greater than or equal to 8
    (?=.*\d)  -- Matches if the string contains one or more numbers
    (?=.*[A-Z])  -- Matches if the string contains one or more uppercase letters
    (?=.*[a-z])  -- Matches if the string contains one or more lowercase letters
    .*$  -- Matches any char except line breaks
"""


class PasswordMatcher:
    def __init__(self, strings_list):
        self.pattern = r"(?=^.{8,}$)(?=.*\d)(?=.*[A-Z])(?=.*[a-z]).*$"
        self.strings_list = strings_list
        self.matches = []

    def get_match(self):
        for string in self.strings_list:
            match = re.match(self.pattern, string)
            if match:
                self.matches.append(match.string)
        return self.matches
