from application import db
        
class Engine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(30), unique=False)
    cc = db.Column(db.Integer(), nullable=False)
    power = db.Column(db.Integer(), nullable=False)



class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(30), unique=False)
    model = db.Column(db.String(30), nullable=False)
    registration = db.Column(db.String(30), nullable=False)
    #engine = db.Column(db.Integer, db.ForeignKey("engine.id"), nullable=False)



db.create_all()