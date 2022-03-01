from sqlalchemy import ForeignKey
from application import db
        
class Engine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(30), unique=True)
    cc = db.Column(db.Integer(), nullable=False)
    power = db.Column(db.Integer(), nullable=False)
    cars = db.relationship("Car", back_populates="Engine")



class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    engine_id = db.Column(db.Integer, ForeignKey('engine.id'))
    make = db.Column(db.String(30), unique=False)
    model = db.Column(db.String(30), nullable=False)
    registration = db.Column(db.String(30), nullable=False)
    Engine = db.relationship("Engine", back_populates="cars")
    
db.create_all()
