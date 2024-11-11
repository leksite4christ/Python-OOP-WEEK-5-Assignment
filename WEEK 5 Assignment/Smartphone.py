class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def make_call(self, number):
        print(f"Calling {number} from {self.model}...")

    def send_message(self, number, message):
        print(f"Sending message to {number}: {message}")

# Inheritance example
class Smartwatch(Smartphone):
    def __init__(self, brand, model, price, battery_life):
        super().__init__(brand, model, price)
        self.battery_life = battery_life

    def make_call(self, number):
        print(f"Calling {number} from {self.model} smartwatch...")

    def track_steps(self):
        print(f"Tracking steps with {self.model} smartwatch.")

# Creating objects
phone = Smartphone("Apple", "iPhone 13", 999)
watch = Smartwatch("Apple", "Apple Watch Series 7", 399, "18 hours")

# Using methods
phone.make_call("123-456-7890")
phone.send_message("123-456-7890", "Hello!")
watch.make_call("123-456-7890")
watch.track_steps()
