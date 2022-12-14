from urllib.parse import uses_relative
from mysqlconnection import connectToMySQL

class User:
    def __init__( self, data):
        self.id = data['id']
        self.fname = data['first_name']
        self.lname = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def __repr__( self ):
        return(
            f'Id: {self.id}\n'
            f'First Name: {self.fname}\n'
            f'Last Name: {self.lname}\n'
            f'Email: {self.email}\n'
            f'Created At: {self.created_at}\n'
            f'Updated At: {self.updated_at}\n'

        )

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []

        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def add(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, NOW(), NOW());"

        return connectToMySQL('users_schema').query_db(query, data)