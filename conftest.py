from restaurant_reviews.tests.rr_conftest import rr
from RestaurantGuide.tests.RestaurantGuide_conftest import rg
import pytest

@pytest.fixture
def default_restaurant_reviews():
  return rr()

@pytest.fixture
def default_restaurant_guide():
  return rg()