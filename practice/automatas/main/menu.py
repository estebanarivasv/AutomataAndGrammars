import os
from terminaltables import SingleTable

from main.models import ExerciseOneAutomata, ExerciseTwoAutomata



def clear_screen():
    if os.name == "posix":
        os.system('clear')
    else:
        os.system('cls')


def call_automata_1():
    table_data = [["State", "Input 'a'", "Input 'b'"],
                  ["A", "B", "C"],
                  ["B", "B", "C"],
                  ["C", "B", "C"]]
    table = SingleTable(table_data)
    print("First, we've developed how the automata work into this resulting table:\n\n")
    print(table.table)
    automata = ExerciseOneAutomata()
    automata.set_input()
    automata.test_input()


def call_automata_2():
    table_data = [["State", "Input 'a'", "Input 'b'"],
                  ["A", "B", "C"],
                  ["B", "D", "E"],
                  ["C", "B", "F"],
                  ["D", "B", "C"],
                  ["E", "-", "G"],
                  ["F", "B", "F"],
                  ["G", "H", "E"],
                  ["H", "H", "E"]
                  ]
    table = SingleTable(table_data)
    print("First, we've developed how the automata work into this resulting table:\n\n")
    print(table.table)
    automata = ExerciseTwoAutomata()
    automata.set_input()
    automata.test_input()
