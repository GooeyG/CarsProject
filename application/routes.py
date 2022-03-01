from calendar import c
from flask import render_template, url_for, redirect, flash, request, jsonify
from application import app, db
from application.forms import Delete, EngineForm, CarForm, UpdateCar, UpdateEngine
from application.models import Engine, Car

@app.route('/')
@app.route('/index')
def index():
    engines = Engine.query.all()
    cars = Car.query.all()
    return render_template('index.html', title='Home', engines=engines, cars=cars)


@app.route("/add/engine", methods=['GET', 'POST'])
def add_engine():
    form = EngineForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_engine = Engine(
            type = request.form["type"],
            cc = request.form["cc"],
            power = request.form["power"]
            )
            db.session.add(new_engine)
            db.session.commit()
            engines = Engine.query.all()
            cars = Car.query.all()
            return render_template("index.html", new_engine=new_engine, form=form, engines=engines, cars=cars)
    return render_template('add_engine.html', title="Add a new engine", form=form)


@app.route("/add/car", methods=["GET", 'POST'])
def add_car():
    form = CarForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_car = Car(
            engine_id = request.form["engine_id"],
            make = request.form["make"],
            model = request.form["model"],
            registration = request.form["registration"]
            )
            db.session.add(new_car)
            db.session.commit()
            cars = Car.query.all()
            engines = Engine.query.all()
            return render_template("index.html", new_car=new_car, form=form, cars=cars, engines=engines)
    return render_template('add_car.html', title="Add a new car", form=form)


@app.route('/delete', methods = ['GET', 'POST'])
def delete():
    engines = Engine.query.all()
    cars = Car.query.all()
    form = Delete()
    if request.method == 'POST' and form.validate_on_submit():
        id = form.id.data
        question = form.question.data
        if question.lower() == "engine":
            engine = Engine.query.get(id)
            db.session.delete(engine)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            car = Car.query.get(id)
            db.session.delete(car)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template('delete.html', title="Deletion from database", form=form, engines=engines, cars=cars)


@app.route('/update_car/<int:id>', methods = ['GET', 'POST'])
def update_car(id):
    engines = Engine.query.all()
    cars = Car.query.all()
    form = UpdateCar()
    new = Car.query.get(id)
    if request.method == 'POST' and form.validate_on_submit():
        new.engine_id = form.engine_id.data
        new.make = form.make.data
        new.model = form.model.data
        new.registration = form.registration.data
        db.session.commit()
        return(redirect(url_for('index', title='Home', cars=cars, engines=engines)))
    return render_template('update_car.html', title='Update Car', form=form, new=new)

@app.route('/update_engine/<int:id>', methods = ['GET', 'POST'])
def update_engine(id):
    engines = Engine.query.all()
    cars = Car.query.all()
    form = UpdateEngine()
    new = Engine.query.get(id)
    if request.method == 'POST' and form.validate_on_submit():
        new.type = form.type.data
        new.cc = form.cc.data
        new.power = form.power.data
        db.session.commit()
        return(redirect(url_for('index', title='Home', cars=cars, engines=engines)))
    return render_template('update_engine.html', title='Update Engine', form=form, new=new)