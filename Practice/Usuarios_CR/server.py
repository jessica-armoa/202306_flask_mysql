from flask import Flask, render_template, redirect, request
# importar la clase de user.py
from user import User
app = Flask(__name__)

@app.route("/")
def form():
    # llamar al método de clase get all para obtener todos los amigos
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
    # No olvides redirigir después de guardar en la base de datos
    return redirect('/tabla')


@app.route("/tabla")
def tabla():
    # llamar al método de clase get all para obtener todos los amigos
    users = User.get_all()
    print(users)
    return render_template("tabla.html", users = users)

if __name__ == "__main__":
    app.run(debug=True)

