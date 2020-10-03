import re

"""
    Basic  
    http - All patterns matching "https"
    s? - Optional
    ://
    w{3}
    \.
    \w+
    \.
    [\w\d:#@%/;$()~_?\+-=\\\.&]*

"""

class UrlMatcher:
    def __init__(self, string):
        self.string = string
        self.pattern = r'https?://w{3}\.\w+\.[\w\d:#@%/;$()~_?\+-=\\\.&]*'
        
        # http o https
        # mas todo lo que venga

    def get_match(self):
        return re.findall(self.pattern, self.string)
        

string = "https://www.geeksforgeeks.org/python-check-url-string/\nhttp://www.geeksforgeeks.org/python-check-url-string/"
matcher = UrlMatcher(string)
print(matcher.get_match())
