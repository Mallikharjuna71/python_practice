class Telephone:
    def __init__(self, type, connection, number=None):
        self.type = type
        self.connection = connection
        self.number = number
        print('you called telephone class')


class Phone(Telephone):
    def __init__(self, type, connection, number, camera):
        super().__init__(type, connection, number)
        self.camera = camera
        print('you called phone class')


class SmartPhone(Phone):
    def __init__(self, type, connection, number, camera, touch):
        super().__init__(type, connection, number, camera)
        self.touch = touch
        print('you called smartphone class')



blackberry_priv = SmartPhone('wireless', 'wireless', 1234567890, '12mp',True )


class Computer:
    def __init__(self, portable=False):
        self.portable = portable

    def name(self):
        print('im computer')

class Laptop:
    def __init(self):
        self.portable = True
        self.battery = True



class ring(SmartPhone, Laptop):
    def __init__(self):
        super().__init()


