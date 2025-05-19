class Singleton:
    _instance = None #class variable
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
ob1 = Singleton()
ob2 = Singleton()
print(ob1 is ob2)