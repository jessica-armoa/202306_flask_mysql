from flask import render_template, request, redirect

from flask_app import app

from flask_app.models.dojo import Dojo

@app.route("/")
def inicio():
    return redirect('/dojos')

@app.route("/dojos")
def dojos():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("new_dojo.html", dojos=dojos)

@app.route('/create_dojo', methods=["POST"])
def create_user():
    data = {
        "name" : request.form["name"]
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route("/dojos/<id>")
def ninjas_de_dojo(id):
    dojo=Dojo.get_dojo_with_ninjas(id)
    print(dojo.ninjas)
    return render_template('ninjas.html',dojo=dojo)


