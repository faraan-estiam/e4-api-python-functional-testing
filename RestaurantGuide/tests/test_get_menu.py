import pytest

@pytest.mark.parametrize("restaurant, expected_output", [
  ('Default Diner', []),
  ("Static Sushi", [{"name": "Salmon Sashimi", "description": "Salmon (6 pieces)", "price": 5.99}]),
  ("Permanent Pizza", [
    {"name": "Pepperoni Pizza", "description": "A pizza with pepperoni on it", "price": 7.50},
    {"name": "Pineapple Pizza", "description": "A demon comming straight from hell", "price": 666}
  ])
])
def test_get_menu(restaurant, expected_output, default_restaurant_guide):
  rg = default_restaurant_guide
  output = rg.get_menu(restaurant)
  assert output == expected_output