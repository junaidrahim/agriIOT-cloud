import random

class AgriIOTAcousticSensor:
    def __init__(self):
        pass

    def generateData(self, size):
        data = [random.uniform(0.25, 0.8) for x in range(size)]
        return data
    