import os
import requests
from typing import Union, Dict
import pandas as pd

class API:
    def __init__(self, apiKey:str):
        self.session = requests.Session()
        self.session.headers = {"Application": "spoonacular",
        "Content-Type": "application/x-www-form-urlencoded"}
        self.api_root = 'https://api.spoonacular.com/'
        self.apiKey = apiKey
        self.timeout = 5
        self.params = {'apiKey':self.apiKey}
        self.data = pd.read_csv(os.path.join(os.path.dirname(__file__),'data/ingredients.csv'),sep=';')
        self.valid_ids = list(self.data['ingredientId'].unique())
        df = self.data.copy()
        df['ingredient'] = df['ingredient'].str.strip().str.lower()
        self.ing_id_map = df.set_index('ingredient').to_dict()['ingredientId']

    def check_valid_id(self, id: int) -> bool:
        return id in self.valid_ids

    def _gen_url(self, id: int):
        endpoint = f"food/ingredients/{id}/information"
        url = f"{self.api_root}{endpoint}"
        return url
    
    def _get_response(self, url: str) -> Union[requests.models.Response]:
        return self.session.request(method='GET',
                                        url=url,
                                        params=self.params,
                                        timeout=self.timeout)

    def _eval_response(self, resp: requests.models.Response) -> Dict:
        if resp.status_code == 200:
            return resp.json()
        elif resp.status_code == 401:
            raise AttributeError('Invalid Credentials')
        elif resp.status_code == 404:
            raise AttributeError('404 Not Found')
        else:
            raise AttributeError(f'Error: {resp.status_code}')

    def get_info_id(self, id: int) -> Dict:
        if self.check_valid_id(id):
            url = self._gen_url(id)
            resp = self._get_response(url)
            return self._eval_response(resp)
        raise AttributeError('Invalid Id')

    def get_info_ingredient(self, ingredient: str) -> Dict:
        if ingredient in self.ing_id_map.keys():
            id = self.ing_id_map[ingredient]
            url = self._gen_url(id)
            resp = self._get_response(url)
            return self._eval_response(resp)
        raise AttributeError('Ingredient Not Found')

    def get_info_concise(self, ingredient: str) -> Dict:
        try:
            full_results = self.get_info_ingredient(ingredient)
            concise = {'id': full_results['id'],
                        'name': full_results['original'].lower(),
                        'image': full_results['image'],
                        'categoryPath': full_results['categoryPath'],
                        'response':200 
                        }
            return concise
        except AttributeError as exp:
            return {'id': None,
                    'name': ingredient.strip().lower(),
                    'image': None,
                    'categoryPath': [None],
                    'response': f"{exp}"}
