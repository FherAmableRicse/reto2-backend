from flask_wtf import FlaskForm
from wtforms.fields import StringField,EmailField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Length

class ContactoForm(FlaskForm):
    nombre = StringField('Nombre',validators=[DataRequired()])
    email = EmailField('Email',validators=[DataRequired()])
    mensaje = TextAreaField('Mensaje',validators=[DataRequired(),Length(max=200)])
    submit = SubmitField('Enviar')
