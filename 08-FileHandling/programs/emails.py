import re
def email_sender(filename):
    pattern="From:.*<(\w+\.?\w+@\w+.com)"
    with open(filename,"r") as file:
        email=file.read()
    sender = re.findall(pattern, email)
    return sender
def email_recipent(filename):
    pattern="To:.*<(\w+\.?\w+@\w+.com)"
    with open(filename,"r") as file:
        email=file.read()
    recipent = re.findall(pattern, email)
    return recipent
def email_subject(filename):
    pattern="Subject:\s?(.*)"
    with open(filename,"r") as file:
        email=file.read()
    subject = re.findall(pattern, email)
    return subject
def email_body(filename):
    pattern=".*"#"(^((?!:|Postfix).)*$)"
    with open(filename,"r") as file:
        email=file.read()
    body = re.findall(pattern, email)
    return body

if __name__=="__main__":
    nameoffile="08-FileHandling/email.txt"
    print(email_sender(nameoffile))
    print(email_recipent(nameoffile))
    print(email_subject(nameoffile))
    print(email_body(nameoffile))
    