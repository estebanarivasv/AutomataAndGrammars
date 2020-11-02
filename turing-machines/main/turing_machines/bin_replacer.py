from termcolor import cprint
from terminaltables import AsciiTable
from colorclass import Color


class BinaryReplacer:
    # The turing machine must change the ones for zeroes or viceversa
    """
    q0 - Initial state
    q1 - If zero recieved, turns it to one
    q2 - If one recieved, turns it to zero
    q3 - Accepting state
    q4 - Rejecting state
    """

    input_list = None
    states = [
        {"name": "q0", "0": "q1", "1": "q2", "finish": "q3", "error": "q4"},
        {"name": "q1", "0": "q1", "1": "q2", "finish": "q3", "error": "q4"},
        {"name": "q2", "0": "q1", "1": "q2", "finish": "q3", "error": "q4"}
    ]
    control_position = 3
    tape = None
    state_index = 0

    def print_tape(self, position, situation):
        printable_tape = self.tape
        print(printable_tape)
        if situation == "R":  # RIGHT

            # Defines the tape with the current position of the control colored
            printable_tape[position] = Color('{autogreen}' + self.tape[position] + '{/green}')

            tape_table = AsciiTable([printable_tape])
            cprint("Tape state: ")
            print(tape_table.table)

        elif situation == "B":  # BAD
            # Defines the tape with the current position of the control colored
            printable_tape[position] = Color('{autored}' + self.tape[position] + '{/red}')

            tape_table = AsciiTable([printable_tape])
            cprint("Tape state: ")
            print(tape_table.table)

    def set_input(self, string):

        entered_list = list(string)

        entered_list.insert(0, "")
        entered_list.insert(0, "")
        entered_list.insert(0, "")
        entered_list.append("")
        entered_list.append("")
        entered_list.append("")

        self.input_list = list(string)
        self.tape = self.input_list

    @staticmethod
    def index_setter(next_state):
        if next_state == "q1":
            return 1
        elif next_state == "q2":
            return 2

    def write_tape(self, state, position):
        if state == "q1":
            # Defines the tape with the modified value colored
            self.tape[position] = Color('{autoyellow}' + "1" + '{/yellow}')
            tape_table = AsciiTable([self.tape])
            cprint("Tape state with the table modified: ")
            print(tape_table.table)

        elif state == "q2":
            # Defines the tape with the modified value colored
            self.tape[position] = Color('{autoyellow}' + "0" + '{/yellow}')
            tape_table = AsciiTable([self.tape])
            cprint("Tape state with the table modified: ")
            print(tape_table.table)

    def run_tm(self):

        while self.control_position <= (len(self.tape) - 3):

            # Save the binary value that is being focused by the tape control
            char = self.tape[self.control_position]

            # Print of the actual state of the tape
            self.print_tape(self.control_position, "R")

            # Set the current state by index
            current_state = self.states[self.state_index]
            cprint(f"Actual state: {current_state['name']}")

            if char == "0":
                self.state_index = self.index_setter(current_state['0'])
                print(f"Move from {current_state['name']} to {current_state['0']}")
                self.write_tape(current_state['0'], self.control_position)

            elif char == "1":
                self.state_index = self.index_setter(current_state['1'])

            else:
                self.print_tape(self.control_position, "B")
                print(f"Move from {current_state['name']} to final rejecting state {current_state['error']}.")
                break

        cprint("Accepting state q4 reached. The string is valid and correctly swapped", "green")

        input_table = AsciiTable([self.input_list])
        print("Input: \n", input_table.table)

        output_table = AsciiTable([self.tape])
        print("Output: \n", output_table.table)

if __name__ == '__main__':

    tm = BinaryReplacer()
    tm.set_input("00110100101")
    tm.run_tm()
