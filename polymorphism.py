class Syian:
    def __init__(self):
        pass

    def greet(self):
        print('hi i am a syian')

class SuperSyian(Syian):
    def __init__(self):
        pass
    def greet(self):
        print('i am a super syian')


krillin = Syian()
goku = SuperSyian()

krillin.greet()
goku.greet()


