from colorclass import Color
from termcolor import cprint
from terminaltables import SingleTable

"""
    Syntax:     states = [Dict, Dict, ..., Dict]

    Each state will have:
    {"name": "",
     "inputs":  {
                },
     "write": "",
     "move": ""},       Right or Left

"""


class BinaryParityTester:
    name = "Binary parity tester"
    states = [
        # qEven - Shows if the number of ones are even
        {"name": "qEven",
         "inputs": {
             "0": "qEven",
             "1": "qOdd"
         },
         "move": "R"},
        # qOdd - Shows if the number of ones are odd
        {"name": "qOdd",
         "inputs": {
             "0": "qOdd",
             "1": "qEven"
         },
         "move": "R"}
    ]
    input = []  # Input list from given string
    tape = []  # len(input) + 6
    control_position = 1  # Position of the tm's control head
    current = ""  # Describes the current state index
    c_state = {}
    reject = False

    def set_input(self, string):

        self.input = list(string)
        self.input.insert(0, "")
        self.input.append("")
        self.input.append("")

        self.tape = list(string)
        # Add this in order to simulate the infinite tape
        self.tape.insert(0, "")
        self.tape.append("")
        self.tape.append("")

    def get_state(self) -> dict:
        if self.current == "qEven":
            cprint("\nCurrent state: qEven", "yellow")
            return self.states[0]
        if self.current == "qOdd":
            cprint("\nCurrent state: qOdd", "yellow")
            return self.states[1]

    def print_tape(self):
        printable_tape = self.tape
        printable_tape[self.control_position] = Color('{green}' + str(self.tape[self.control_position]) + '{/green}')
        tape_table = SingleTable([printable_tape])
        print("\n\n---------------------------------------------------------------\n\n")
        print("TURING MACHINE STATE: \n")
        print(tape_table.table)

    """
    This function recieves the char and changes the state
    """

    def read_input(self, char):
        self.print_tape()
        print(f"\nReading from control head: {char}")
        # Print tape

        self.c_state = self.get_state()  # Obtains dict form self.current
        if char == "0":
            cprint(f"\n'0' -> {self.c_state['inputs']['0']}", 'cyan')
            self.current = self.c_state['inputs']['0']
        elif char == "1":
            cprint(f"\n'1' -> {self.c_state['inputs']['1']}", 'cyan')
            self.current = self.c_state['inputs']['1']
        else:
            cprint("\nWrong input, moving to qReject", "red")
            cprint("\nqReject reached", "yellow")
            print("\n\n---------------------------------------------------------------\n\n")
            self.reject = True

    def move_tape(self):
        self.c_state = self.get_state()
        if self.c_state['move'] == "R":  # RIGHT
            self.control_position += 1
            cprint("\nMoving right...", "cyan")
        elif self.c_state['move'] == "L":  # LEFT
            self.control_position -= 1
        elif self.c_state['move'] == "H":  # HALT
            pass

    def run_tm(self):

        while not self.tape[self.control_position] == "" and self.reject is False:
            char = self.tape[self.control_position]
            self.read_input(char)
            if self.reject is True:
                break
            else:
                self.move_tape()


        if self.tape[self.control_position] == "" and self.current == "qEven":
            print("\n\n---------------------------------------------------------------\n\n")
            self.tape[self.control_position] = 1
            cprint("The number of ones is even. Appending a 1 to the end of string", "cyan")
        if self.tape[self.control_position] == "" and self.current == "qOdd":
            print("\n\n---------------------------------------------------------------\n\n")
            self.tape[self.control_position] = 0
            cprint("The number of ones is odd. Appending a 0 to the end of string", "cyan")

        if self.reject is False:
            cprint(f"\nThis is the end of input, moving to qAccept", "green")
            cprint(f"\nqAccept reached", "yellow")
            self.print_tape()
            print("\n\n---------------------------------------------------------------\n\n")