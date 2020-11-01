from termcolor import colored
import main.menu as menu

if __name__ == '__main__':
    menu.clear_screen()
    print("\n\nHello! In this practical example, we work with automatas.")
    while True:
        print("\n\nSelect an option to test an example of finite state automatas:"
              "\n1. Automata (a|b)*"
              "\n2. Automata (aa|b)*(a|bb)*"
              "\n3. Exit")
        try:
            opt = int(input("\n\nOPTION: "))
            if opt == 1:
                menu.clear_screen()
                print(colored(text="-------------------------------------------------------------\n"
                                   "                       AUTOMATA (a|b)*\n"
                                   "-------------------------------------------------------------\n",
                              color='cyan'))
                menu.call_automata_1()
            elif opt == 2:
                menu.clear_screen()
                print(colored(text="-------------------------------------------------------------\n"
                                   "                    AUTOMATA (aa|b)*(a|bb)*\n"
                                   "-------------------------------------------------------------\n",
                              color='cyan'))
                menu.call_automata_2()
            elif opt == 3:
                print("Exiting...")
                break
            else:
                print("Wrong input. Try again.")
        except ValueError:
            print("Wrong input. Try again.")
