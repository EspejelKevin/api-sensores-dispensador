from flask_restful import Resource, reqparse
from src.models.dispensador import DispensadorModel


class Dispensador(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('dia',
                        type=str,
                        required=True,
                        help="Día que se alimentó"
                        )
    parser.add_argument('hora',
                        type=str,
                        required=True,
                        help="La hora se maneja con p.m o a.m"
                        )
    parser.add_argument('año',
                        type=int,
                        required=True,
                        help="Año en que se esta alimentando"
                        )
    parser.add_argument('cantidad',
                        type=float,
                        required=True,
                        help="Cantidad en gramos"
                        )
    
    async def get(self, id):
        sensor = await DispensadorModel.find_by_id(id)
        if sensor:
            return sensor.json()
        return {"message": "Resource not found"}, 404
    
    async def post(self):
        data = Dispensador.parser.parse_args()
        
        device = DispensadorModel(dia=data["dia"], hora=data["hora"], anio=data["año"], cantidad=data["cantidad"])

        try:
            await device.save_to_db()
            return device.json(), 201
        except:
            return {"message": "An error ocurred inserting the device"}, 500


class DispensadorAll(Resource):
    async def get(self):
        return {"Info dispensador": await list(map(lambda x:x.json(), DispensadorModel.query.all()))}
