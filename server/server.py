from flask import Flask
from flask_restful import Resource, Api
from flask_cors import cross_origin, CORS
import pickle

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r'/*':{"origins": 'http://localhost:4000'}})

class Recipes(Resource):
	def get(self):
		# return {'hello': 'world', "ingredients": recipes[1]}
		return str(recipes[list(recipes.keys())[0]])

api.add_resource(Recipes, '/cookease/recipes/')

class Test(Resource):
	def get(self):
		return "hello world"
api.add_resource(Test, '/')

if __name__ == '__main__':
	with open("../data/ingredients.pkl", "rb") as file:
		ingredients = list(pickle.load(file))
	with open("../data/id_recipes.pkl", "rb") as file:
		recipes = pickle.load(file)
	app.run(debug=True)