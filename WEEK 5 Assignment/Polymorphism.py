class Animal:
    def move(self):
        pass

class Car:
    def move(self):
        print("Driving")

class Plane:
    def move(self):
        print("Flying")

class Bird(Animal):
    def move(self):
        print("Flying")

class Fish(Animal):
    def move(self):
        print("Swimming")

# Creating objects
car = Car()
plane = Plane()
bird = Bird()
fish = Fish()

# Using polymorphic method
for vehicle in (car, plane):
    vehicle.move()

for animal in (bird, fish):
    animal.move()
