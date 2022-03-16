from db import db

class DispensadorModel(db.Model):
    __tablename__ = "dispensador"

    id = db.Column(db.Integer(), primary_key=True)
    dia = db.Column(db.String(200))
    hora = db.Column(db.String(50))
    anio = db.Column(db.Integer())
    cantidad = db.Column(db.Float())

    def __init__(self, dia, hora, anio, cantidad):
        self.dia = dia
        self.hora = hora
        self.anio = anio
        self.cantidad = cantidad

    def json(self):
        return {
            "dia": self.dia,
            "hora": self.hora,
            "año": self.anio,
            "cantidad": self.cantidad
        }
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def __str__(self):
        return self.dia
