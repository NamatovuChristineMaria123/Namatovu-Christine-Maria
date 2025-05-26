class Animal:
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def makeSound(self):
        print("Dogs bark")


# Create an object of Dog and call the method
dogObj = Dog()
dogObj.makeSound()
dogObj.sound()
