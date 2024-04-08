from app import app
from models import db, Restaurant, RestaurantPizza, Pizza

with app.app_context():
    Restaurant.query.delete()
    Pizza.query.delete()
    RestaurantPizza.query.delete()

    restaurant1 = Restaurant(name='Dominion Pizza', address='Good Italian, Ngong Road, 5th Avenue')
    restaurant2 = Restaurant(name='Pizza Hut', address='Westgate Mall, Mwanzi Road, Nrb 100')

    # save restaurants
    db.session.add_all([restaurant1, restaurant2])
    db.session.commit()
    print('Restaurants succesfully created')

    pizza1 = Pizza(name='Cheese', ingredients='Dough, Tomato Sauce, Cheese')
    pizza2 = Pizza(name='Pepperoni', ingredients='Dough, Tomato Sauce, Cheese, Pepperoni')

    # save pizzas
    db.session.add_all([pizza1, pizza2])
    db.session.commit()
    print('Pizzas succesfully created')

    restaurant_pizzas1 = RestaurantPizza(price=3, pizza_id=1, restaurant_id=2)
    restaurant_pizzas2 = RestaurantPizza(price=30, pizza_id=2, restaurant_id=1)

    # save restaurant pizzas
    db.session.add_all([restaurant_pizzas1, restaurant_pizzas2])
    db.session.commit()
    print('Restaurant Pizzas succesfully created')