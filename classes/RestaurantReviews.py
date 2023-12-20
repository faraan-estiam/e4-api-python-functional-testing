class RestaurantReviews:
    def __init__(self):
        self.reviews = {}
    
    def add_review(self, restaurant, comment, rating) :
        if rating<0 or rating>5 : raise ValueError(f"rating must be between 0 and 5 (given: {rating})")
        if restaurant in self.reviews.keys()  : raise ReviewAlreadyExists(restaurant+" already has a review")
        self.reviews[restaurant]={"comment":comment, "rating":rating}
        return self
    
    def get_review(self, restaurant) :
        if not restaurant in self.reviews.keys() : raise ReviewDoesNotExists(restaurant + " does not have review")
        return self.reviews[restaurant]

    def update_review(self, restaurant, comment, rating) :
        if not restaurant in self.reviews.keys() : raise ReviewDoesNotExists(restaurant + " does not have review")
        if rating<0 or rating>5 : raise ValueError(f"rating must be between 0 and 5 (given: {rating})")
        self.reviews[restaurant]={"comment":comment, "rating":rating}
        return self
    
class ReviewAlreadyExists (Exception) :
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class ReviewDoesNotExists (Exception) :
    def __init__(self, *args: object) -> None:
        super().__init__(*args)