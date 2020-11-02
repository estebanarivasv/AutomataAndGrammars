import os
from termcolor import colored

from main.turing_machines import bin_replacer


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


def string_catcher():
    print("-------------------------------------------------------------"
          "\n\nReading from input..."
          "\n")
    input_str = input("--> ")

    print(colored(text=f"\nEntered string: {input_str}\n", color='yellow'))
    input("\nContinue...")
    return input_str


def call_bin_replacer():
    print(
        "\nHow does the turing machine work?"
        "\n- The turing machine must change the ones for zeroes or viceversa."
        "\n\n"
    )
    str_input = string_catcher()


def call_parity_tester():
    print(
        "\nHow does the turing machine work?"
        "\n- The turing machine must add a zero at the end if the quantity of ones is odd."
        "\n- It also must add a one if the quantity of ones is even."
        "\n\n"
    )
    str_input = string_catcher()