class Users:
    def __init__(self, name, address, email, id):
        self.name = name
        self.address = address
        self.email = email
        self.id = id
        self.messages = []

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Address: {self.address}, ID: {self.id}"

    def add_post(self, message):
        new_post = NewPost(self.name, message)
        self.message = message
        self.messages.append(message)
        return new_post

    def show_posts(self):
        if len(self.messages) > 0:
            return f"{self.name}'s messages: {self.messages}"
        else:
            return "User has no messages."


class NewPost:
    def __init__(self, name, message):
        self.name = name
        self.message = message


# Tests
if __name__ == "__main__":
    user1 = Users("Steve", "address", "steve@email.com", 111)
    print("Users Class Tests:\n")
    print(user1)
    user1.add_post("User 1 Posted this.")
    print(user1.show_posts())
