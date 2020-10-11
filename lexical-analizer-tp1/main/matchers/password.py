import re

"""
    How it works?
    .{8,} - its a "replacement" for scanf(), equivalent of %8c  (8 characteres)
    ?=    - Matches if .{8,} matches next
    \d    - any numeber
    *[a-z] - any letter from a to z
    *[A-Z] - any letter from A to Z
    ^ - matches the start of the string
    $ - matches the end of the string
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

# YA LO TERMINASTE?