import requests
from loguru import logger
from assertpy import assert_that, soft_assertions
from cerberus import validator, Validator
from .logging import Logger

Logger()

def is_in(object1, object2):
    logger.debug(f'Checking is "{object1}" in "{object2}"...')
    try:
        assert_that(object1).contains(object2)
    except AssertionError:
        logger.error(f'Error {object1} NOT IN {object2}')


def is_created(response):
    logger.debug(f'Checking is {response.status_code} matches {requests.codes.created}')
    try:
        assert_that(response.status_code).is_equal_to(requests.codes.created)
    except AssertionError:
        logger.error(f'{response.status_code} does not match expected {requests.codes.created}')


def is_deleted(response):
    logger.debug(f'Checking is {response.status_code} matches {requests.codes.ok}')
    try:
        assert_that(response.status_code).is_equal_to(requests.codes.ok)
    except AssertionError:
        logger.error(f'{response.status_code} does not match expected {requests.codes.created}')


def is_updated(response):
    logger.debug(f'Checking is {response.status_code} matches {requests.codes.ok}')
    try:
        assert_that(response.status_code).is_equal_to(requests.codes.ok)
    except AssertionError:
        logger.error(f'{response.status_code} does not match expected {requests.codes.ok}')


def is_true(object1):
    assert_that(object1, description=validator.errors).is_true()


def validate(schema, objects):
    logger.debug(f'Checking is {objects} follows schema {schema}')
    try:
        validator = Validator(schema, require_all=True)
        with soft_assertions():
            for object1 in objects:
                is_valid = validator.validate(object1)
                is_true(is_valid)
    except Exception:
        logger.error(f'{objects} is not follows expected schema {schema}')

def is_value_empty(response, key):
    logger.debug(f'Checking is {key} empty')
    try:
        for val in response:
            assert_that([val]).extracting(key).is_empty()
    except AssertionError:
        logger.error(f'{key} is not empty!')
