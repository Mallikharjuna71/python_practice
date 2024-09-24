class Rocket:
    count = 0
    def __init__(self,name=None, speed=None, fuel_capacity=None, engines=None, satellites=None):
        self.speed = speed
        self.fuel_capacity = fuel_capacity
        self.engines = engines
        self.satellites = satellites
        self.name = name
        Rocket.count += 1

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

rocket1 = Rocket('PSLV', 300, 4000, 3, 15)
rocket2 = Rocket()
rocket3 = Rocket()
print(Rocket.count)


