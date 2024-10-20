from flask_restful import Resource
from flask import request , jsonify
from .db import getDb
from .bcrypt import bcrypt_
from bson.objectid import ObjectId

client  = getDb()
db = client['UserDatabse']  
collection = db['My-database']  

class Endpoints(Resource):

    def get(self):
        items = list(collection.find({}))  
        result = []
        for document in items:
            document['_id'] = str(document['_id'])  # Convert ObjectId to string
            result.append(document)
        return jsonify(result)
    
    def post(self):
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        hashing_passowrd = bcrypt_.generate_password_hash(password)
        user = {
            "name":name,
            "email":email,
            "password":hashing_passowrd
        }
        print(user)
        exist_user =collection.find_one({"email":email})
        if exist_user :
            return {'message': 'user already exist'}, 201 
        else:
            j = collection.insert_one(user).inserted_id

            return {'message': 'Successfully created'}, 201 
        
    def put(self):
        email = request.form.get('email')
        password = request.form.get('password')

        name = request.form.get('name')
        new_password =request.form.get('New_password')

        new_hashing_passowrd = bcrypt_.generate_password_hash(new_password)

        user_exist = collection.find_one({"email":email})


        if user_exist and bcrypt_.check_password_hash(user_exist['password'], password):

            update = collection.update_one(
                {"email":email},
                {"$set": {"name": name,"password":new_hashing_passowrd}} 
                )
            return {'message': 'Successfully update Name and Password'}, 201 
        else :

            return {'message': 'No user found or Password is wrong' }, 401 
    
    def delete(self):
        email = request.form.get('email')
        password = request.form.get('password')

        user_exist = collection.find_one({"email":email})

        if user_exist and bcrypt_.check_password_hash(user_exist['password'], password):
            deleted = collection.delete_one({"email":email})
            return {'message': 'Successfully deleted' }, 201
        else :
            return {'message': 'No user found or Password is wrong' }, 401 


class SecondEndpoints(Resource):
     
     def get(self, user_id):
         exist = collection.find_one({"_id":ObjectId(user_id)})
         if exist:
             exist['_id'] = str(exist['_id'])
             for key, value in exist.items():
                if isinstance(value, bytes):
                    exist[key] = value.decode('utf-8')
             print(exist)
             return jsonify(exist)
         else :
             return jsonify({'message':'User does not exist'})
         
     def put(self,user_id):
        name = request.form.get('name')
        email = request.form.get('email')
        new_password =request.form.get('New_password')
        new_hashing_passowrd = bcrypt_.generate_password_hash(new_password)
        user_exist = collection.find_one({"_id":ObjectId(user_id)})
        if user_exist :
            update = collection.update_one(
                {"_id":ObjectId(user_id)},
                {"$set": {"name": name,"email":email,"password":new_hashing_passowrd}} 
                )
            return {'message': 'Successfully update Name and Password'}, 201 
        else :

            return {'message': 'No user found ' }, 401 
             
     def delete(self,user_id):
        user_exist = collection.find_one({"_id":ObjectId(user_id)})

        if user_exist :
            deleted = collection.delete_one({"_id":ObjectId(user_id)})
            return {'message': 'Successfully deleted' }, 201
        else :
            return {'message': 'No user found ' }, 401     
         

