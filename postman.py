from flask import Flask, json
from apis import api

app = Flask(__name__)

def see_json():
    urlvars = False  # Build query strings in URLs
    swagger = True  # Export Swagger specifications
    data = api.as_postman(urlvars=urlvars, swagger=swagger)
    # print(json.dumps(data))
    f = open('postman_import.json', 'w')
    f.write(json.dumps(data))

with app.app_context():
    see_json()

