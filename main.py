from flask import Flask, request,render_template, Response
import forms
from flask_wtf.csrf import CSRFProtect
from flask import flash
from flask import g

app=Flask(__name__)
app.secret_key ='esta es la clave secreta'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
        return render_template("index.html")

@app.before_request
def before_request():
    g.prueba ='Hola'
    print('antes de ruta')



@app.route("/alumnos", methods=["GET","POST"])
def alumnos():
        print('dentro de alumnos')
        valor=g.prueba
        print('El dato es: {}'.format(valor))
        nom=''
        apa=''
        correo=''
        flash=''
        alumn_form=forms.UserForm(request.form)
        if request.method=="POST" and alumn_form.validate():
                nom=alumn_form.nombre.data
                apa=alumn_form.apaterno.data
                correo=alumn_form.email.data
                messages = 'Bienvenido {}'.format(nom)
                flash(messages)

                print("nombre:{}".format(nom))
                print("apaterno:{}".format(apa))
                print("apaterno:{}".format(correo))
                messages = 'Bienvenido {}'.format(nom)
                flash(messages)
        return render_template("alumnos.html", form=alumn_form,nom=nom,apa=apa,correo=correo)

@app.after_request
def after_request(response):
    print('despues de ruta 3')
    return response


@app.route("/maestros")
def maestros():
        return render_template("maestros.html")

@app.route("/hola")
def func():
    return "<h1> Saludo desde Hola -UTL !!!</h1>"


@app.route("/saludo")
def func1():
    return "<h1> Saludo desde Hola desde Saludo</h1>"

@app.route("/nombre/<string:nom>")
def nombre(nom):
    return "<h1>Hola</h1>"+nom

@app.route("/numero/<int:n1>")
def numero(n1):
    return "<h1>El valor es: {} </h1>".format(n1)

@app.route("/user/<string:nom>/<int:id>")
def user(nom,id):
    return "ID: {} NOMBRE: {}".format(id,nom)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return "La suma de {} + {} = {}".format(n1,n2,n1+n2)

@app.route("/multiplica", methods=["GET","POST"])
def mult():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        
        return "<h1>El resultado es: {}</h1>".format(int(num1)*int(num2))
    else:
        return '''
            <form action="/multiplica" method="POST">
                <label> N1:</label>
                <input type="number" name="n1"/>
                
                <label> N2:</label>
                <input type="number" name="n2"/>

                <input type="submit">
                
            </form>

        '''

@app.route("/formulario1")
def calculo():
    return render_template("formulario1.html")

@app.route("/resultado", methods=["GET","POST"])
def multiplica():
    if request.method=="POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        
        return "<h1>El resultado es: {}</h1>".format(int(num1)*int(num2))


if __name__=="__main__":
    app.run(debug=True)