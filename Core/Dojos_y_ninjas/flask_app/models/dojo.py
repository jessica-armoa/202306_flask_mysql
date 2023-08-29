from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.ninjas = []
    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL('dojos_y_ninjas').query_db(query)
        print(results)
        # crear una lista vacía para agregar nuestras instancias de dojos
        dojos = []
        # Iterar sobre los resultados de la base de datos y crear instancias de users con cls
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    # método de clase para guardar a nuestro usuario en la base de datos
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos (name, created_at) VALUES ( %(name)s, NOW());"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('dojos_y_ninjas').query_db( query, data )

    @classmethod
    def get_dojo_with_ninjas(cls,dojo_id):
        data ={"dojo_id" : dojo_id}
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(dojo_id)s;"
        results = connectToMySQL('dojos_y_ninjas').query_db(query,data)
        print("RESULTADOS",results)
        dojo = cls(results[0])
        # Iterar sobre los resultados de la base de datos y crear instancias
        for row in results:
            ninja_data = {
                "id" : row["ninjas.id"],
                "first_name" : row["first_name"],
                "last_name" : row["last_name"],
                "age" : row["age"],
                "dojo_id" : row["dojo_id"],
                "created_at" : row["created_at"]
            }
            dojo.ninjas.append(Ninja(ninja_data))
        for n in dojo.ninjas:
            print(n.id)
        return dojo
