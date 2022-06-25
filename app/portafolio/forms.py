from flask_wtf import FlaskForm
from wtforms.fields import StringField,EmailField,SubmitField
from wtforms.validators import DataRequired

class ContactoForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()])
    email = EmailField('Email',validators=[DataRequired()])
    mensaje = StringField('Mensaje',validators=[DataRequired()])
    submit = SubmitField('Enviar')
