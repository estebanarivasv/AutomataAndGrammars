from time import sleep
from matchers import Ipv4Matcher
from matchers import UrlMatcher
import sys
import signal

def term_handler():
    print("Terminating string input...")
    break

    #commiteate por las dudas xd add . a huevo
def strings_catcher():
    # TENEMOS QUE HACER ALGO QUE NOS PERMITA INGRESAR CARACTERES HASTA QUE PRESIONEMOS ESCAPE
    inputs = []
    signal.signal(signal.SIGTERM, term_handler)
    while True:
        string = input("Enter values: ")
        inputs.append(string)
        print(inputs)
    
    """while True:
        string = input("Insert string: ")
        print(string)
    return string
    """

def call_url_matcher():
    string = strings_catcher()
    matcher = UrlMatcher(string)
    matches = matcher.get_match()
    if matches:
        print("The following matches have been found: ")
        print(matches)
    else:
        print("We were not able to get any matches.")


def call_ipv4_matcher():
    string = strings_catcher()
    matcher = Ipv4Matcher(string)
    match = matcher.get_match
    
    if match:
        print ("\n\nPattern Admitted")
        """splited_string = string.split(".",)
        max_ipv4 = int(255)
        if len(splited_string) == 4:
            print("correct number of octets")
        else:
            print("wrong number of octets")
            sleep(2)
            exit(0)
        if int(splited_string[0]) <= max_ipv4 & int(splited_string[1]) <= max_ipv4 & int(splited_string[2]) <= max_ipv4 & int(splited_string[3]) <= max_ipv4:
            print("passed (0-255)")
        else:
            print("the IPV4 entered exceeds the maximum allowed IP values [000.000.000.000-255.255.255.255]")
            sleep(2)
            exit(0)
        """
    else: 
        print("\n\nPattern not found")
        
