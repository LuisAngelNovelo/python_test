from flask_restful import Resource
from config import slave, db

class Index(Resource):

	def get(self):
		return {}, 200