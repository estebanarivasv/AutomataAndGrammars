from termcolor import cprint


def print_actual_letter(letter):
    if letter != "":
        cprint(f"\nActual letter from list: {letter}", "yellow")
    else:
        cprint(f"\nEnd of line detected.", "yellow")


def print_status(actual_state, next_state):
    if next_state == "accepting state":
        print(f"Move from {actual_state} to qAccept.")
        cprint("The introduced string was correct.", "green")
    elif next_state == "rejecting state":
        print(f"Move from state {actual_state} to qRej.")
        cprint("The introduced string was invalid.", "red")
    else:
        print(f"Move from state {actual_state} to {next_state}.")
