from flask import Flask, render_template, redirect, request
# importar la clase de user.py
from user import User
app = Flask(__name__)

@app.route("/")
def inicio():
    return redirect('/users')

@app.route("/users/new")
def form():
    # llamar al método de clase get all para obtener todos los usuarios
    users = User.get_all()
    print(users)
    return render_template("formulario.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    # Primero hacemos un diccionario de datos a partir de nuestro request.form proveniente de nuestra plantilla
    # Las claves en los datos tienen que alinearse exactamente con las variables en nuestra cadena de consulta
    data = {
        "fname" : request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # Pasamos el diccionario de datos al método save de la clase Friend
    User.save(data)
    return redirect('/users')

@app.route("/users")
def usuarios():
    # llamar al método de clase get all para obtener todos los amigos
    users = User.get_all()
    print(users)
    return render_template("tabla.html", users = users)

@app.route("/users/<id>")
def usuario(id):
    user = User.get(id)
    print(user)
    return render_template("ver_datos_usuario.html", user = user)

@app.route("/users/<id>/edit")
def edit(id):
    user = User.get(id)
    print(user)
    return render_template("editar_datos_usuario.html", user = user)

@app.route('/edit_user/<id>', methods=["POST"])
def edit_user(id):
    user = User.get(id)
    user.first_name = request.form["fname"]
    user.last_name = request.form["lname"]
    user.email = request.form["email"]
    user.edit()
    return redirect('/users/'+id)

@app.route("/users/<id>/delete")
def delete(id):
    user = User.get(id)
    print("Usuario a eliminar: ", user)
    user.delete()
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)

