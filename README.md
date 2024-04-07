## Flask Code Challenge - Pizza Restaurants

Welcome to the Flask Code Challenge focusing on the Pizza Restaurants domain. In this challenge, you will be building a Flask API to implement various functionalities related to pizza restaurants.

### Models

You are required to create the following relationships in your database:

- A Restaurant has many Pizzas through RestaurantPizza.
- A Pizza has many Restaurants through RestaurantPizza.
- A RestaurantPizza belongs to a Restaurant and belongs to a Pizza.

Begin by creating the necessary models and migrations for the specified database tables.

![Domain](domain.png)

#### Validations

Ensure the following validations are implemented:

- **RestaurantPizza Model:**
  - Must have a price between 1 and 30.

- **Restaurant Model:**
  - Must have a name less than 50 characters in length.
  - Must have a unique name.

### Routes

Set up the following routes. Make sure to return JSON data in the specified format along with the appropriate HTTP verb.

#### GET /restaurants

Returns a list of restaurants in the following JSON format:

```json
[
  {
    "id": 1,
    "name": "Dominion Pizza",
    "address": "Good Italian, Ngong Road, 5th Avenue"
  },
  {
    "id": 2,
    "name": "Pizza Hut",
    "address": "Westgate Mall, Mwanzi Road, Nrb 100"
  }
]
```

#### GET /restaurants/:id

Links to an external site.

If the Restaurant exists, return JSON data in the format below:

```json
{
  "id": 1,
  "name": "Dominion Pizza",
  "address": "Good Italian, Ngong Road, 5th Avenue",
  "pizzas": [
    {
      "id": 1,
      "name": "Cheese",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    }
  ]
}
```

If the Restaurant does not exist, return the following JSON data, along with the appropriate HTTP status code:

```json
{
  "error": "Restaurant not found"
}
```