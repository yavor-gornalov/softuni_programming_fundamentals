# https://judge.softuni.org/Contests/Practice/Index/1733#2

class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
while True:
    command = input()
    if command == "Stop":
        break
    command_args = command.split()
    sender = command_args[0]
    receiver = command_args[1]
    content = command_args[2]
    emails.append(Email(sender, receiver, content))

emails_tobe_sent = [int(x) for x in input().split(', ')]

for idx, email in enumerate(emails):
    if idx in emails_tobe_sent:
        email.send()
    print(email.get_info())
