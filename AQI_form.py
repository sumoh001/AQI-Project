from flask_wtf import FlaskForm
from wtforms import DateField, StringField, SubmitField

class AQIForm(FlaskForm):
    PredictionDate = DateField("Enter Prediction Date")
    PredictionCity = StringField("Enter Prediction City")

    submit = SubmitField("Predict")
