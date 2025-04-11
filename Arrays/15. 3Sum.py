class Microwave:

    def __init__(self,name,brand):
        self.name = name
        self.brand = brand


    def start(self):
        return "the Micro wave is starting"

    def __add__(self, other):
        return f'{self.brand} + {other.brand}'

    def __str__(self):
        return f'{self.name} is {self.brand}'




mc = Microwave("walton","abc")
bc = Microwave("samsung","zxy")

print(bc)
