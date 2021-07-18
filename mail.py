import re

regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

def email_parse(email):
    if (re.match(regex, email)):
        print("Valid Email")
        regexdomain = "@[\w.]+"
        domain = re.search(regexdomain, email).group(0)
        regexname = r'^([^@]+)@[^@]+$'
        username = re.search(regexname, email).group(1)
        email_dict = {username: domain}
        print(email_dict)

    else:
        print("ValueError: wrong email:", email)

email_parse('blahblah@gmail.com')

email_parse('someone@geekbrainsru')

