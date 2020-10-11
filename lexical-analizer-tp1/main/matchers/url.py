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
        self.strings_list = strings_list
        self.pattern = r'https?:\/\/w{3}\.\w+\.[\w\d:#@%/;/{3}$()~_?\+-=.&]*'

    def get_match(self):
        return re.findall(self.pattern, self.strings_list)

"""
string = "https://www.geeksforgeeks.org/python-check-url-string/\nhttp://www.geeksforgeeks.org/python-check-url-string/http://www.google.com"
matcher = UrlMatcher(string)
print(matcher.get_match())
"""