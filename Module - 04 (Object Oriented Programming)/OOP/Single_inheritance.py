class GrandFather:
    def __init__(self,color,f_name):
        self.color = color
        self.f_name = f_name
    def show_details(self):
        print(f"{self.color},{self.f_name}")
    

class Father(GrandFather):
    def __init__(self, color, f_name, hobby):
        super().__init__(color, f_name)
        self.hobby = hobby


# gf = GrandFather("White","rahman")
f = Father("offwhite","rahman","swiming")
print(f.color)
f.show_details()

#Another example of inheritance
class Shape:
    def __init__(self,dm1,dm2):
        self.dm1 = dm1
        self.dm2 = dm2
    def area(self):
        print("I am area method of shape class")

class Triangle(Shape):
    #shape class er shb constructor er poperty ache
    def area(self):
        area = 0.5 * self.dm1 * self.dm2
        print("area of triangle:",area)

class Rectangle(Shape):
    #shape class er shb constructor er poperty ache
    def area(self):
        area = self.dm1 * self.dm2
        print("area of rectangle:",area)

tri = Triangle(5,6)
rec = Rectangle(6,7)
tri.area()
rec.area()

