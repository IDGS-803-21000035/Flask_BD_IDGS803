from flask import Flask, render_template, request, flash, Response
#proceso de seguridad
from flask_wtf.csrf import CSRFProtect
from flask import redirect
#variable global
from flask import g

from config import DevelopmentConfig

import forms

#importación de las tablas
from models import db, Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



@app.route("/index", methods=["GET", "POST"])
def index():
    alum_form = forms.UserForm2(request.form)
    if request.method == 'POST':
        #instancia de clase
        alum = Alumnos(nombre=alum_form.nombre.data, apaterno = alum_form.apaterno.data, email = alum_form.email.data)

        #usar orm, con add inserto parametros
        db.session.add(alum)
        #guardar ddatos
        db.session.commit()

    
    return render_template("index.html", form = alum_form)

@app.route("/ABC_Completo", methods = ["GET","POST"])
def ABC_Completo():
    alum_form = forms.UserForm2(request.form)
    alumno = Alumnos.query.all()
    return render_template("ABC_Completo.html", alumnos = alumno)

@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    nom = ''
    apa = ''
    ama = ''
    edad = ''
    correo = ''

    alum_form = forms.UserForm(request.form)
    if request.method == 'POST' and alum_form.validate():
        nom = alum_form.nombre.data
        apa = alum_form.apaterno.data
        ama = alum_form.amaterno.data
        edad = alum_form.edad.data
        correo = alum_form.correo.data


        print(f'Nombre: {nom}, aPaterno: {apa}, aMaterno: {ama}, Edad: {edad}, Correo: {correo}')

    return render_template("alumnos.html", form=alum_form, nom=nom, apa=apa, ama=ama, edad=edad, correo=correo)


if __name__== "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()