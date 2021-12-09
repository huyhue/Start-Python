from codexplore import emailProcess, printMsg

def main():
    emails = ["tpgiahuy1@gmail.com", "tpgiahuy2@gmail.com", "tpgiahuy3@gmail.com"]
    for email in emails:
        username, domain = emailProcess(email)
        printMsg(username, domain)
        
if __name__ == "__main__":
    main()