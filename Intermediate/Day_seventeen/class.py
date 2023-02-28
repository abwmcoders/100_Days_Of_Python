class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.user_name = user_name
        self.email = 'email@gmail.com'
        self.following = 0
        self.followers = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User( '123', 'Malik')
user_2 = User('124', 'berry')
user_1.follow(user_2)
print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)
