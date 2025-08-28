class BMW:
    def __init__(self, model, color):
        self.model = model
        self.color = color
    def car_info(self):
        return f"BMW Model: {self.model}, Color: {self.color}"
    def top_speed(self):
        return "BMW top speed: 250 km/h"
    def fuel_type(self):
        return "BMW runs on Petrol"
class Ferrari:
    def __init__(self, model, color):
        self.model = model
        self.color = color
    def car_info(self):
        return f"Ferrari Model: {self.model}, Color: {self.color}"
    def top_speed(self):
        return "Ferrari top speed: 330 km/h"
    def fuel_type(self):
        return "Ferrari runs on Petrol"
def show_car_details(car):
    print(car.car_info())
    print(car.top_speed())
    print(car.fuel_type())
    print("-" * 40)
bmw_car = BMW("X5", "Black")
ferrari_car = Ferrari("488 GTB", "Red")
for car in (bmw_car, ferrari_car):
    show_car_details(car)