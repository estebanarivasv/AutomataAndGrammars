from time import sleep
from termcolor import colored
from main.matchers import UrlMatcher
import sys
import os
import signal


def clear_screen():
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')


def get_result(matches):
    clear_screen()
    if matches:
        print(colored(text=f"-------------------------------------------------------------\n"
                           "The following matches have been found: \n", color="green"))
        for match in matches:
            print(colored(text=repr(match), color="green"))
        print("\n")
    else:
        print(colored(text="-------------------------------------------------------------\n"
                           "We were not able to get any matches.", color="red"))
        print("\n")


def strings_catcher():
    clear_screen()
    inputs = []
    print("-------------------------------------------------------------"
          "\n\nReading from input..."
          "\nTo stop text input, just hit ENTER key."
          "\n")
    while True:
        string = input("--> ")
        if string == '':
            break
        inputs.append(string)

    print(colored(text="\nEntered strings:", color='yellow'))
    for string in inputs:
        print(colored(text=repr(string), color='yellow'))
    print("\n")

    princ_string = ""
    for string in inputs:
        princ_string = princ_string + string + "\n"
    return princ_string


def call_url_matcher():
    print(
        "\nREQUIREMENTS:"
        "\n- Must begin with 'http' or 'https'"
        "\n- Must contain 'www.'"
    )
    inputs = strings_catcher()
    matcher = UrlMatcher(inputs)
    matches = matcher.get_match()
    get_result(matches)


"""
def call_ipv4_matcher():
    string = strings_catcher()
    matcher = Ipv4Matcher(string)
    match = matcher.get_match

    if match:
        print("\n\nPattern Admitted")
    else:
        print("\n\nPattern not found")
"""
