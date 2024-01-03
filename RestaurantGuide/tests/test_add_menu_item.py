from RestaurantGuide.classes.RestaurantGuide import MenuItemAlreadyExists, RestaurantDoesNotExists
import pytest

@pytest.mark.parametrize("restaurant, item, description, price, expected_output",[
  ("Default Diner", "Data", "Couldn't find anything eatable that starts with 'D'", 1, "Data added to Default Diner's menu"),
  ("Default Diner", "Dust", "Maybe you could eat this, I wouldn't recommend", 0.01, "Dust added to Default Diner's menu")
])
def test_valid_add_menu_item(restaurant, item, description, price, expected_output, default_restaurant_guide):
  rg = default_restaurant_guide
  output = rg.add_menu_item(restaurant, item, description, price)
  assert output == expected_output

@pytest.mark.parametrize("restaurant, item, description, price, expected_error_message",[
  ("Static Sushi", "Salmon Sashimi", "Salmon (4pieces)", 1.10, "Static Sushi already has Salmon Sashimi in the menu"),
  ("Default Diner", "Dust", "I'll pay you if you eat it, or just get a broom and clean the place idk", -100, "price must be positive"),
  ("Missing Milkshake", "Mega Mystery", "It's actually an escape game, you will get clues to find us", 25, "Missing Milkshake does not exists")
])
def test_invalid_add_menu_item(restaurant, item, description, price, expected_error_message, default_restaurant_guide):
  rg = default_restaurant_guide
  with pytest.raises((MenuItemAlreadyExists, ValueError, RestaurantDoesNotExists)) as e :
    rg.add_menu_item(restaurant, item, description, price)
  assert str(e.value) == expected_error_message

