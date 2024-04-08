from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'
    serialize_only = ('id', 'name', 'address',)
    serialize_rules = ('-restaurant_pizzas.restaurant',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    address = db.Column(db.String, nullable=False)

    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Restaurant {self.id}, {self.name}, {self.address}>'

class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'
    serialize_only = ('id', 'name', 'ingredients',)
    serialize_rules = ('-restaurant_pizzas.pizza',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ingredients = db.Column(db.String, nullable=False)

    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='pizza', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Pizza {self.id}, {self.name}, {self.ingredients}>'

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    serialize_rules = ('-restaurant.restaurant_pizzas', '-pizza.restaurant_pizzas',)

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)

    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)

    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')

    def __repr__(self):
        return f'<RestaurantPizza {self.id}, {self.price}, {self.restaurant_id}, {self.pizza_id}>'

# Validations
# class RestaurantPizza(db.Model):
#     __tablename__ = 'restaurant_pizzas'

#     id = db.Column(db.Integer, primary_key=True)
#     price = db.Column(db.Float, nullable=False)

#     restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
#     pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)

#     restaurant = db.relationship('Restaurant', backref=db.backref('restaurant_pizzas', cascade='all, delete-orphan'))
#     pizza = db.relationship('Pizza', backref=db.backref('restaurant_pizzas', cascade='all, delete-orphan'))

#     def __repr__(self):
#         return f'<RestaurantPizza {self.id}, {self.price}, {self.restaurant_id}, {self.pizza_id}>'
