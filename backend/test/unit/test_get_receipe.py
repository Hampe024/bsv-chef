import json
import pytest
from unittest.mock import Mock, patch
from src.controllers.receipecontroller import ReceipeController
# add your test case implementation here

@pytest.mark.parametrize(
    "available_items, diet, expected_result",
    [
        (
            {
                "Egg": 3,
                "Milk": 100,
                "Yoghurt": 200,
                "Flour": 150,
                "Baking Powder": 1,
                "Salt": 5,
                "Sugar": 25
            },
            "normal",
            1
        ),
        (
            {
                "Egg": 4,
                "Milk": 100,
                "Yoghurt": 200,
                "Flour": 150,
                "Baking Powder": 1,
                "Salt": 5,
                "Sugar": 25
            },
            "normal",
            1
        ),
        (
            {
                "Egg": 3,
                "Milk": 100,
                "Yoghurt": 200,
                "Flour": 150,
                "Baking Powder": 1,
                "Salt": 5,
                "Sugar": 25,
                "Vanilla Sugar": 1
            },
            "normal",
            1
        ),
        (
            {
                "Egg": 3,
                "Milk": 99,
                "Yoghurt": 200,
                "Flour": 150,
                "Baking Powder": 1,
                "Salt": 5,
                "Sugar": 25
            },
            "normal",
            0.99
        ),
        (
            {
                "Egg": 3,
                "Milk": 100,
                "Yoghurt": 200,
                "Flour": 150,
                "Baking Powder": 1,
                "Salt": 5,
                "Sugar": 25
            },
            "vegan",
            None
        ),
        (
            {
                "Egg": 0,
                "Milk": 0,
                "Yoghurt": 0,
                "Flour": 0,
                "Baking Powder": 0,
                "Salt": 0,
                "Sugar": 0
            },
            "normal",
            None
        ),
        (
            {
                "Egg": 0,
                "Milk": 1,
                "Yoghurt": 0,
                "Flour": 0,
                "Baking Powder": 0,
                "Salt": 0,
                "Sugar": 0
            },
            "normal",
            None
        ),
        (
            {
                "Egg": 0,
                "Milk": 0,
                "Yoghurt": 0,
                "Flour": 0,
                "Baking Powder": 1,
                "Salt": 5,
                "Sugar": 25
            },
            "normal",
            0.1
        )
    ]
)
@patch('src.controllers.receipecontroller.ReceipeController.__init__')
@pytest.mark.unit
def test_get_receipe_readiness(available_items, diet, expected_result, mocked_calculate):
    
    with open('backend/src/static/dummy_items/pancakes.json', 'r') as file:
        json_data = file.read()
    pancake = json.load(json_data)

    # TODO mock it so it returns 0-1 based on how many of the ingredients exist
    # mocked_calculate.return_value = lambda

    with patch('src.controllers.receipecontroller.ReceipeController.__init__') as init_mock:
        init_mock.return_value = None
        sut = ReceipeController()

    assert sut.get_receipe_readiness(pancake, available_items, diet) == expected_result