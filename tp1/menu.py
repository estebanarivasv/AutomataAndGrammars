from time import sleep
from matchers import EmailMatcher
from matchers import Ipv4Matcher


# bueno ponete con email y volves xd

def strings_catcher():
    # TENEMOS QUE HACER ALGO QUE NOS PERMITA INGRESAR CARACTERES HASTA QUE PRESIONEMOS ESCAPE
    string = input("Insert string: ")
    return string

def call_email_matcher():
    string = strings_catcher()
    matcher = EmailMatcher(string)
    matches = matcher.get_match()
    if matches:
        print("The following matches have been found: ")
        for match in matches:
            print(match)
    else:
        print("We were not able to get any matches.")


def call_ipv4_matcher():
    string = input("Insert string: ")
    matcher = Ipv4Matcher(string)
    match = matcher.get_match
    
    if match:
        print ("\n\nPattern Admitted")
        splited_string = string.split(".",)
        max_ipv4 = int(255)
        if len(splited_string) == 4:
            print("correct number of octets")
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
        
        
    else: 
        print("\n\nPattern not found")
        
