from typing import List
import json
from apistar import App, Route, validators, types
from apistar.http import JSONResponse
#Pytalk getting data from mockaroo.com website in json,csv,sql etc etc
def _load_car_data():
    with open('cars.json','r') as f:
        cars=json.loads(f.read())[:5]
        return {car['id']: car for car in cars}



cars= _load_car_data()

VALID_CAR_MANUFACTURER=set([car['make']
                              for car in cars.values()])
CAR_NOT_FOUND='Car Not Found'


class Car(types.Type):
    id=validators.Integer(allow_null=True)  # assign in POST
    make=validators.String(enum=list(VALID_CAR_MANUFACTURER))
    model=validators.String(max_length=50)
    year=validators.Integer(minimum=1900,maximum=2050)
    vin=validators.String(max_length=50,default='')

#API Methods


def list_cars() -> List[Car]:
      return [Car(car[1]) for car in sorted(cars.items())]

routes=[
    #Define Routes
    Route('/',method='GET',handler=list_cars),
]
app=App(routes=routes)

if __name__=="__main__":
    app.serve(host='0.0.0.0',port=9090,debug=True)