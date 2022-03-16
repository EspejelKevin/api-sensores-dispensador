from flask import Flask
from flask_restful import Api
from db import db
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from src.resources.dispensador import Dispensador, DispensadorAll
from src.resources.sensores import Sensores, SensoresAll


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://fzcpptcdpeiuxh:5b0cfb537916c5e389fd1938aeec0277f1c35dcc14e20cdff7250e8be714ca17@ec2-34-194-171-47.compute-1.amazonaws.com:5432/d7fgnqa6hdktu8"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "development"
app.config['PROPAGATE_EXCEPTIONS'] = True

CORS(app, resources={r"*": {"origins": "*"}})

api = Api(app)

SQLAlchemy(app)

#with app.app_context():
#    db.create_all()


api.add_resource(Dispensador, "/api/post/dispensador", "/api/get/dispensador/<int:id>")
api.add_resource(DispensadorAll, "/api/get/dispensador/info")
api.add_resource(Sensores, "/api/post/sensor", "/api/get/sensor/<int:id>")
api.add_resource(SensoresAll, "/api/get/sensores/info")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)