import requests
import os
import pytest
from payloads import *

@pytest.mark.parametrize("payload, expected_status_code",[
    (NEW_BOOK_PAYLOAD, 201),
    (INVALID_PAYLOAD, 400), # this invalid payload has a rating value outside of expected range. expected range is [1,5] but the payload has 9.0 as its rating
    # TODO we can also tweak the payload to have other invalid parameters, for instance, missing a required parameter, or having an unexpected parameter, 
    # or the review is exceeding the max character number etc
])
def test_add_a_book(base_url, payload, expected_status_code):
    url = base_url + os.environ["ALL_BOOKS_PATH"]
    response = requests.post(url, json=payload)
    assert response.status_code == expected_status_code
    if expected_status_code == 201:
        json_res = response.json()
        assert json_res["id"] is not None, "the key 'id' is missing in the response"
        assert json_res["message"] == "Book added successfully.", "there is no 'message' in the response or the copy is not as expected"