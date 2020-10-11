from time import sleep
from matchers import Ipv4Matcher
from matchers import UrlMatcher
import sys
import signal
    

def strings_catcher():
    # TENEMOS QUE HACER ALGO QUE NOS PERMITA INGRESAR CARACTERES HASTA QUE PRESIONEMOS ESCAPE beio
    inputs = []
    while True:
        string = input("Enter values: ")
        print(repr(string))
        if string == "\n\t":
            break
        inputs.append(string)
        print(inputs)
    
    """while True:
        string = input("Insert string: ")
        print(string)
    return string
    """

def call_url_matcher():
    inputs = strings_catcher()
    matcher = UrlMatcher(inputs)
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
    else: 
        print("\n\nPattern not found")
        
