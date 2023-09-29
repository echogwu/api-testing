import requests
import os
import pytest
from payloads import *

INVALID_ID = 5

@pytest.fixture(scope="module", autouse=True)
def setup():
    # insert books with info from BOOK_WITH_REVIEW and BOOK_WITHOUT_REVIEW from ./constants/ file
    yield
    # delete the books from the db

@pytest.mark.parametrize("id, expected_status_code",[
    (BOOK_WITHOUT_REVIEW["id"], 200)
    (BOOK_WITH_REVIEW["id"], 500),
    (INVALID_ID, 404), # this id doesn't belong to any books
])
def test_delete_a_book(base_url, id, expected_status_code):
    url = base_url + os.environ["ONE_BOOK_PATH"]
    response = requests.delete(url.format(id))
    assert response.status_code == expected_status_code, f"expecting status code {expected_status_code} but got {response.status_code}"