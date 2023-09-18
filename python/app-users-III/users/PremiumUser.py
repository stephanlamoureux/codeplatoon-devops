from User import Users, NewPost


class PremiumUsers(Users):
    def __init__(self, name, address, email, id):
        super().__init__(name, address, email, id)
        self.__discount_code = None

    def set_code(self, value):
        self.__discount_code = value

    def get_code(self):
        return f"{self.name}'s Promo code: {self.__discount_code}"


# Tests
if __name__ == "__main__":
    user1 = PremiumUsers("Steve", "address", "steve@email.com", 111)
    print("Premium Users Class Tests:\n")
    user1.set_code(80)
    print(user1.get_code())
    user1.add_post("hellooooo")
    print(user1.show_posts())
