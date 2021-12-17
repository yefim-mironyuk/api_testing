from faker import Faker
from random import randint


def get_fake_name():
    fake_name = Faker().name()
    return fake_name


def get_fake_body():
    fake_body = Faker().text()
    return fake_body


def get_fake_id():
    fake_id = randint(10, 20)
    return fake_id


def get_fake_email():
    fake_email = Faker().ascii_email()
    return fake_email
