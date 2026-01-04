'''
    Q2 
    . Create a class Books  with the following attributes:
    • title
    • author
    • list of reviews
    And add methods to:
    • add a new review
    • count reviews
    • display all reviews
'''

class Book:
    def __init__(self,tittle,author):
        self.tittle=tittle
        self.author=author
        self.reviews=[]

    def add_reviews(self,review):
        self.reviews.append(review)
        print("Review Added!")
    
    def count_reviews(self):
        print("Total number of review is : ",len(self.reviews))

    def display_all_review(self):
        print(self.reviews)

b1=Book("Think & Grow Rich","Napolean Hill")
b1.add_reviews("Awesome book")
b1.count_reviews()
b1.display_all_review()
b1.add_reviews("Must read this book")
b1.count_reviews()
b1.display_all_review()
        