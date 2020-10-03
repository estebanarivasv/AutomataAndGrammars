from matchers import EmailMatcher


def call_email_matcher():
    string = input("Insert string: ")
    matcher = EmailMatcher(string)
    match = matcher.get_match()
    if match:
        pass
    else:
        print("No se encontro")