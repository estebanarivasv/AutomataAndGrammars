from termcolor import colored, cprint

state_inputs = [
    # STATE A
    {"a": "B", "b": "C", "": "ACCEPT"},
    # STATE B
    {"a": "B", "b": "C", "": "ACCEPT"},
    # STATE C
    {"a": "B", "b": "C", "": "ACCEPT"},
    # REJECT STATE
    "",
    # ACCEPT STATE
    ""
]

# (a|b)*


def index_changer(next_state):
    if next_state == "B":
        return 1
    elif next_state == "C":
        return 2
    elif next_state == "REJECT":
        return 3
    elif next_state == "ACCEPT":
        return 4

if __name__ == "__main__":

    test_str = input(colored("\nENTER STRING TO TEST>>>>: ", "cyan"))

    # Conversion de cadena a lista
    char_list = list(test_str)
    char_list.append("")

    state_index = 0         
    for letter in char_list:
        state_dict = state_inputs[state_index]

        # Estado inicial A
        if state_index == 0:
            if letter != "":
                cprint(f"letra actual: {letter}", "yellow")
            if letter == "a":
                state_index = index_changer(state_dict['a'])  # state_dict['a'] devuelve el estado siguiente danda una entrada "a" (B)
                print(f"Moviendo de estado A a estado {state_dict['a']}")
                
            elif letter == "b":
                state_index = index_changer(state_dict['b'])    # state_dict['a'] devuelve el estado siguiente danda una entrada "b" (C)
                print(f"Moviendo de estado A a estado {state_dict['b']}")

            # Estado final de aceptacion
            elif letter == "":
                print(f"Moviendo de estado A a estado final de aceptacion.")
                cprint("\nCORRECT STRING.", "green")
                
             # Estado final de rechazo
            else:
                state_index = index_changer("REJECT")
                print(f"Moviendo de estado A a estado final de rechazo.")

        # Estado B
        elif state_index == 1:
            if letter != "":
                cprint(f"letra actual: {letter}", "yellow")
            if letter == "a":
                state_index = index_changer(state_dict['a'])  # state_dict['a'] devuelve el estado siguiente danda una entrada "a" (B)
                print(f"Moviendo de estado B a estado {state_dict['a']}")
                
            elif letter == "b":
                state_index = index_changer(state_dict['b'])    # state_dict['a'] devuelve el estado siguiente danda una entrada "b" (C)
                print(f"Moviendo de estado B a estado {state_dict['b']}")

            # Estado final de aceptacion
            elif letter == "":
                print(f"Moviendo de estado B a estado final de aceptacion.")
                cprint("\nCORRECT STRING.","green")

            else:
                state_index = index_changer("REJECT")
                print(f"Moviendo de estado B a estado final de rechazo")

        # Estado C
        elif state_index == 2:
            if letter != "":
                cprint(f"letra actual: {letter}", "yellow")
            if letter == "a":
                state_index = index_changer(state_dict['a'])  # state_dict['a'] devuelve el estado siguiente danda una entrada "a" (B)
                print(f"Moviendo de estado C a estado {state_dict['a']}")
                
            elif letter == "b":
                state_index = index_changer(state_dict['b'])    # state_dict['a'] devuelve el estado siguiente danda una entrada "b" (C)
                print(f"Moviendo de estado C a estado {state_dict['b']}")

            # Estado final de aceptacion
            elif letter == "":
                print(f"Moviendo de estado C a estado final de aceptacion.")
                cprint("\nCORRECT STRING.","green")

            else:
                state_index = index_changer("REJECT")
                print(f"Moviendo de estado C a estado final de rechazo")

        elif state_index == 3:  # REJECT STATE
            cprint("\nINVALID STRING.","red")
            break
