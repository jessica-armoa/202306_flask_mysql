from flask import render_template, request, redirect

from flask_app import app

from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/ninjas")
def ninjas():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("new_ninja.html", dojos=dojos)

@app.route('/create_ninja', methods=["POST"])
def create_ninja():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo_id"]
    }
    Ninja.save(data)
    return redirect('/dojos')
