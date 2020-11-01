from termcolor import colored, cprint

# (a|b)*

# We define the movements for each state given certain inputs.
state_inputs = [
    {"name": "state A", "a": "B", "b": "C", "finish": "accepting state", "error": "rejecting state"},
    {"name": "state B", "a": "B", "b": "C", "finish": "accepting state", "error": "rejecting state"},
    {"name": "state C", "a": "B", "b": "C", "finish": "accepting state", "error": "rejecting state"}
]


def print_actual_letter(char):
    if char != "":
        cprint(f"Actual letter from list: {letter}", "yellow")


def print_status(actual_state, next_state):
    if next_state == "accepting state":
        print(f"\nMove from state {actual_state} to {next_state}.")
        cprint("The introduced string was correct.", "green")
    elif next_state == "rejecting state":
        print(f"\nMove from state {actual_state} to {next_state}.")
        cprint("The introduced string was invalid.", "red")
    else:
        print(f"\nMove from state {actual_state} to {next_state}.")


# This function defines the next state to be accessed given a certain value
def index_changer(next_state):
    if next_state == "B":
        return 1
    elif next_state == "C":
        return 2


if __name__ == "__main__":

    test_str = input(colored("\nEnter the string to test\n>>>  ", "cyan"))

    # String to list conversion
    char_list = list(test_str)
    # We add "" at the end to get to the acceptance state
    char_list.append("")

    # This variable will be modified as the program runs. We begin in state A
    state_index = 0

    for letter in char_list:
        # We define the actual state
        actual = state_inputs[state_index]

        print_actual_letter(letter)

        if letter == "a":
            state_index = index_changer(actual['a'])
            # index_changer sets the following state given an input "a" defined in dict "state"
            print_status(actual['name'], actual['a'])
            # Given an input "b", the program stops and enters to the next state

        elif letter == "b":
            state_index = index_changer(actual['b'])

            print_status(actual['name'], actual['b'])
            # Given an input "b", the program stops and enters to the next state

        elif letter == "":
            print_status(actual['name'], actual['finish'])
            break
            # Given an input "", the program stops and enters to the accepting state

        else:
            print_status(actual['name'], actual['error'])
            break
            # Given an input different that the admitted characters, it will raise an error.
            # The program stops and enters to the rejecting state
