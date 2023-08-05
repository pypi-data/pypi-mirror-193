from dataclasses import dataclass
from typing import List, Union
from urllib.parse import urljoin

import requests
from requests import Session

from cocktaildbpy.drink import Drink
from cocktaildbpy.constants import Ingredient


@dataclass
class DrinkShortcut:
    name: str
    thumbnail: str
    id: str

    @classmethod
    def loads(cls, **kwargs):
        return cls(
            name=kwargs["strDrink"],
            thumbnail=kwargs["strDrinkThumb"],
            id=kwargs["idDrink"],
        )


class ApiSession(Session):
    def __init__(self, base_url=None):
        super().__init__()
        self.base_url = base_url

    def request(self, method, url, *args, **kwargs):
        joined_url = urljoin(self.base_url, url)
        return super().request(method, joined_url, *args, **kwargs)


class Api:
    base_url = "https://www.thecocktaildb.com/api/json/v1/"

    def __init__(self, api_key):
        self.client = ApiSession(base_url=self.base_url + f"/{api_key}/")

    def get_cocktail_by_name(self, name: str) -> Drink:
        r = self.client.get("search.php", params={"s": name})
        response = r.json()
        if response["drinks"] is None:
            raise ValueError("Drink not found")
        drink = Drink.loads(**response["drinks"][0])
        return drink

    def lookup_cocktail_by_id(self, id: str) -> Drink:
        r = self.client.get("lookup.php", params={"i": id})
        response = r.json()
        if response["drinks"] is None:
            raise ValueError("Drink not found")
        drink = Drink.loads(**response["drinks"][0])
        return drink

    def search_by_ingredient(self, ingredient: Union[str, Ingredient]) -> List[DrinkShortcut]:
        __ingredient = ingredient if isinstance(ingredient, str) else ingredient.value
        r = self.client.get("filter.php", params={"i": __ingredient})
        response = r.json()
        if response["drinks"] is None:
            raise ValueError("Ingredient not found")
        drinks = [DrinkShortcut.loads(**x) for x in response["drinks"]]
        return drinks
