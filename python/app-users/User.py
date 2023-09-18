class Users:
    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}"


user1 = Users("Steve", "123 Main St.", "steve@email.com")
user2 = Users("Avery", "456 Hope St.", "avery@email.com")
user3 = Users("Tom", "6 Title Town Dr.", "tom@email.com")

print(user1)
print(user1.name)
print(user2.address)
print(user3.email)

users = [user1, user2, user3]
for user in users:
    print(user)
