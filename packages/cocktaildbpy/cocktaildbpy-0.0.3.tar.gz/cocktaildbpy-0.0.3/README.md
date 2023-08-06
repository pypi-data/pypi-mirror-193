# cocktaildbpy

A small python library to interact with cocktaildb api (https://www.thecocktaildb.com/api.php)

## Installation

`pip install cocktaildbpy`

## Example Usage

```python
from cocktaildbpy import Api
from cocktaildbpy.constants import Ingredient

def main():
    # "1" is the development/testing api key
    client = Api(api_key="1")
    drinks = client.search_by_ingredient(Ingredient.GIN)
    drink = client.lookup_cocktail_by_id(drinks[0].id)
    print(drink)
    drink = client.get_cocktail_by_name("old fashioned")
    print(drink)

if __name__ == "__main__":
    main()
```