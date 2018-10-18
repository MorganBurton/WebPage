from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

from wtforms.validators import DataRequired, Length


class PCform(FlaskForm):
	postcode = StringField('Postcode', 
							validators=[DataRequired(), Length(min=6, max=7)])

	enter = SubmitField('Enter')

