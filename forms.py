from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired


class ReportForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    amount_donated = FloatField('Amount Donated ($)', validators=[DataRequired()])
    causes = SelectMultipleField('Causes (Use Cmd/Ctrl to select multiple fields)', choices=[
        ('Education', 'Education'),
        ('Health Care', 'Health Care'),
        ('Water Relief', 'Water Relief'),
        ('Orphan Care', 'Orphan Care')
    ], validators=[DataRequired()])
    submit = SubmitField('Generate Report')
