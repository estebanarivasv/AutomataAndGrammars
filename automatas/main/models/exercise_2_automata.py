from termcolor import colored

from main.functions import print_status, print_actual_letter


# (aa|b)*(a|bb)*
class ExerciseTwoAutomata:
    # We define the movements for each state given certain inputs.
    input_list = []
    state_inputs = [
        {"name": "state A", "a": "B", "b": "C", "finish": "accepting state", "error": "rejecting state"},
        {"name": "state B", "a": "D", "b": "E", "finish": "accepting state", "error": "rejecting state"},
        {"name": "state C", "a": "B", "b": "F", "finish": "accepting state", "error": "rejecting state"},
        {"name": "state D", "a": "B", "b": "C", "finish": "accepting state", "error": "rejecting state"},
        {"name": "state E", "b": "G", "finish": "accepting state", "error": "rejecting state"},
        {"name": "state F", "a": "B", "b": "F", "finish": "accepting state", "error": "rejecting state"},
        {"name": "state G", "a": "H", "b": "E", "finish": "accepting state", "error": "rejecting state"},
        {"name": "state H", "a": "H", "b": "E", "finish": "accepting state", "error": "rejecting state"}
    ]
    state_index = 0
    actual = {}

    @staticmethod
    def index_changer(next_state):
        # This function defines the next state to be accessed given a certain value
        if next_state == "B":
            return 1
        elif next_state == "C":
            return 2
        elif next_state == "D":
            return 3
        elif next_state == "E":
            return 4
        elif next_state == "F":
            return 5
        elif next_state == "G":
            return 6
        elif next_state == "H":
            return 7

    def set_input(self):
        input_str = input(colored("\nEnter the string to test\n>>>  ", "cyan"))

        # String to list conversion
        self.input_list = list(input_str)

        # We add "" at the end to get to the acceptance state
        self.input_list.append("")

    def test_input(self):
        # This variable will be modified as the program runs. We begin in state A

        self.state_index = 0
        for letter in self.input_list:
            # We define the actual state
            self.actual = self.state_inputs[self.state_index]

            print_actual_letter(letter)

            if letter == "a":
                try:
                    self.state_index = self.index_changer(self.actual['a'])
                    # index_changer sets the following state given an input "a" defined in dict "state"
                    print_status(self.actual['name'], self.actual['a'])
                    # Given an input "b", the program stops and enters to the next state
                except KeyError:
                    # The state E does not recieve an input "a"
                    print_status(self.actual['name'], self.actual['error'])
                    break
                    # Given an input different that the admitted characters, it will raise an error.
                    # The program stops and enters to the rejecting state

            elif letter == "b":
                try:
                    self.state_index = self.index_changer(self.actual['b'])

                    print_status(self.actual['name'], self.actual['b'])
                    # Given an input "b", the program stops and enters to the next state
                except KeyError:
                    print_status(self.actual['name'], self.actual['error'])
                    break
                    # Given an input different that the admitted characters, it will raise an error.
                    # The program stops and enters to the rejecting state

            elif letter == "":
                print_status(self.actual['name'], self.actual['finish'])
                break
                # Given an input "", the program stops and enters to the accepting state

            else:
                print_status(self.actual['name'], self.actual['error'])
                break
                # Given an input different that the admitted characters, it will raise an error.
                # The program stops and enters to the rejecting state


if __name__ == '__main__':
    automata = ExerciseTwoAutomata()
    automata.set_input()
    automata.test_input()
