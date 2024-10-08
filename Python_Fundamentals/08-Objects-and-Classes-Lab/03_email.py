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


info = input()
emails = []                  #----------------------->лист, в който ще пазя целите обекти(sender, receiver, content)


while info != "Stop":
    sender, receiver, content = info.split()    #присвоявам на всеки един стойност, разделена с интервал
    email_info = Email(sender, receiver, content)   #създавам обект, който ще го презаписвам при всяка итерация
    emails.append(email_info)                       #добавям обекта в листа
    info = input()

indexes = [int(index) for index in input().split(", ")] #с list comprehension си правя индексите в лист, за да ги достъпя

for index in indexes:
    emails[index].send()    #за имейла под съответния индекс, викам метода(функцията) който ни е нужен по условие

for current_email in emails:
    print(current_email.get_info()) #за всеки имейл в листа, викам метода(функцията) който ни е нужен по условие