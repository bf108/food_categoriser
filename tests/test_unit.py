from food_categoriser.api import API
from food_categoriser.config import API_KEY
import pytest
from requests.models import Response

def test_api_gen_url():
    api = API(API_KEY)
    assert api._gen_url(1) == 'https://api.spoonacular.com/food/ingredients/1/information'

def test_check_valid_id():
    api = API(API_KEY)
    assert api.check_valid_id(1) == False
    assert api.check_valid_id(1001) == True

def test_get_response():
    api = API(API_KEY)
    url = api._gen_url(1001)
    url_invalid = api._gen_url(1)
    assert api._get_response(url).status_code == 200
    assert api._get_response(url_invalid).status_code == 404

def test_eval_response():
    api = API(API_KEY)
    url = api._gen_url(1001)
    resp = api._get_response(url)
    assert type(api._eval_response(resp)) == dict
    
    api = API('test')
    url = api._gen_url(1001)
    resp = api._get_response(url)
    with pytest.raises(Exception) as exp:
        api._eval_response(resp)

    api = API(API_KEY)
    url = api._gen_url(1)
    resp = api._get_response(url)
    with pytest.raises(Exception) as exp:
        api._eval_response(resp)

def test_get_info_id():
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
        api.get_info_id('water')

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
        api.get_info_ingredient('shoes')

def test_get_info_concise():
    api = API(API_KEY)
    resp = {'id': 2047,
        'name': 'table salt',
        'image': 'salt.jpg',
        'categoryPath': ['salt'],
        'response': 200}
    invalid_resp = {'id': None,
                    'name': 'xxxx',
                    'image': None,
                    'categoryPath': [None],
                    'response': "Ingredient Not Found"}
    
    assert api.get_info_concise('xxxx') == invalid_resp
    assert api.get_info_concise('table salt') == resp