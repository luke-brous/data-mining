class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return "Woof!"
    
    def __str__(self):
        return f"{self.name}, {self.age} years old, {self.weight} pds"
    
if __name__ == "__main__":
    dog = Dog("Buddy", 3, 50)
    print(dog)
    print(dog.bark())


        