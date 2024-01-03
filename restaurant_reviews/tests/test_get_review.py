from classes.RestaurantReviews import RestaurantReviews, ReviewDoesNotExists
import pytest

#valid
@pytest.mark.parametrize("restaurant, expected_output",[
    ("Default Diner", ({'comment': 'Great burgers', 'rating': 5})),
    ("Permanent Pizza", ({'comment': 'Best pizzas for developers', 'rating': 5})),
    ("Static Sushi", ({"comment": "Fish was raw !", "rating": 1}))
])

def test_get_valid_review (restaurant, expected_output, default_restaurant_reviews) :
    rr = default_restaurant_reviews
    assert rr.get_review(restaurant) == expected_output

#invalid
@pytest.mark.parametrize("restaurant, expected_output",[
    ("Cafe Mocha", "Cafe Mocha does not have review"),
    ("Best Burgers", "Best Burgers does not have review")
])

def test_get_invalid_review (restaurant, expected_output, default_restaurant_reviews) :
    with pytest.raises(ReviewDoesNotExists) as e: #review does not exists
        rr = default_restaurant_reviews
        rr.get_review(restaurant)
    assert str(e.value) == expected_output