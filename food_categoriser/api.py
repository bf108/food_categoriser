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
        self.ingredient_id_mappings = pd.read_csv('data/ingredients.csv',sep=';')\
                                    .set_index('ingredientId')\
                                    .to_dict()['ingredient']

    def _gen_url(self,id:int):
        endpoint = f"food/ingredients/{id}/information"
        url = f"{self.api_root}{endpoint}"
        return url

    def get_info(self, id: int) -> Union[Dict,None]:
        url = self._gen_url(id)
        resp = self.session.request(method='GET',
                                    url=url,
                                    params=self.params,
                                    timeout=self.timeout)
        if resp.status_code == 200:
            return resp.json()
        else:
            return None








