from flask import Flask
from apis import api
from marshmallow.exceptions import ValidationError

app = Flask(__name__)

@app.errorhandler(ValidationError)
def handle_validation_error(error):
    print(error.messages)
    return {"message": error.messages}, 400

# app.register_error_handler(ValidationError, handle_validation_error)

api.init_app(app)

if __name__ == '__main__':
    app.run(
        debug=True, port='80', host='0.0.0.0')