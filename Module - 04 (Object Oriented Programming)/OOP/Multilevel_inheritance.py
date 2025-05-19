class GrandFather:
    def __init__(self,color,f_name):
        self.color = color
        self.f_name = f_name

class Father(GrandFather):
    def __init__(self, color, f_name, hobby):
        super().__init__(color, f_name) #father class calling grandfather class
        self.hobby = hobby

class Children(Father,GrandFather):
    def __init__(self, color, f_name, hobby, fashion):
        super().__init__(color, f_name, hobby) #calling father class
        self.fashion = fashion
    def info(self):
        print(f"{self.color},{self.f_name},{self.fashion},{self.hobby}")

c1 = Children(color="white",f_name="rahman",fashion="styleish",hobby="singing")
c1.info()