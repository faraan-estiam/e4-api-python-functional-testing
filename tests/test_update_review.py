from classes.RestaurantReviews import RestaurantReviews, ReviewDoesNotExists
import pytest

def test_update_valid_review () :
    rr = RestaurantReviews()
    rr.reviews["Cafe Mocha"] = {'comment':"Great coffee and pastries", 'rating':5}
    rr.update_review("Cafe Mocha", "Worst coffe ever!", 0)
    assert rr.reviews["Cafe Mocha"] == {"comment": "Worst coffe ever!", "rating": 0}

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