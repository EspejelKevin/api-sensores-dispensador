from db import db

class SensoresModel(db.Model):
    __tablename__ = "sensores_info"

    id = db.Column(db.Integer(), primary_key=True)
    tipo = db.Column(db.String(200))
    valor = db.Column(db.Integer())
    fecha = db.Column(db.DateTime())

    def __init__(self, tipo, valor, fecha):
        self.tipo = tipo
        self.valor = valor
        self.fecha = fecha

    def json(self):
        return {
            "tipo": self.tipo,
            "valor": self.valor,
            "fecha": self.fecha.strftime("%d/%m/%y")
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
        return self.tipo

