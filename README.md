# Api-testing
This is an example of an api test framework.

## Requirements
- Design and write automated tests for CRUD operations on books.
- Prepare a brief explanation of your testing approach and considerations you made while writing these tests.
- (Optional) Discuss how you would organize load testing.

## Endpoints

* GET /books?genre={genre}&author={author}: Returns a filtered list of books.

  Request:

  Query Parameters:

  * genre (optional): Filter books by genre.

  * author (optional): Filter books by author.

 

* GET /books/{id}: Returns details of a specific book along with its reviews.

  Request:
  {id}: Unique identifier of the book.

  Response:

  <pre><code>
  {
    "id": "1",
    "title": "Moby Dick",
    "author": "Herman Melville",
    "genre": "Fiction",
    "reviews": [
      {
        "reviewId": "r1",
        "rating": 5,
        "comment": "An epic tale of man versus nature."
      },
      // ... Other reviews
    ]
  }
  </code></pre>
 

* POST /books: Add a new book and optionally include initial reviews.
  Request Body:
  <pre><code>
  {
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
  </code></pre>

  Response:
  <pre><code>
  {
    "id": "3",
    "message": "Book added successfully."
  }
  </code></pre>


* DELETE /books/{id}: Deletes a specific book. Only books without reviews can be deleted.


# Future work
* For the purpose of showing you my understanding and coding skills in API testing, I used my favorite language Python for this exercise. I understand Gainbridge uses javascript/typescript extensively for both front and backend development. Also it was hard to find information on k6 in Python. In the future, I need to improve my js skills on the job. I combined Python API testing and Javascript load testing in one repo, this is not a ideal blending. I'm aware of that. 

* Deserialize json object into a customized Book class. This would make assertion/verificaiton more robust and less error prone. 

  Currently in the test case `test_book_detail`. We can do assertions like: ` assert json_res["author"] == "ex_author"`. If we have the customized Book class in place, we can do something like `assert deserizlized_json.author == "ex_author"`. The benefit of having a customized Book class is: If at any point, the attribute name of `author` is updated, we only need to change the attribute name in the Book class file, instead of updating it in all the files that use it. In practice, [here](https://levelup.gitconnected.com/how-to-deserialize-json-to-custom-class-objects-in-python-d8b92949cd3b) is a blog detailing how we can go about deserialization.  

* We should test the authentication and authorization of the APIs. For instance, the get endpoints prob don't need it. But for delete and post endpoints, we should only allow authorized and authenciated users to access it. 

* If these API endpoints are serving websites, we can also add a test case for cookies.

* For now, I have a javascript to do some basic load testing against the GET endpoint with a specified RPS and SLA. I don't have a full understanding of k6 yet, but am willing to learn as I go. [This blog](https://k6.io/blog/building-a-ui-for-the-k6-load-testing-tool/) seems to be an interesting read to build a in-house load testing dashboard. 

* In terms of organizaiton for load testing, we can resort to the testing pyramid and run load testing on different levels(if it's a micro-service architecture): component level, integration level and end-to-end level. Also we need run load testing against each API endpoint. 


## Disclaimer
This exercise might have typos through the repo just because I don't have a live service to run the tests against. 