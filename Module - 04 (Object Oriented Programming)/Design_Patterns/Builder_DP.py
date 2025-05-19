#step by step build kora
class Computer:
    def __init__(self,cpu,ram,storage):
        self.cpu = cpu
        self.ram = ram
        self.storage =storage
    def __str__(self):
        return f"Computer build with:{self.cpu} Processor,{self.ram} RAM,{self.storage} Storage"
        
class ComputerBuilder:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
    def set_cpu(self,cpu):
        self.cpu = cpu
        return self
    def set_ram(self,ram):
        self.ram = ram
        return self
    def set_storage(self,st):
        self.storage = st
        return self
    def build(self):
        return Computer(self.cpu,self.ram,self.storage)

builder= ComputerBuilder()
computer = builder.set_cpu("Ryzen 7535HS").set_ram("16GB").set_storage("500GB").build()
print(computer)