from wtforms import TextAreaField, SubmitField, SelectField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
import utils


language_choice =[]
for key, value in utils.languages.items(): 
    language_choice.append((key,value))

class MyForm(FlaskForm):
    text_field = TextAreaField("Data", validators=[DataRequired()])
    language_field = SelectField("Language to Translate to", choices=[("En" , "English"), ("Ar", "Arabic")] )
    submit = SubmitField("Translate")
     