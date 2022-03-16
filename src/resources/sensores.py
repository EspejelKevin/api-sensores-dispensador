from flask_restful import Resource, reqparse
from src.models.sensores import SensoresModel
import datetime


class Sensores(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('tipo',
                        type=str,
                        required=True,
                        help="Nombre del dispositivo IoT"
                        )
    parser.add_argument('valor',
                        type=int,
                        required=True,
                        help="Valor que emite el dispositivo"
                        )
    
    def get(self, id):
        sensor = SensoresModel.find_by_id(id)
        if sensor:
            return sensor.json()
        return {"message": "Resource not found"}, 404
    
    def post(self):
        data = Sensores.parser.parse_args()

        device = SensoresModel(tipo=data["tipo"], valor=data["valor"], fecha=datetime.date.today())

        try:
            device.save_to_db()
            return device.json(), 201
        except:
            return {"message": "An error ocurred inserting the device"}, 500


class SensoresAll(Resource):
    def get(self):
        return {"Info sensores": list(map(lambda x:x.json(), SensoresModel.query.all()))}
