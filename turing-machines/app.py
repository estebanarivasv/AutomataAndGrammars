from termcolor import colored
import main.menu as menu

if __name__ == '__main__':
    menu.clear_screen()
    print("\n\nHello! This is an exercise of Turing Machines")
    while True:
        print("\nSelect an option for a Turing machine:"
              "\n1. Binary replacer"
              "\n2. Binary parity tester"
              "\n3. Exit")
        try:
            opt = int(input("\n\nOPTION: "))
            if opt == 1:
                menu.clear_screen()
                print(colored(text="-------------------------------------------------------------\n"
                                   "                       BINARY REPLACER\n"
                                   "-------------------------------------------------------------\n",
                              color='cyan'))
                menu.call_bin_replacer()
            elif opt == 2:
                menu.clear_screen()
                print(colored(text="-------------------------------------------------------------\n"
                                   "                    BINARY PARITY TESTER\n"
                                   "-------------------------------------------------------------\n",
                              color='cyan'))
                menu.call_parity_tester()
            elif opt == 3:
                print("Exiting...")
                break
            else:
                print("Wrong input. Try again.")
        except ValueError:
            print("Wrong input. Try again.")
