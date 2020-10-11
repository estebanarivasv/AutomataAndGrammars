import re

"""
    How it works?
    http - All patterns matching "https"
    s? - Optional char
    :\/\/ - All patterns matching "://"
    w{3} - All patterns matching "www"
    \. - Escaping "."
    \w+ - All patterns matching any word type characters
    \. - Escaping "."
    [\w\d:#@%/;$()~_?\+-=\.&]* - All patterns matching url type characters
    \s - White space caracter
"""


class UrlMatcher:
    def __init__(self, strings_list):
        self.pattern = r'https?:\/\/w{3}\.\w+\.[\w\d:#@%/;/{3}$()~_?\+-=.&]*'
        self.strings_list = strings_list
        self.matches = []

    def get_match(self):
        for string in self.strings_list:
            match = re.match(self.pattern, string)
            if match:
                self.matches.append(match.string)
        return self.matches
