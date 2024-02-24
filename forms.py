from wtforms import Form
from wtforms import StringField, SelectField, RadioField, EmailField, IntegerField
#esta clase sirve para las validaciones 
from wtforms import validators

class UserForm(Form):
    nombre = StringField('nombre',[
        validators.DataRequired(message = 'El campo es requerido'),
        validators.length(min=4, max=10, message='Ingresa nombre valido')
    ])
    apaterno = StringField('apaterno',[
        validators.DataRequired(message = 'El campo es requerido'),
        validators.length(min=4, max=10, message='Ingresa apellido paterno valido')
    ])
    amaterno = StringField('amaterno',[
        validators.DataRequired(message = 'El campo es requerido'),
        validators.length(min=4, max=10, message='Ingresa apellido materno valido')
    ])
    edad = IntegerField('edad',[
        validators.DataRequired(message = 'El campo es requerido'),
        validators.number_range(min=1, max=20, message='No valido')
    ])
    correo = EmailField('correo',[
        validators.DataRequired(message = 'El campo es requerido'),
        validators.Email(message = 'Ingresa un correo valido')
    ])