import re

"""
    How it works?
    \w+   -- Matches any word caracter
    [\.\-\_]?  -- Matches any caracter set
    @  -- Matches a "@" caracter
    .  -- Matches a "." caracter
"""


class EmailMatcher:
    def __init__(self, strings_list):
        self.pattern = r"\w+[\.\-\_]?\w+@\w+.\w+"
        self.strings_list = strings_list
        self.matches = []

    def get_match(self):
        for string in self.strings_list:
            match = re.match(self.pattern, string)
            if match:
                self.matches.append(match.string)
        return self.matches
