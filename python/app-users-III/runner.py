import sys

sys.path.insert(0, "./users")
from FreeUser import FreeUsers
from PremiumUser import PremiumUsers


# create new users
user1 = FreeUsers("Steve", "123 Main St.", "steve@email.com", 444)
user2 = FreeUsers("Joe", "456 Main St.", "joe@email.com", 111)
user3 = PremiumUsers("Tom", "789 Main St.", "joe@email.com", 999)

# print basic user info
print(user1)
print(user2)
print(user3)

print("-----------------------------------")

# user 1 messages
user1.add_post("test1")
user1.add_post("test2")
user1.add_post("test3")  # should not work

# user 2 messages
user2.add_post("user 2 was here")
user2.add_post("my second message")

# user 3 messages
user3.add_post("I'm a premium user.")
user3.add_post("I can write as many messages as I want.")
user3.add_post("Here's my third pos.t")

# show user 1 posts
print(user1.show_posts())
# show user 2 posts
print(user2.show_posts())
# show user 3 posts
print(user3.show_posts())

# add discount code to user 3
user3.set_code(12)
# show user 3 discount code
print(user3.get_code())
