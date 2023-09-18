class Users:
    messages = []

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}"

    def post(self, message):
        self.message = message
        Users.messages.append(message)


# Create new instances of users
user1 = Users("Steve", "123 Main St.", "steve@email.com")
user2 = Users("Avery", "456 Hope St.", "avery@email.com")
user3 = Users("Tom Brady", "6 Title Town Dr.", "goat@email.com")

# Update user message
user1.post("hey!")
user2.post("I love Python")
user3.post("7 rings 💍")
# Print all user messages and formatted
users = [user1, user2, user3]
for user in users:
    print(f"{user.name} says: {user.message}")

# Variable created of all user messages
print(Users.messages)
