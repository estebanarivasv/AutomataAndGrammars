from menu import call_email_matcher

if __name__ == '__main__':
    print("Welcome to a homemade lexical analyzer!")
    opt = int(input("Select an option for a lexical analyzer:\n1. Email\n2. URL\n3.IP address\n4.Secure password\n\nOPTION: "))
    if opt == 1:
        call_email_matcher()
    if opt == 2:
        pass
    if opt == 3:
        pass
    if opt == 4:
        pass