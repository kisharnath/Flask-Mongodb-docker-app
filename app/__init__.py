from flask import Flask
from flask_restful import Resource, Api
from dotenv import load_dotenv
import os
from .bcrypt import bcrypt_

from .utility import Endpoints, SecondEndpoints



def create_app():

    app_ = Flask(__name__)
    api = Api(app_)
    bcrypt_.init_app(app_)
   
    # Add resources to the API
    api.add_resource(Endpoints, '/users')  
    api.add_resource(SecondEndpoints, '/users/<user_id>') 
    return app_