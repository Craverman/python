import time
class TrafficLight:
    def running(self):
        self.color = "red"
        print(self.color)
        time.sleep(7)
        self.color = "yellow"
        print(self.color)
        time.sleep(2)
        self.color = "green"
        print(self.color)
        time.sleep(5)

newlight = TrafficLight()
newlight.running()


