
from time import sleep


class TrafficLight:
    __color = ["Red", "Yellow", "Green"]

    def running(self):
        c = 0
        while True:
            if c == 0:
                print(f"Light \n" f"{TrafficLight.__color[c]}-Stop!")
                sleep(7)
            elif c == 1:
                print(f"Light \n" f"{TrafficLight.__color[c]}-Wait!")
                sleep(3)
            elif c == 2:
                print(f"Light \n" f"{TrafficLight.__color[c]}-Go!")
                sleep(3)
            c += 1
    pass


TrafficLight = TrafficLight()
TrafficLight.running()
