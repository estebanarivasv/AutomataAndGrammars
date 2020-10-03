from time import sleep
import re


class Ipv4:
    def __init__(self, string):
        self.pattern = r"[\d].+[\d].+[\d].+[\d].+"
        self.string = string

    def get_match(self):
        return re.findall(self.pattern, self.string)

    def pattern_validator(self):
        splited_string = string.split(".",)
        max_ipv4 = int(255)
        if len(splited_string) == 4:
            print("cantidad de octetos correcta")
        else:
            print("cantidad de octetos erronea")
            sleep(2)
            exit(0)
        if int(splited_string[0]) <= max_ipv4 & int(splited_string[1]) <= max_ipv4 & int(splited_string[2]) <= max_ipv4 & int(splited_string[3]) <= max_ipv4:
            print("passed (0-255)")
        else:
            print("the IPV4 entered exceeds the maximum allowed IP values [000.000.000.000-255.255.255.255]")
            sleep(2)
            exit(0)

string = "244.244.244.244"
matcherEmail = Ipv4(string)
matcherEmail.pattern_validator()
