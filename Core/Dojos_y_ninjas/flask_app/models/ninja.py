from flask_app.config.mysqlconnection import connectToMySQL
class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']

    # método de clase para guardar a nuestro usuario en la base de datos
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at) VALUES ( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW());"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('dojos_y_ninjas').query_db( query, data )
