import menu

if __name__ == '__main__':
    print("Welcome to a homemade lexical analyzer!")
    print("Select an option for a lexical analyzer:\n1. Email\n2. URL\n3. IP address\n4. Secure password\n5. Exit")
    while True:
        try:
            opt = int(input("\n\nOPTION: "))
            if opt == 1:
                pass
            elif opt == 2:
                menu.call_url_matcher()
            elif opt == 3:
                pass
            elif opt == 4:
                pass
            elif opt == 5:
                print("Exiting...")
                break
            else:
                print("Wrong input. Try again.")
        except ValueError:
            print("Wrong input. Try again.")