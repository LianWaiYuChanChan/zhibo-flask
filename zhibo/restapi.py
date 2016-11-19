from flask import Flask, request
from flask_restful import Resource, Api


class Account(Resource):
    def get(self):
        return {'id': 'account_1'}

    def post(self):
        json_data = request.get_json(force=True)
        print json_data, type(json_data)
        un = json_data['username']
        pw = json_data['password']
        print un, pw
        return {"id": "res_post"}

    def put(self):
        json_data = request.get_json(force=True)
        pw = json_data['newPassword']
        print pw
        return {'id': 'res_put'}

    def delete(self):
        return {'id': 'res_1'}


def run_zhibo():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Account, '/account')
    app.run(debug=True)
