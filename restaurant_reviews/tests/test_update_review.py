from classes.RestaurantReviews import RestaurantReviews, ReviewDoesNotExists
import pytest

#valid
@pytest.mark.parametrize("restaurant, comment, rating, expected_output",[
    ("Default Diner", 'Meh burgers', 3, ({'comment': 'Meh burgers', 'rating': 3})),
    ("Permanent Pizza", 'Great pizzas for developers', 4, ({'comment': 'Great pizzas for developers', 'rating': 4})),
    ("Static Sushi", "It's supposed to be raw", 4, ({"comment": "It's supposed to be raw", "rating": 4}))
])

def test_update_valid_review (restaurant, comment, rating, expected_output, default_restaurant_reviews) :
    rr = default_restaurant_reviews
    rr.update_review(restaurant, comment, rating)
    assert rr.reviews[restaurant] == expected_output

def test_update_invalid_review () :
    with pytest.raises(ReviewDoesNotExists) as e : #review does not exists
        rr = RestaurantReviews()
        rr.update_review("Cafe Mocha", "Worst coffe ever!", 0)
    assert str(e.value) == "Cafe Mocha does not have review"
    with pytest.raises(ValueError) as e: #invalid rating
        rr = RestaurantReviews()
        rr.reviews["Cafe Mocha"] = {'comment':"Great coffee and pastries", 'rating':5}
        rr.update_review("Cafe Mocha", "Worst coffe ever!", -99)
    assert str(e.value) == "rating must be between 0 and 5 (given: -99)"