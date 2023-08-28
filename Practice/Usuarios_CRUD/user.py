# importar la función que devolverá una instancia de una conexión
from mysqlconnection import connectToMySQL
# modelar la clase después de la tabla friend de nuestra base de datos
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['nombre']
        self.last_name = data['apellido']
        self.email = data['correo_electronico']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('usuarios_bd').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de users
        users = []
        # Iterar sobre los resultados de la base de datos y crear instancias de users con cls
        for user in results:
            users.append( cls(user) )
        return users

    # método de clase para guardar a nuestro usuario en la base de datos
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO usuarios ( nombre , apellido , correo_electronico , created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('usuarios_bd').query_db( query, data )

    @classmethod
    def get(cls,id):
        data = {"id" : id}
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        results = connectToMySQL('usuarios_bd').query_db(query, data)
        if results:
            return cls(results[0])
        return None

    def delete(self):
        data = {"id" : self.id}
        query = "DELETE FROM usuarios WHERE id =  %(id)s;"
        connectToMySQL('usuarios_bd').query_db(query, data)
        return True

    def edit(self):
        data = {
            "id" : self.id,
            "fname" : self.first_name,
            "lname" : self.last_name,
            "email" : self.email
        }
        query = "UPDATE usuarios SET nombre = %(fname)s, apellido = %(lname)s, correo_electronico = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
        connectToMySQL('usuarios_bd').query_db(query, data)
        return True