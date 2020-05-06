from typing import List
import json


#Pytalk getting data from mockaroo.com website in json,csv,sql etc etc
def _load_car_data():
    with open('cars.json','r') as f:
        cars=json.loads(f.read())
        return {car['id']: car for car in cars}



cars= _load_car_data()

VALID_CAR_MANUFACTURER=set([car['make']
                              for car in cars.values()])
CAR_NOT_FOUND='Car Not Found'
print(VALID_CAR_MANUFACTURER)
print(len(VALID_CAR_MANUFACTURER))
type(VALID_CAR_MANUFACTURER)

print(type(cars))