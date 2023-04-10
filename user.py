class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.is_rewards_member = False
        self.gold_card_points= 0

    def display_info(self):
        print("===========================")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Current Points: {self.gold_card_points}")
        print("==========================")
        
    def enroll(self):
        self.is_rewards_member =True
        self.gold_card_points= 200
        
    def spend_points(self, amount):
        self.gold_card_points -=  amount

my_user = User("Mike", "Orange", 40, "Orangeman@yayay.com")
my_user.display_info()
my_user.enroll()
my_user.display_info()
my_user.spend_points(50)
my_user.display_info()

user_2 = User("Cam", "Blue", 25, "CBlue1@gmil.com")
user_2.display_info()
user_2.enroll()
user_2.display_info()
user_2.spend_points(80)
user_2.display_info()




