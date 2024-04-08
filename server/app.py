from flask import Flask, make_response, request
from flask_migrate import Migrate
from models import db, Restaurant, RestaurantPizza, Pizza


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Flask Code Challenge - Pizza Restaurants</h1>'

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    if request.method == 'GET':
        restaurants = Restaurant.query.all()
        return make_response([restaurant.to_dict() for restaurant in restaurants], 200)

@app.route('/restaurants/<int:id>', methods=['GET', 'DELETE'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    
    if restaurant:
        if request.method == 'GET':
            return make_response(restaurant.to_dict(), 200)
        elif request.method == 'DELETE':
            db.session.delete(restaurant)
            db.session.commit()

            response = make_response('', 204)
            return response
    else:
        return make_response({"error": "Restaurant not found"}, 404)

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    response = make_response([pizza.to_dict() for pizza in pizzas], 200)
    return response

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.json
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)

    db.session.add(restaurant_pizza)
    try:
        db.session.commit()
        return make_response(restaurant_pizza.pizza.to_dict(), 201)
    except:
        db.session.rollback()
        return make_response({"errors": ["validation errors"]}, 400)

if __name__ == '__main__':
    app.run(port=5555, debug=True)