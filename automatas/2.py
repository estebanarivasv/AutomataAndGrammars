from termcolor import colored, cprint

state_inputs = [
    # STATE A
    {"a": "B", "b": "C", "": "ACCEPT"},
    # STATE B
    {"a": "D", "b": "E", "": "ACCEPT"},
    # STATE C
    {"a": "B", "b": "F", "": "ACCEPT"},
    # STATE D
    {"a": "B", "b": "C", "": "ACCEPT"},
    # STATE E
    {"b": "G", "": "ACCEPT"},
    # STATE F
    {"a": "B", "b": "F", "": "ACCEPT"},
    # STATE G
    {"a": "H", "b": "E", "": "ACCEPT"},
    # STATE H
    {"a": "H", "b": "E", "": "ACCEPT"},
    # REJECT STATE
    "",
    # ACCEPT STATE
    ""
]

# (aa|b)*(a|bb)*

def print_act_letter(letter, state_index):
    if letter != "":
        cprint(f"Actual Letter: {letter}, state: {state_index}", "yellow")
    


def index_changer(next_state):
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
    elif next_state == "REJECT":
        return 8

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
            
            print_act_letter(letter, state_index)
                
            if letter == "a":
                state_index = index_changer(state_dict['a'])  # state_dict['a'] devuelve el estado siguiente danda una entrada "a" (B)
                print(f"Moving from state A a estado {state_dict['a']}")
                
            elif letter == "b":
                state_index = index_changer(state_dict['b'])    # state_dict['a'] devuelve el estado siguiente danda una entrada "b" (C)
                print(f"Moving from state A a estado {state_dict['b']}")

            # Estado final de aceptacion
            elif letter == "":
                print(f"Moving from state A a estado final de aceptacion.")
                cprint("\nCORRECT STRING.", "green")
                
             # Estado final de rechazo
            else:
                state_index = index_changer("REJECT")
                print(f"Moviendo de estado A a estado final de rechazo.")

        # Estado B
        elif state_index == 1:

            print_act_letter(letter, state_index)          
                
            if letter == "a":
                state_index = index_changer(state_dict['a'])  # state_dict['a'] devuelve el estado siguiente danda una entrada "a" (B)
                print(f"Moving from state B a estado {state_dict['a']}")
                
            elif letter == "b":
                state_index = index_changer(state_dict['b'])    # state_dict['a'] devuelve el estado siguiente danda una entrada "b" (C)
                print(f"Moving from state B a estado {state_dict['b']}")

            # Estado final de aceptacion
            elif letter == "":
                print(f"Moving from state B a estado final de aceptacion.")
                cprint("\nCORRECT STRING.","green")

            else:
                state_index = index_changer("REJECT")
                print(f"Moving from state B a estado final de rechazo")

        # Estado C
        elif state_index == 2:
            
            print_act_letter(letter, state_index)

            if letter == "a":
                state_index = index_changer(state_dict['a'])  # state_dict['a'] devuelve el estado siguiente danda una entrada "a" (B)
                print(f"Moving from state C a estado {state_dict['a']}")
                
            elif letter == "b":
                state_index = index_changer(state_dict['b'])    # state_dict['a'] devuelve el estado siguiente danda una entrada "b" (C)
                print(f"Moving from state C a estado {state_dict['b']}")

            # Estado final de aceptacion
            elif letter == "":
                print(f"Moving from state C a estado final de aceptacion.")
                cprint("\nCORRECT STRING.","green")

            else:
                state_index = index_changer("REJECT")
                print(f"Moving from state C a estado final de rechazo")
        # Estado D
        elif state_index == 3:
            
            print_act_letter(letter, state_index)

            if letter == "a":
                state_index = index_changer(state_dict['a'])  # state_dict['a'] devuelve el estado siguiente danda una entrada "a" (B)
                print(f"Moving from state D a estado {state_dict['a']}")
                
            elif letter == "b":
                state_index = index_changer(state_dict['b'])    # state_dict['a'] devuelve el estado siguiente danda una entrada "b" (C)
                print(f"Moving from state D a estado {state_dict['b']}")

            # Estado final de aceptacion
            elif letter == "":
                print(f"Moviendo de estado D a estado final de aceptacion.")
                cprint("\nCORRECT STRING.","green")

            else:
                state_index = index_changer("REJECT")
                print(f"Moviendo de estado D a estado final de rechazo")
        # Estado E
        elif state_index == 4:
            
            print_act_letter(letter, state_index)
                
            if letter == "b":
                state_index = index_changer(state_dict['b'])    # state_dict['a'] devuelve el estado siguiente danda una entrada "b" (C)
                print(f"Moviendo de estado E a estado {state_dict['b']}")

            # Estado final de aceptacion
            elif letter == "":
                print(f"Moviendo de estado E a estado final de aceptacion.")
                cprint("\nCORRECT STRING.","green")

            else:
                state_index = index_changer("REJECT")
                print(f"Moviendo de estado E a estado final de rechazo")
        # Estado F
        elif state_index == 5:
            
            print_act_letter(letter, state_index)

            if letter == "a":
                state_index = index_changer(state_dict['a'])  # state_dict['a'] devuelve el estado siguiente danda una entrada "a" (B)
                print(f"Moviendo de estado F a estado {state_dict['a']}")
                
            elif letter == "b":
                state_index = index_changer(state_dict['b'])    # state_dict['a'] devuelve el estado siguiente danda una entrada "b" (C)
                print(f"Moviendo de estado F a estado {state_dict['b']}")

            # Estado final de aceptacion
            elif letter == "":
                print(f"Moviendo de estado F a estado final de aceptacion.")
                cprint("\nCORRECT STRING.","green")

            else:
                state_index = index_changer("REJECT")
                print(f"Moviendo de estado F a estado final de rechazo")
        # Estado G
        elif state_index == 6:
            
            print_act_letter(letter, state_index)

            if letter == "a":
                state_index = index_changer(state_dict['a'])  # state_dict['a'] devuelve el estado siguiente danda una entrada "a" (B)
                print(f"Moviendo de estado G a estado {state_dict['a']}")
                
            elif letter == "b":
                state_index = index_changer(state_dict['b'])    # state_dict['a'] devuelve el estado siguiente danda una entrada "b" (C)
                print(f"Moviendo de estado G a estado {state_dict['b']}")

            # Estado final de aceptacion
            elif letter == "":
                print(f"Moviendo de estado G a estado final de aceptacion.")
                cprint("\nCORRECT STRING.","green")

            else:
                state_index = index_changer("REJECT")
                print(f"Moviendo de estado G a estado final de rechazo")
        # Estado H
        elif state_index == 7:
            
            print_act_letter(letter, state_index)

            if letter == "a":
                state_index = index_changer(state_dict['a'])  # state_dict['a'] devuelve el estado siguiente danda una entrada "a" (B)
                print(f"Moviendo de estado H a estado {state_dict['a']}")
                
            elif letter == "b":
                state_index = index_changer(state_dict['b'])    # state_dict['a'] devuelve el estado siguiente danda una entrada "b" (C)
                print(f"Moviendo de estado H a estado {state_dict['b']}")

            # Estado final de aceptacion
            elif letter == "":
                print(f"Moviendo de estado H a estado final de aceptacion.")
                cprint("\nCORRECT STRING.","green")

            else:
                state_index = index_changer("REJECT")
                print(f"Moviendo de estado H a estado final de rechazo")

        # Estado REJECT
        elif state_index == 8:  # REJECT STATE
            cprint("\nINVALID STRING.","red")
            break
