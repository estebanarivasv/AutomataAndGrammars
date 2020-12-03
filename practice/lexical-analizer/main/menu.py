import os
from termcolor import colored

from main.matchers import UrlMatcher, EmailMatcher, Ipv4Matcher, PasswordMatcher


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
    else:
        print(colored(text="-------------------------------------------------------------\n"
                           "We were not able to get any matches.", color="red"))
    input("\n\nPress any key to go back to menu...")


def strings_catcher():
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

    input("\nContinue...")
    return inputs


def call_url_matcher():
    print(
        "\nREQUIREMENTS:"
        "\n- Must begin with 'http' or 'https'"
        "\n- Must contain 'www.'"
        "\n\n"
    )
    inputs = strings_catcher()
    matcher = UrlMatcher(inputs)
    matches = matcher.get_match()
    get_result(matches)


def call_email_matcher():
    print(
        "\nREQUIREMENTS:"
        "\n- Must contain '@'"
        "\n- Must contain '.'"
        "\n\n"
    )
    inputs = strings_catcher()
    matcher = EmailMatcher(inputs)
    matches = matcher.get_match()
    get_result(matches)


def call_ipv4_matcher():
    print(
        "\nREQUIREMENTS:"
        "\n- Must contain from 1 to 3 characters each octet"
        "\n- Must contain '.'"
        "\n\n"
    )
    inputs = strings_catcher()
    matcher = Ipv4Matcher(inputs)
    matches = matcher.get_match()
    get_result(matches)


def call_password_matcher():
    print(
        "\nREQUIREMENTS:"
        "\n- At least one uppercase letter."
        "\n- At least one lowercase letter."
        "\n- At least one number."
        "\n- The minimum length of 8 characters."
        "\n\n"
    )
    inputs = strings_catcher()
    matcher = PasswordMatcher(inputs)
    matches = matcher.get_match()
    get_result(matches)
