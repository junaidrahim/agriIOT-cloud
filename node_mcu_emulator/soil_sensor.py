import numpy as np

class AgriIOTSoilSensor:
    def __init__(self):
        pass

    def generateData(self, size):
        data = np.random.random_sample(size) * 100 # because percentage
        return list(data)

