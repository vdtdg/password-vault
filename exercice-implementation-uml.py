from abc import ABC


class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.kph = 0

    def speed(self):
        return self.kph

    def start(self):
        print(f'The vehicle {self.make} is started.')

    def klaxon(self):
        print('bip')


class Car(Vehicle):
    def __init__(self, make, model, colour):
        super().__init__(make, model)
        self.colour = colour

    def klaxon(self):
        print("The car goes bip")


class Boat(Vehicle):
    def __init__(self, make, model, length, type):
        super().__init__(make, model)
        self.length = length
        self.type = type

    def klaxon(self):
        print("The boat goes boop")


class Truck(Vehicle):
    def __init__(self, make, model, load_size_tons, length):
        super().__init__(make, model)
        self.load_size_tons = load_size_tons
        self.length = length

    def klaxon(self):
        print("The truck goes BAAAAAAAAAAAAAAAAAAAAAH")


if __name__ == '__main__':
    renault_4l = Car(make='Renault', model='4L', colour='yellow')
    print(renault_4l.speed())
    renault_4l.start()

    vovlo_fh16 = Truck(make='Volvo', model='FH16', load_size_tons=32, length=28)

    renault_4l.klaxon()
    vovlo_fh16.klaxon()

    v = Vehicle(make='2zer', model="sdfsdf")
