import random

class AgriIOTElectrochemicalSensor:
    def __init__(self):
        pass

    def generateData(self, size):
        data = [random.uniform(6.5,8.5) for x in range(size)] # because percentage
        return data

