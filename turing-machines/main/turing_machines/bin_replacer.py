from colorclass import Color
from termcolor import cprint
from terminaltables import SingleTable

"""
    Syntax:     states = [Dict, Dict, ..., Dict]

    Each state will have:
    {"name": "qWrite0",
     "inputs":  {
                 "0": "qWrite0",
                 "1": "qWrite1"
                },
     "write": "0",
     "move": "R"},

"""


class TuringMachine:
    name = "Binary replacer"
    states = [
        # qWrite0 - Writes a 0
        {"name": "qWrite0",
         "inputs": {
             "0": "qWrite1",
             "1": "qWrite0"
         },
         "write": "0",
         "move": "R"},
        # qWrite1 - Writes a 1
        {"name": "qWrite1",
         "inputs": {
             "0": "qWrite1",
             "1": "qWrite0"
         },
         "write": "1",
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

        self.tape = list(string)
        # Add this in order to simulate the infinite tape
        self.tape.insert(0, "")
        self.tape.append("")

    def get_state(self) -> dict:
        if self.current == "qWrite0":
            cprint("\nCurrent state: qWrite0", "yellow")
            return self.states[0]
        if self.current == "qWrite1":
            cprint("\nCurrent state: qWrite1", "yellow")
            return self.states[1]

    def print_tape(self):
        printable_tape = self.tape
        printable_tape[self.control_position] = Color('{green}' + self.tape[self.control_position] + '{/green}')
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

    def write_tape(self):

        self.c_state = self.get_state()
        print(f"\nWriting {self.c_state['write']} instead of {self.tape[self.control_position]}")

        self.tape[self.control_position] = Color('{yellow}' + self.c_state['write'] + '{/yellow}')

    def move_tape(self):
        if self.c_state['move'] == "R":  # RIGHT
            self.control_position += 1
            cprint("\nMoving right...", "cyan")
        elif self.c_state['move'] == "L":  # LEFT
            self.control_position -= 1
        elif self.c_state['move'] == "H":  # HALT
            pass

    def run_tm(self):
        """
        1 - Estado actual recibe entrada y cambia de estado
        2 - Estado cambiado escribe en cinta
        """

        while not self.tape[self.control_position] == "" and self.reject is False:
            char = self.tape[self.control_position]
            self.read_input(char)
            if self.reject is True:
                break
            else:
                self.write_tape()
                self.move_tape()

        if self.reject is False:
            cprint(f"\nThis is the end of string, moving to qAccept", "green")
            cprint(f"\nqAccept reached", "yellow")
            self.print_tape()
            print("\n\n---------------------------------------------------------------\n\n")


if __name__ == '__main__':
    # The turing machine must change the ones for zeroes or viceversa
    tm = TuringMachine()
    tm.set_input("00110000101")
    tm.current = "qWrite0"  # Set as initial state
    tm.run_tm()
