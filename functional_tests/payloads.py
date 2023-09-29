NEW_BOOK_PAYLOAD = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "genre": "Novel",
    "reviews": [
      {
        "rating": 4.5,
        "comment": "A mesmerizing tale of ambition and love."
      }
    ]
  }

INVALID_PAYLOAD = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "genre": "Novel",
    "reviews": [
      {
        "rating": 9.0, # pretend the rating 9.0 is out of the allowed range
        "comment": "A mesmerizing tale of ambition and love."
      }
    ]
  }

BOOK_WITHOUT_REVIEW = {
    "id": 33,
    "title": "BOOK WITHOUT REVIEW",
    "author": "Infamous author",
    "genre": "Novel"
  }

BOOK_WITH_REVIEW = {
    "id": 55,
    "title": "BOOK WITH REVIEW",
    "author": "Famous author",
    "genre": "Novel",
    "reviews": [
      {
        "rating": 4.5,
        "comment": "A mesmerizing tale of ambition and love."
      }
    ]
  }