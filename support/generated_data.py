from json import dumps
from api_testing.utils.fake_data_generator import *

postId = get_fake_id()
fake_id = get_fake_id()
name = get_fake_name()
email = get_fake_email()
body = get_fake_body()

NEW_COMMENT_PAYLOAD = dumps({
    "postId": postId,
    "id": fake_id,
    "name": name,
    "email": email,
    "body": body,
})

NEW_DATA = dumps({
    "postId": f'{postId} NEW',
    "id": f'{fake_id} NEW',
    "name": f'{name} NEW',
    "email": f'{email} NEW',
    "body": f'{body} NEW',
})


