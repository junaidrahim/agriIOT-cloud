import json
import firebase_admin
from firebase_admin import credentials, db

class AgriIOTDatabase:
    def __init__(self):
        cred = credentials.Certificate("subscriber/serviceAccountKey.json")
        firebase_admin.initialize_app(cred, {
            'databaseURL' : 'https://agriiot-cloud.firebaseio.com/'
        })

    
    def write(self, data):
        result_id = db.reference("/node_mcu_data").push()
        result_id.set(json.loads(str(data)))


