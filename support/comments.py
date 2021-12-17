import requests
from api_testing.support.config import COMMENTS_URL


def search_emails(comments):
    emails = [email['email'] for email in comments]
    return emails


def get_all_comments(url):
    comments = requests.get(url).json()
    return comments


def create_unique_comment(payload, headers):
    response = requests.post(url=COMMENTS_URL, data=payload, headers=headers)
    return response






