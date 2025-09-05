# Class Inheritance

class Animal:
    def __init__(self):
        self.num_eyes = 2
    
    def breath():
        print("Inhale, Exhale")
    
class Fish(Animal):

    def __init__(self):
        super().__init__()

    def swim(self):
        print("Moving in water")

nemo = Fish()
nemo.swim()
