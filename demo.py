from flask import Flask
from flask_restful import Api, Resource, reqparse

demo = Flask(__name__)
api = Api(demo)

users = [
    {
        "id": "1",
        "First_name": "Abhijeet",
        "Last_name": "Ahirwar",
        "age": 21,
        "occupation": "Computer Science Engineer"
    },
    {
        "id": "2",
        "First_name": "Colin",
        "Last_name": "Startus",
        "age": 22,
        "occupation": "Web Developer"
    }
]


class User(Resource):
    def get(self, id):                          # retrieving user data
        for user in users:
            if id == user["id"]:
                return user, 200
        return "User not found", 404

    def post(self, id):                         # creating a new user
        parser = reqparse.RequestParser()
        parser.add_argument("First_name")
        parser.add_argument("Last_name")
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if id == user["id"]:
                return "User with id {} already exists".format(id), 400

        user = {
            "First_name": args["First_name"],
            "Last_name": args["Last_name"],
            "age": args["age"],
            "id" : id,
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def put(self, id):                        # Update details of user and create a new user if not created
        parser = reqparse.RequestParser()
        parser.add_argument("First_name")
        parser.add_argument("Last_name")
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:                      # For Updating the existing user detail
            if id == user["id"]:
                user["First_name"] = args["First_name"]
                user["Last_name"] = args["Last_name"]
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200

        user = {
            "id": id,
            "First_name": args["First_name"],
            "Last_name": args["Last_name"],
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def delete(self, id):                       # deleting the existing user
        global users
        users = [user for user in users if user["is"] != id]
        return "{} is deleted.".format(id), 200


api.add_resource(User, "/user/<string:id>")

demo.run(debug=True)