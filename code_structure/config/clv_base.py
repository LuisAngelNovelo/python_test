from flask import request
from flask_restful import Resource
from functools import wraps
import requests


__all__ = ["SlaveHandler"]

STATUS_CODES = {
	200: "Ok",
	201: "Create",
	202: "Accept",
	203: "Non-Authoritative Information",
	204: "No Content",
	400: "Bad Request",
	401: "Unauthorized",
	403: "Forbidden",
	404: "Not Found",
	405: "Method Not Allowed",
	409: "Conflict",
	422: "Unprocessable Entity",
	500: "Internal Server Error",
	408: "Request Timeout",
	406: "Not Acceptable",
	409: "Conflict",
	410: "Gone",
	413: "Request Entity Too Large",
	414: "Request URI Too Large",
	417: "Expectation Failed",
	429: "TooManyRequests",
	503: "Service Unavailable"}

URLS = {
	"DEV": {
		"rates": "http://dev.clever-api-rates.local",
		"auth": "http://auth-api-qa.clever.palace-resorts.local",
		"secrets": "http://missecretosmasoscuros-dev.local",
		"logs": "http://mislogs-dev.local"},
	"QA": {
		"rates": "http://rates-api-qa.clever.palace-resorts.local",
		"auth": "http://auth-api-qa.clever.palace-resorts.local",
		"secrets": "http://missecretosmasoscuros-qa.local",
		"logs": "http://mislogs-qa.local"},
	"PRO": {
		"rates": "http://rates-api.clever.palace-resorts.local",
		"auth": "http://clever.auth-api.palace-resorts.local",
		"secrets": "http://missecretosmasoscuros-pro.local",
		"logs": "http://mislogs-pro.local"}}


class SlaveHandler:

	def __init__(self, app=None):
		self.__CONFIG = app.config

	@property
	def environment(self):
		return self.app_config("APP_ENV")

	@property
	def system_id(self):
		return self.app_config("SYSTEM_ID")

	# Decorator to validate Bearer Token in request.
	def access_middleware(self, func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			if 'Authorization' not in request.headers:
				return self.build_error_response(400, "EMPTY TOKEN OR NOT RECEIVED")
			else:
				# Request auth to validate token
				try:
					resource = 'Flask%s' % request.endpoint
					method = request.method.lower()
					url = self.get_url('auth')
					system_id = self.system_id
					auth_url = "%s/acl/acl/%s/%s/%s" % (url, resource, method, system_id)
					response = self.request(url=auth_url)
					if response['allowed_access'] is False:
						return self.build_error_response(403, response['message'])
				except Exception as e:
					return self.build_error_response(401, "BAD TOKEN GET A NEW ONE")
				# Execute resource function
				try:
					return func(*args, **kwargs)
				except Exception as e:
					return self.build_error_response(500, "Something went wrong!")
		return wrapper

	def decode_base64(self):
		pass

	def app_config(self, key):
		""" Returns Flask.config global variables """
		return self.__CONFIG.get(key, "")

	def build_error_response(self, status=500, return_code=True):
		response = {
			"success": False,
			"status": status,
			"message": [STATUS_CODES.get(status, "Error")],
			"data": []
		}
		if return_code:
			return response, status
		return response

	def request(
		self, url="", method="get", data={},
		content_type="application/json", auth=True, timeout=15):
		"""Make HTTP GET/POST/PUT requests"""

		try:
			headers = {}
			if not auth:
				headers = {"Authorization": request.headers["Authorization"]}
			if content_type == "application/json":
				data = json.dumps(data)
			headers["content-type"] = content_type
			response = None
			if method == "post":
				response = requests.post(url, data=data, headers=headers)
			elif method == "put":
				response = requests.put(url, data=data, headers=headers)
			else:
				response = requests.get(url, headers=headers)
			if content_type == "application/json":
				response = json.loads(response.text)
			return response
		except Timeout as e:
			return self.build_error_response(408)
		except Exception as e:
			return self.build_error_response(500)

	def get_url(self, module):
		""" Gets API urls """

		url = URLS.get(self.environment, "DEV").get(module, "")
		return url

	def get_db_uri(self):
		""" Retrieves database secret from AWS """

		dbapi = self.app_config("SQLALCHEMY_DBAPI")
		database = self.app_config("SQLALCHEMY_DATABASE")
		params = self.app_config("SQLALCHEMY_PARAMS")

		if type(params) is dict:
			params = "?%s" % "".join(
				["&%s=%s" % (key, value) for (key, value) in params.items()])

		username = "clv-rates-adm"
		password = "fk+ZrP3)8TSeb"
		host = "mysqldev57-cluster.cluster-cdrfidjuoewu.us-east-1.rds.amazonaws.com"
		db_uri = "{dbapi}://{username}:{password}@{host}/{database}{params}".format(
			dbapi=dbapi, username=username, password=password,
			host=host, database=database, params=params)
		return db_uri

	def save_log(self, message):
		""" Saving logs in AWS """
		url = self.get_url("logs")
		log_description = "Saving log in {url}: {message}"
		print(log_description.format(url=url, message=message))

	def werkzeug_errors(self):
		""" Custom errors for flask_restful """

		errors = {
			'NotFound': self.build_error_response(404, return_code=False),
			'Forbidden': self.build_error_response(403, return_code=False),
			'MethodNotAllowed': self.build_error_response(405, return_code=False),
			'InternalServerError': self.build_error_response(500, return_code=False),
			'Unauthorized': self.build_error_response(401, return_code=False),
			'BadRequest': self.build_error_response(400, return_code=False),
			'RequestTimeout': self.build_error_response(408, return_code=False),
			'NotAcceptable': self.build_error_response(406, return_code=False),
			'Conflict': self.build_error_response(409, return_code=False),
			'Gone': self.build_error_response(410, return_code=False),
			'RequestEntityTooLarge': self.build_error_response(413, return_code=False),
			'RequestURITooLarge': self.build_error_response(414, return_code=False),
			'ExpectationFailed': self.build_error_response(417, return_code=False),
			'TooManyRequests': self.build_error_response(429, return_code=False),
			'ServiceUnavailable': self.build_error_response(503, return_code=False),
		}
		return errors
