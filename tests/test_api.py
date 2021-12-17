import pytest
from api_testing.support.comments import *
from api_testing.support.config import *
from api_testing.support.headers import HEADERS
from api_testing.support.generated_data import NEW_COMMENT_PAYLOAD, NEW_DATA
from api_testing.support.schemes import COMMENTS_SCHEMA
from api_testing.support.static_data import PERSONAL_EMAIL
from api_testing.utils.verificators import *


@pytest.mark.positive
def test_read_all_has_personal_email():
    all_comments = get_all_comments(url=COMMENTS_URL)
    emails = search_emails(comments=all_comments)
    is_in(emails, PERSONAL_EMAIL)


@pytest.fixture(scope="function")
def setup():
    new_comment = create_unique_comment(payload=NEW_COMMENT_PAYLOAD, headers=HEADERS)
    is_created(new_comment)
    return new_comment


@pytest.mark.positive
def test_new_comment_can_be_added(setup):
    is_created(setup)


@pytest.mark.positive
def test_comment_can_be_deleted(setup):
    new_comment_in_request = get_all_comments(url=COMMENTS_URL)[0]
    id_url = f'{COMMENTS_URL}/{new_comment_in_request["id"]}'
    deletion_response = requests.delete(url=id_url)
    is_deleted(deletion_response)


@pytest.mark.positive
def test_comment_can_be_updated():
    update_response = requests.put(url=f'{COMMENTS_URL}/3', data=NEW_DATA, headers=HEADERS)
    is_updated(update_response)


@pytest.mark.positive
def test_comments_has_expected_scheme():
    all_comments = get_all_comments(url=COMMENTS_URL)
    validate(COMMENTS_SCHEMA, all_comments)


@pytest.mark.xfail
@pytest.mark.negative
def test_body_is_empty():
    all_comments = get_all_comments(url=COMMENTS_URL)
    is_value_empty(all_comments, 'body')






