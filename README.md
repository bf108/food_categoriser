# Overview 

Web API to classify ingredients into food categories

Built ontop of https://spoonacular.com/food-api web api.

You will require an API Key to get started. It is free to [sign up](https://spoonacular.com/food-api/console#Dashboard) for basic use (~200 requests per day)

Data is available on over 5000 ingredients. The ingredient to id mapping is in data/ingredients.csv

# Getting Started 
```
from food_categoriser.api import API
API_KEY = "INSERT_YOUR_API_KEY"
api = API(API_KEY)

#Get information for specific ingredients
resp = api.get_info_ingredient('table salt')

resp =>
{'id': 2047,
'original': 'table salt',
'originalName': 'table salt',
'name': 'table salt',
'possibleUnits': ['pinch','g','oz','dash','teaspoon','cup','serving','tablespoon'],
'consistency': 'solid',
'aisle': 'Spices and Seasonings',
'image': 'salt.jpg',
'meta': [],
'categoryPath': ['salt']}

#Get concise info
resp = api.get_concise_info('table salt')

resp =>
{'id': 2047,
'name': 'table salt',
'image': 'salt.jpg',
'categoryPath': ['salt'],
'response': 200}

```
