# This repository contains example of API Testing framework


# How to install it

1) Clone the repository.

``git clone https://github.com/yefim-mironyuk/api_testing.git``

2) Install allure command line and add the allure folder installation into system environment variable: https://docs.qameta.io/allure/#_installing_a_commandline

3) Install pipenv for creation virtual environment and installation packages: https://pipenv.pypa.io/en/latest/  

``pip install --user pipenv``

4) Install dependencies:

``pipenv install``

# How to run it


Use: `` python -m pytest`` to run all tests.

**Parameters**

``-m negative`` to run negative tests.

``-m positive`` to run positive tests.

`` -n auto `` to run tests in parallel.

``--alluredir=report_allure/`` to create Allure report.

**Ex.**

``python -m pytest -m positive -n auto --alluredir=report_allure/`` runs positive tests in parallel and creates Allure report.

**Allure report**

Use: ``allure serve report_allure`` to open Allure report.

**Logging**

Logs are in ``debug.log``
