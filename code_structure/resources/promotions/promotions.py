from flask_restful import Resource
from config import slave


class Template(Resource):

	@slave.access_middleware
	def post(self):
		return {}, 200