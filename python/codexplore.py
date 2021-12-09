# print(f"Sub_module 's name {__name__}")

def emailProcess(email):
    # tpgiahuy@gmail.com
    email_username = email[0:email.index("@")]
    email_domain = email[email.index("@")+1:]
    return [email_username, email_domain]

def printMsg(email_username, email_domain):
    print(f"username: {email_username}; Domain: {email_domain}")

def main():
    email = input("Please enter your email address: ").strip()
    email_username, email_domain = emailProcess(email)
    printMsg(email_username, email_domain)

if __name__ == "__main__":
    main()