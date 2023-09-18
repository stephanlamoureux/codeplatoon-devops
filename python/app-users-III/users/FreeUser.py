from User import Users, NewPost


class FreeUsers(Users):
    def __init__(self, name, address, email, id):
        super().__init__(name, address, email, id)
        self.free_messages = []
        self.posts = 0

    def add_post(self, message):
        self.message = message

        if self.posts < 2:
            new_post = NewPost(self.name, message)
            self.message = message
            self.messages.append(message)
            self.posts += 1
            return new_post
        else:
            return f"Unable to add a new message, {self.name} has reached their two post limit."


# Tests
if __name__ == "__main__":
    user1 = FreeUsers("Steve", "123 Main St.", "steve@email.com", 999)
    print("FreeUsers Class Tests:\n")
    user1.add_post("This is a post from a Free User's account.")
    user1.add_post("I can only add 2 messages :(")
    print(user1.show_posts())
