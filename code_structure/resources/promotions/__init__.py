from config import api
from .promotions import Template

api.add_resource(Template, '/promotions/template', endpoint="Template")