# Polymorphism with inheritance
class Bird:
    def fly(self):
        print("Birds fly in the sky")


class Eagle(Bird):
    def fly(self):
        print("Eagle flies at a higher altitude")


class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies at a lower altitude")


def fly_test(bird):
    bird.fly()


eagle1 = Eagle()
sparrow1 = Sparrow()

fly_test(eagle1)
fly_test(sparrow1)
