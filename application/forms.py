from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired, ValidationError, AnyOf


class EngineForm(FlaskForm):
    style = StringField("style", validators=[DataRequired()])
    cc = IntegerField("cc", validators=[DataRequired()])
    power = IntegerField("BHP", validators=[DataRequired()])
    submit = SubmitField('Submit')


class CarForm(FlaskForm):
    engine_id = StringField("Engine ID", validators=[DataRequired()])
    make = StringField("Make", validators=[DataRequired()])
    model = StringField("Model", validators=[DataRequired()])
    registration = StringField("Registration", validators=[DataRequired()])
    submit = SubmitField('Submit')

class UpdateEngine(FlaskForm):
    style = StringField("style", validators=[DataRequired()])
    cc = IntegerField("cc", validators=[DataRequired()])
    power = IntegerField("BHP", validators=[DataRequired()])
    submit = SubmitField('Submit')

class UpdateCar(FlaskForm):
    engine_id = StringField("Engine ID", validators=[DataRequired()])
    make = StringField("Make", validators=[DataRequired()])
    model = StringField("Model", validators=[DataRequired()])
    registration = StringField("Registration", validators=[DataRequired()])
    submit = SubmitField('Submit')

class Delete(FlaskForm):
    id = IntegerField("Provide ID for the item you want to remove", validators=[DataRequired()])
    question = StringField("Delete from Engine or Cars?", validators=[DataRequired(), AnyOf("Engine, engine, car, cars, Car, Cars", message="Please enter either Engine or Car", values_formatter=None)])
    submit = SubmitField("Delete")
