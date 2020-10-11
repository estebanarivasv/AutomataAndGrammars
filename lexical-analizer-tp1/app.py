from termcolor import colored
import main.menu as menu

if __name__ == '__main__':
    menu.clear_screen()
    print("\n\nWelcome to a homemade lexical analyzer!")
    while True:
        print("\nSelect an option for a lexical analyzer:\n1. Email\n2. URL\n3. IP address\n4. Secure password\n5. Exit")
        try:
            opt = int(input("\n\nOPTION: "))
            if opt == 1:
                menu.clear_screen()
                print(colored(text="-------------------------------------------------------------\n"
                                   "                      EMAIL INPUT TESTER\n"
                                   "-------------------------------------------------------------\n",
                              color='cyan'))
            elif opt == 2:
                menu.clear_screen()
                print(colored(text="-------------------------------------------------------------\n"
                                   "                      URL INPUT TESTER\n"
                                   "-------------------------------------------------------------\n",
                              color='cyan'))
                menu.call_url_matcher()
            elif opt == 3:
                menu.clear_screen()
                print(colored(text="-------------------------------------------------------------\n"
                                   "                    IP ADDRESS INPUT TESTER\n"
                                   "-------------------------------------------------------------\n",
                              color='cyan'))
            elif opt == 4:
                menu.clear_screen()
                print(colored(text="-------------------------------------------------------------\n"
                                   "                 SECURE PASSWORD INPUT TESTER\n"
                                   "-------------------------------------------------------------\n",
                              color='cyan'))
            elif opt == 5:
                print("Exiting...")
                break
            else:
                print("Wrong input. Try again.")
        except ValueError:
            print("Wrong input. Try again.")
