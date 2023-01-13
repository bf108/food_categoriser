from food_categoriser.api import API
from food_categoriser.config import API_KEY
import pytest

def test_api_gen_url():
    api = API(API_KEY)
    assert api._gen_url(1) == 'https://api.spoonacular.com/food/ingredients/1/information'

def test_check_valid_id():
    api = API(API_KEY)
    assert api.check_valid_id(1) == False
    assert api.check_valid_id(1001) == True

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

    assert api.get_info_id(2047) == resp
    with pytest.raises(Exception) as e_info:
        api.get_info('water')

def test_get_info_ing():
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

    assert api.get_info_ingredient('table salt') == resp
    with pytest.raises(Exception) as e_info:
        api.get_info_ing('shoes')

def test_get_ingredient_id():
    api = API(API_KEY)
    assert api.get_ingredient_id('water') == 14412
    assert api.get_ingredient_id('butter') == 1001
    assert api.get_ingredient_id('BUTTER') == 1001
    assert api.get_ingredient_id('xxxx') == None