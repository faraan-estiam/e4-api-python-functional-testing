from RestaurantGuide.classes.RestaurantGuide import RestaurantDoesNotExists, MenuItemDoesNotExists
import pytest

@pytest.mark.parametrize("restaurant, item, description, price, expected_output", [
  ("Static Sushi", "Salmon Sashimi", "RAW Salmon (6pieces)", 5.99, "Salmon Sashimi updated from Static Sushi's menu"),
  ("Permanent Pizza", "Pineapple Pizza", "If you buy one, we'll send your adress to Mauro Rocco (you will die)", 9999999, "Pineapple Pizza updated from Permanent Pizza's menu")
])
def test_valid_update_menu_item(restaurant, item, description, price, expected_output, default_restaurant_guide):
  rg = default_restaurant_guide
  output = rg.update_menu_item(restaurant, item, description, price)
  assert output == expected_output

@pytest.mark.parametrize("restaurant, item, description, price, expected_error_message",[
  ("Static Sushi", "Salmon Sushi", "Salmon (4pieces)", 5, "Static Sushi does not have Salmon Sushi in the menu"),
  ("Static Sushi", "Salmon Sashimi", "Salmon (4pieces)", -4.99, "price must be positive"),
  ("Missing Milkshake", "Mega Mystery", "It's actually an escape game, you will get clues to find us", 25, "Missing Milkshake does not exists")
])
def test_invalid_update_menu_item(restaurant, item, description, price, expected_error_message, default_restaurant_guide):
  rg = default_restaurant_guide
  with pytest.raises((MenuItemDoesNotExists, ValueError, RestaurantDoesNotExists)) as e :
    rg.update_menu_item(restaurant, item, description, price)
  assert str(e.value) == expected_error_message

