import re


class Email:
    def __init__(self, string):
        self.pattern = r"[\w.]+@[\w.-]+"
        self.string = string

    def get_match(self):
        return re.findall(self.pattern, self.string)