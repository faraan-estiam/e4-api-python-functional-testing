class RestaurantGuide:
  def __init__(self) -> None:
    self.restaurants = {}

  def get_restaurant (self, restaurant: str):
    if restaurant not in self.restaurants.keys(): raise RestaurantDoesNotExists(f'{restaurant} does not exists')
    return self.restaurants[restaurant]

  #creates a restaurant with an empty menu (could add a review aswell)
  def add_restaurant (self, restaurant: str):
    if restaurant in self.restaurants.keys(): raise RestaurantAlreadyExists(f'{restaurant} already exists')
    self.restaurants[restaurant] = {"menu":{}}
    return self
  
  def remove_restaurant (self, restaurant: str):
    if restaurant not in self.restaurants.keys(): raise RestaurantDoesNotExists(f'{restaurant} does not exists')
    del self.restaurants[restaurant]
    return self
  
  def add_menu_item(self, restaurant: str, item: str, description: str, price: float) -> str:
    if price < 0 : raise ValueError('price must be positive')
    if restaurant not in self.restaurants.keys(): raise RestaurantDoesNotExists(f'{restaurant} does not exists')
    if item in self.restaurants[restaurant]['menu'].keys(): raise MenuItemAlreadyExists(f'{restaurant} already has {item} in the menu')
    self.restaurants[restaurant]["menu"][item] = {"description": description, "price": price}
    return f"{item} added to {restaurant}' menu" if restaurant[-1] == 's' else f"{item} added to {restaurant}'s menu"

  def get_menu(self, restaurant: str) -> list:
    if restaurant not in self.restaurants.keys(): raise RestaurantDoesNotExists(f'{restaurant} does not exists')
    menu = []
    for k, v in self.restaurants[restaurant]["menu"].items():
      menu.append({"name": k, "description": v["description"], "price": v["price"]})
    return menu
  
  def update_menu_item(self, restaurant: str, item: str, description: str, price: float) -> str:
    if price < 0 : raise ValueError('price must be positive')
    if restaurant not in self.restaurants.keys(): raise RestaurantDoesNotExists(f'{restaurant} does not exists')
    if item not in self.restaurants[restaurant]['menu'].keys(): raise MenuItemDoesNotExists(f'{restaurant} does not have {item} in the menu')
    self.restaurants[restaurant]["menu"][item] = {"description": description, "price": price}
    return f"{item} updated from {restaurant}' menu" if restaurant[-1] == 's' else f"{item} updated from {restaurant}'s menu"
  
  def delete_menu_item(self, restaurant: str, item: str) -> str:
    if restaurant not in self.restaurants.keys(): raise RestaurantDoesNotExists(f'{restaurant} does not exists')
    if item not in self.restaurants[restaurant]['menu'].keys(): raise MenuItemDoesNotExists(f'{restaurant} does not have {item} in the menu')
    del self.restaurants[restaurant]["menu"][item]
    return f"{item} removed from {restaurant}' menu" if restaurant[-1] == 's' else f"{item} removed from {restaurant}'s menu"

class RestaurantDoesNotExists(Exception):
  def __init__(self, *args: object) -> None:
    super().__init__(*args)

class RestaurantAlreadyExists(Exception):
  def __init__(self, *args: object) -> None:
    super().__init__(*args)

class MenuItemDoesNotExists(Exception):
  def __init__(self, *args: object) -> None:
    super().__init__(*args)

class MenuItemAlreadyExists(Exception):
  def __init__(self, *args: object) -> None:
    super().__init__(*args)
