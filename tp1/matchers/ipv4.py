import re

"""
    How it works?
    ?: - any expretion in the pharentesis will match
    1 - All patterns starting "1"
    \d - any decimal number
    \d? - can take a decimal or not
    2[0-4]\d - match any number starting with 2 and going to (0-5) followed by any decimal number
    {3} - All patterns matching "(?:\.(?:1?\d\d?|2[0-4]\d|25[0-5]))"
    \. - matching patterns starting with "."
    ?= - Matches if $ matches next
    [^\w.] - will match any character except \w.
"""

class Ipv4Matcher:
    def __init__(self, string):
        self.pattern = r"(?:1?\d\d?|2[0-4]\d|25[0-5])(?:\.(?:1?\d\d?|2[0-4]\d|25[0-5])){3}(?=$|[^\w.])"
        self.string = string
        
        
    def get_match(self):
        return re.findall(self.pattern, self.string)

string = "244.244.244.244\n164.0.15.100"
matcherEmail = Ipv4Matcher(string)
print(matcherEmail.get_match())
