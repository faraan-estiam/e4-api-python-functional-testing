from RestaurantGuide.classes.RestaurantGuide import RestaurantGuide

def rg ():
  rg = RestaurantGuide()
  rg.add_restaurant("Default Diner")
  #Default Diner is empty on purpose (i din't find menu_items starting with 'D' :/ )
  rg.add_restaurant("Permanent Pizza")
  rg.add_menu_item("Permanent Pizza", "Pepperoni Pizza", "A pizza with pepperoni on it", 7.50)
  rg.add_menu_item("Permanent Pizza", "Pineapple Pizza", "A demon comming straight from hell", 666)
  rg.add_restaurant("Static Sushi")
  rg.add_menu_item("Static Sushi", "Salmon Sashimi", "Salmon (6 pieces)", 5.99)
  return rg