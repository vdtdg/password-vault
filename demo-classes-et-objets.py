class Engine:
    def __init__(self, displacement_cc: int, cylinder: int):
        self.displacement_cc = displacement_cc
        self.cylinder = cylinder
        self.started = False

    def start(self):
        self.started = True

    def accelerate(self):
        print(f'The engine is pushing more fuel into its {self.cylinder} cylinders, accelerating !')


class Brake:
    def brake(self):
        print("Braking !")


class Car:
    def __init__(self, engine: Engine, make: str, model: str):
        self.engine = engine
        self.make = make
        self.model = model
        self.speed = 0
        self.brake = Brake()

    def raise_speed_to(self, target_kph):
        while self.speed < target_kph:
            self.engine.accelerate()
            self.speed += 1

    def lower_speed_to(self, target_kph):
        while self.speed > target_kph:
            self.brake.brake()
            self.speed -= 1


if __name__ == '__main__':
    v8_4l = Engine(displacement_cc=4000, cylinder=8)
    car = Car(engine=v8_4l, make="Aston Martin", model="Vantage")
    print(car.speed)
    car.raise_speed_to(5)
    print(car.speed)
