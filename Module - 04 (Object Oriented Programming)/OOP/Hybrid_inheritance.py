class Shape:
    def area(self):
        print("Claculating the area")
class Polygon(Shape):
    def sides(self):
        print("Polygon has multiple sides")
class Rectangle(Polygon):
    def __init__(self,len,breadth):
        self.len = len
        self.breadth = breadth
    def sides(self):
        print("Rectangle has 4 sides")
    def area(self): #overrides the upper area
        return self.len * self.breadth

rec = Rectangle(10,5)
rec.sides()
p = Polygon()
p.sides()
p.area()
print(rec.area())