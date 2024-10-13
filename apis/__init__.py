from flask_restx import Api
from .todos import api as todos
from .pets import api as pets

api = Api(
    version='1.0',
    title='Sample API',
    description='A sample API',
    doc="/doc/"
)

api.add_namespace(todos, path='/api/todos')
api.add_namespace(pets, path='/api/pets')