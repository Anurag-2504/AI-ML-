'''
Q10. Letʼs create a Chat System using OOPs concepts. We have to create classes:
        user,message,chatroom
        And we have to implement functions:
        • sending messages
        • viewing chat history
        • user joining and leaving the chatroom

'''
class User:
    def __init__(self, name):
        self.name = name

    def send_message(self, chatroom, text):
        chatroom.receive_message(self, text)

    def __str__(self):
        return self.name


class Message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text

    def __str__(self):
        return f"{self.sender}: {self.text}"


class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    def join(self, user):
        self.users.append(user)
        print(f"{user} joined the chatroom '{self.name}'")

    def leave(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"{user} left the chatroom '{self.name}'")

    def receive_message(self, user, text):
        if user not in self.users:
            print(f"{user} is NOT in the chatroom. Message not sent.")
            return
        msg = Message(user, text)
        self.messages.append(msg)

    def show_history(self):
        print("\n--- Chat History ---")
        for msg in self.messages:
            print(msg)
        print("--------------------\n")




u1 = User("Anurag")
u2 = User("Abhishek")
u3 = User("Rohit")

chat = ChatRoom("Python Learners")


chat.join(u1)
chat.join(u2)

u1.send_message(chat, "Hello everyone!")
u2.send_message(chat, "Hi Anurag!")

u3.send_message(chat, "Am I allowed here?")

chat.show_history()

chat.leave(u1)

chat.show_history()
