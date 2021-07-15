class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"Car {self.name} is going"

    def stop(self):
        return f"Car {self.name}  stopped"

    def turn_right(self):
        return f"Car {self.name} turned right"

    def turn_left(self):
        return f"Car {self.name} turned left"

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f"Speeding {self.speed}, slow down the speed"
        else:
            return f"Current speed {self.name} is {self.speed}"



class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f"Speeding {self.speed}, slow down the speed"
        else:
            return f"Current speed {self.name} is {self.speed}"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f"{self.name} police car"
        else:
            return f"{self.name} is not police car"


opel = TownCar(80, 'Black', 'Opel', False)
lamborghini = SportCar(120, 'Purple', 'Lamborghini', False)
VAZ = WorkCar(50, 'White', 'VAZ', False)
toyota = PoliceCar(110, 'Blue', 'Toyota', True)
print(f" {opel.go()} and {opel.turn_left()}.{opel.show_speed()} and {opel.stop()}")
print(f" {lamborghini.go()} and {lamborghini.turn_right()}.{lamborghini.show_speed()} and {lamborghini.stop()}")
print(f" {VAZ.go()} .{VAZ.show_speed()} and {VAZ.stop()}")
