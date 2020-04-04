import random

class AgriIOTTempHumiditySensor:
    def __init__(self):
        pass

    def generateData(self, size):
        # (temperature, humidity)
        data = [(random.uniform(28, 34), random.uniform(19,21)) for x in range(size)]
        return data