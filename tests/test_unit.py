from food_categoriser.api import API
from food_categoriser.config import API_KEY

def test_api_gen_url():
    api = API(API_KEY)
    assert api._gen_url(1) == 'https://api.spoonacular.com/food/ingredients/1/information'

def test_get_info():
    api = API(API_KEY)
    resp = {'id': 2047,
            'original': 'table salt',
            'originalName': 'table salt',
            'name': 'table salt',
            'possibleUnits': ['pinch','g','oz','dash','teaspoon','cup','serving','tablespoon'],
            'consistency': 'solid',
            'aisle': 'Spices and Seasonings',
            'image': 'salt.jpg',
            'meta': [],
            'categoryPath': ['salt']}

    assert api.get_info(2047) == resp
    assert api.get_info('water') == 404