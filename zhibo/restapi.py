from flask import Flask
from flask_restful import Resource, Api


class HelloWorld(Resource):
    def get(self):
        return {'Hello': 'World'}


def run_zhibo():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(HelloWorld, '/')
    app.run(debug=True)
