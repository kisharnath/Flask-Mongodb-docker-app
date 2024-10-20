
from app.utility import *
from app import api
from flask_restful import Resource, Api
api.add_resource(Endpoints, '/')
