from dataclasses import dataclass
from typing import List, Dict

from cocktaildbpy.constants import Category, Ingredient, Glass


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

@dataclass
class Drink:
    id: str
    name: str
    category: str
    alcoholic: bool
    glass: str
    instructions: List[str]
    ingriedients: Dict[str, str]

    @classmethod
    def loads(cls, **kwargs):
        ingriedients = {}
        for k, v in kwargs.items():
            if "Ingredient" in k:
                if v is not None:
                    num = k.split("Ingredient")[1]
                    ingriedients[v] = kwargs[f"strMeasure{num}"]

        return cls(
            id=kwargs["idDrink"],
            name=kwargs["strDrink"],
            category=Category(str(kwargs["strCategory"]).lower()),
            alcoholic=True if kwargs["strAlcoholic"] == "Alcoholic" else False,
            glass=Glass(str(kwargs["strGlass"]).lower()),
            instructions=kwargs["strInstructions"].split("."),
            ingriedients=ingriedients,
        )
