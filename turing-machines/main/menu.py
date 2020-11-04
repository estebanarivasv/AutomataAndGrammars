import os
from termcolor import colored

from main.turing_machines import BinaryParityTester, BinaryReplacer

def clear_screen():
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')


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
    # The turing machine must change the ones for zeroes or viceversa
    tm = BinaryReplacer()
    tm.set_input(str_input)
    tm.current = "qWrite0"  # Set as initial state
    tm.run_tm()


def call_parity_tester():
    print(
        "\nHow does the turing machine work?"
        "\n- The turing machine must add a zero at the end if the quantity of ones is odd."
        "\n- It also must add a one if the quantity of ones is even."
        "\n\n"
    )
    str_input = string_catcher()
    tm = BinaryParityTester()
    tm.set_input(str_input)
    tm.current = "qEven"  # Set as initial state
    tm.run_tm()

