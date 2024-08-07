import pytest
from constsnts import Constants
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture
def bun():
    bun = Bun(name=Constants.BUN, price=Constants.BUT_PRICE)
    return bun


@pytest.fixture
def ingredient():
    ingredient = Ingredient(ingredient_type=Constants.INGREDIENT_TYPE, name=Constants.INGREDIENT_NAME,
                            price=Constants.INGREDIENT_PRICE)
    return ingredient
