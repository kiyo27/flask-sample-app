from flask_restx import Namespace, Resource, fields

api = Namespace('petss', description='TODO operations')

pet = api.model('Todo', {
    'id': fields.String(readonly=True,
                        description='The task unique identifier',
                        example='1'),
    'name': fields.String(required=True,
                         description='The pet name',
                         example='pug'),
})

@api.route('/')
class TodoList(Resource):
    @api.doc('list_todos')
    @api.marshal_list_with(pet)
    def get(self):
        return {"id": 1, "name": "pug"}
