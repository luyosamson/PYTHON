class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Woof"

def make_sound(animal):
    print(animal.sound())

cat = Cat()
dog = Dog()

print(make_sound(cat)) # Output: Meow
make_sound(dog)  # Output: Woof
