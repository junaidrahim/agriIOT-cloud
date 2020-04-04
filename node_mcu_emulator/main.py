from soil_sensor import AgriIOTSoilSensor
from acoustic_sensor import AgriIOTAcousticSensor
from temp_humidity_sensor import AgriIOTTempHumiditySensor
from electrochemical_sensor import AgriIOTElectrochemicalSensor

from datetime import datetime
from time import sleep
import requests

soil_sensor = AgriIOTSoilSensor()
acoustic_sensor = AgriIOTAcousticSensor()
temp_humidity_sensor = AgriIOTTempHumiditySensor()
electrochemical_sensor = AgriIOTElectrochemicalSensor()

m = 1000

soil_data = soil_sensor.generateData(m)
acoustic_data = acoustic_sensor.generateData(m)
temp_humidity_data = temp_humidity_sensor.generateData(m)
electrochemical_data = electrochemical_sensor.generateData(m)

def send_request(soil, temp, acoustic, electrochem):
    timestamp = str(datetime.now())

    payload = {
        "timestamp":timestamp,
        "soil_moisture":str(soil),
        "temperature_humidity":str(temp),
        "acoustic":str(acoustic),
        "electrochemical": str(electrochem)
    }

    a = requests.post('http://localhost:3000/api/data', json=payload)
    print(a.text)

for i in range(10, m):
    send_request(soil_data[i], temp_humidity_data[i], acoustic_data[i], electrochemical_data[i])
    sleep(0.1)

