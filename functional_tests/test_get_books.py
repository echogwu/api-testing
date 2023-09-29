import requests
import os
import pytest
from payloads import *


@pytest.fixture(scope="module", autouse=True)
def setup():
    # insert books with info from BOOK_WITH_REVIEW and BOOK_WITHOUT_REVIEW from ./constants/ file
    yield
    # delete the books from the db


# the test below only verify the endpoint is reachable and the numbers of books is correct
# But we can further verify if the book has the correct information. e.g. verify the author, publication year, title, etc
@pytest.mark.parametrize("genre, author, return_books",[
    ("valid_genre", "unvalid_author", False),
    ("invalid_genre", "valid_author", False),
    # TODO below, depending on how many books we seeded in the setup, the number of returned books might differ
    ("valid_genre", "valid_author", True), 
    ("invalid_genre", "invalid_author", False),
])
def test_get_all_books(base_url, genre, author, return_books):
    url = base_url + os.environ["ALL_BOOKS_PATH"]
    response = requests.get(url, params={"genre": {genre}, "author": {author}})
    # TODO check the server's logic, it might return non-200 when there is no book 
    # that is of the specified genre and author
    assert response.status_code == 200, f"expecting status code 200 but got {response.status_code}"
    assert bool(len(response.json())) == return_books, f"It should {'' if return_books else 'NOT'} return books" 

VALID_ID = 3
INVALID_ID = 5

# the test below only verify the endpoint returns the expected status code
# But we can further verify if the book has the correct information. e.g. verify the author, publication year, title, etc
@pytest.mark.parametrize("id, expected_status_code, expected_book_number",[
    (VALID_ID, 200, 1),
    (INVALID_ID, 404, 0),
])
def test_get_one_book(base_url, id, expected_status_code, expected_book_number):
    url = base_url + os.environ["ONE_BOOK_PATH"]
    response = requests.get(url.format(id))
    assert response.status_code == expected_status_code, f"expecting status code {expected_status_code} but got {response.status_code}"
    json_res = response.json()
    assert len(json_res) == expected_book_number, f"expecting to get {expected_book_number} book(s) but got {len(json_res)}"
    # TODO we can go ahead and verify the details of the book. e.g.
    assert json_res["author"] == "ex_author", f"expecting the author to be 'ex_author' book(s) it was {json_res['author']}"
    # TODO ideally, the string "ex_author" should be defined as a constant either in this file or variable files like ./env/other.yml







