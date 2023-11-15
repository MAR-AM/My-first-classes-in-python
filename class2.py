class Car () :
    def __init__(self, speed, color, nitrospeed, model):
        self.speed = speed
        self.color = color
        self.nitrospeed = nitrospeed
        self.model = model

    def turn(self, direction):
        print(f"The car turns {direction}.")

    def accelerate(self):
        print("The car accelerates.")

    def brake(self):
        print("The car brakes.")

    def boost(self):
        print(f"The car boosts with nitro speed of {self.nitrospeed}.")

    def display_info(self):
        print(f"Speed: {self.speed} km/h")
        print(f"Color: {self.color}")
        print(f"Nitro Speed: {self.nitrospeed}")
        print(f"Model: {self.model}")

# Example of using the Car class
car1 = Car(speed=120, color="Blue", nitrospeed=30, model="SportsCar")
car2 = Car(speed=90, color="Red", nitrospeed=25, model="Sedan")
car3 = Car(speed=180, color="Black", nitrospeed=40, model="BMW")

# Calling methods
car1.turn("right")
car2.accelerate()
car1.brake()
car2.boost()

# Show car information
print("\nCar 1:")
car1.display_info()

print("\nCar 2:")
car2.display_info()

print("\nCar 3:")
car3.display_info()
