from RestaurantGuide.classes.RestaurantGuide import RestaurantDoesNotExists, MenuItemDoesNotExists
import pytest

@pytest.mark.parametrize("restaurant, item, expected_output", [
  ("Static Sushi", "Salmon Sashimi", "Salmon Sashimi removed from Static Sushi's menu"),
  ("Permanent Pizza", "Pineapple Pizza", "Pineapple Pizza removed from Permanent Pizza's menu")
])
def test_valid_delete_menu_item(restaurant, item, expected_output, default_restaurant_guide):
  rg = default_restaurant_guide
  output = rg.delete_menu_item(restaurant, item)
  assert output == expected_output

@pytest.mark.parametrize("restaurant, item, expected_error_message",[
  ("Static Sushi", "Salmon Sushi", "Static Sushi does not have Salmon Sushi in the menu"),
  ("Missing Milkshake", "Mega Mystery", "Missing Milkshake does not exists")
])
def test_invalid_delete_menu_item(restaurant, item, expected_error_message, default_restaurant_guide):
  rg = default_restaurant_guide
  with pytest.raises((MenuItemDoesNotExists, RestaurantDoesNotExists)) as e :
    rg.delete_menu_item(restaurant, item)
  assert str(e.value) == expected_error_message

