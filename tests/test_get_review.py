from classes.RestaurantReviews import RestaurantReviews, ReviewDoesNotExists
import pytest

def test_get_valid_review () :
    rr = RestaurantReviews()
    rr.reviews["Cafe Mocha"] = {'comment':"Great coffee and pastries", 'rating':5}
    assert rr.get_review("Cafe Mocha") == {'comment':"Great coffee and pastries", 'rating':5}

def test_get_invalid_review () :
    with pytest.raises(ReviewDoesNotExists) as e:
        rr = RestaurantReviews()
        rr.get_review("Cafe Mocha")
    assert str(e.value) == "Cafe Mocha does not have review"