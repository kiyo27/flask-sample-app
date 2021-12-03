from apis import api
from apis.todos import api as todos
from flask import Flask, json, Blueprint
from flask_restx import Api

app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost'
blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint, doc='/doc/')
api.add_namespace(todos, path='/todos')
app.register_blueprint(blueprint)

def see_json():
    urlvars = False  # Build query strings in URLs
    swagger = True  # Export Swagger specifications
    data = api.as_postman(urlvars=urlvars, swagger=swagger)
    # print(json.dumps(data))
    f = open('postman_import.json', 'w')
    f.write(json.dumps(data))

with app.app_context():
    see_json()

