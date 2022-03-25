from flask import Flask, redirect, url_for, render_template, request, jsonify, flash
from App import app
from Database import mysql
from Filter import *
from Login import *
from Profile import *
from ProfessionCategory import *
from RegisteredCompany import *
from UnregisteredCompany import *
from Engineer import *
from Search import *
from Posts import *
from PostHistory import *
from Database import *
import pytest
import pytest_cov
import sqlite3
from unittest.mock import MagicMock


# fixture for running Flask
@pytest.fixture()
def appTest():
    testMyApp = Flask(__name__)
    testMyApp.config.update({
        "TESTING": True,
    })
    # other setup can go here
    yield testMyApp
    # clean up / reset resources here


@pytest.fixture
def client(appTest):
    return appTest.test_client()


@pytest.fixture
def runner(appTest):
    return appTest.test_cli_runner()


# create fixture for database session
@pytest.fixture
def session():
    connection = sqlite3.connect(':memory:')
    db_session = connection.cursor()

    yield db_session
    db_session.close()


@pytest.fixture
def setupDB(session):
    session.execute('''CREATE TABLE Users
                          (Username varchar(255) NOT NULL, Password varchar(255), PRIMARY KEY (Username))''')  # 3
    session.execute('INSERT INTO Users VALUES ("chad", "holst")')
    session.connection.commit()


# Login class tests:
# @pytest.mark.usefixtures("setupDB")
# def test_validate(session):
#     myLogin = Login("chad", "holst", session)
#     expected = myLogin.validate()
#     actual = [("chad", "holst"), ]
#     print(expected, actual)
#     assert expected == actual, "input should be valid and produce list of tuples"


# Filter class test:
def test_professionType():
    myFilter = Filter()
    professionFilter = "Engineer"
    myListOfTuples = [("I", "Should", "Be", "Removed", "Since", "Index", "7 is", "Not Engineer"),
                      ("I", "Should", "Be", "Stay", "Since", "Index", "7 is", "Engineer")]
    expected = [("I", "Should", "Be", "Stay", "Since", "Index", "7 is", "Engineer"), ]
    actual = myFilter.professionType(myListOfTuples, professionFilter)
    assert expected == actual, "tuple should be removed if profession column from QUESTION_POSTS is different than professionFilter"

# def test_new_account_add_company():
#     newAccount = Profile()
#     username = "NewUser"
#     expected = "NewUser"
#     newAccount.createProfile(username)
#     actual2 = newAccount.getProfile(username)

# Engineer class test
def test_engineer_degree():
    newEngineer = Engineer("Software engineering", "Canada", "80", "21")
    actual = newEngineer.degree
    expected = "Software engineering"
    assert expected == actual

# Post test
def test_posting():
    newPost = Posts("chad")    
    newPost.

