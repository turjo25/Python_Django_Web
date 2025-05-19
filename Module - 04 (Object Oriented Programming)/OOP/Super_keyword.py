class Phone:
    def __init__(self):
        print("I am in phone class")
class Samsung(Phone):
    def __init__(self):
        super().__init__() #parent class er property call hocce age
        print("I am in samsung class")

s =Samsung()
