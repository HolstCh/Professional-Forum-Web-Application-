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
    session.execute('''CREATE TABLE USERS
                          (username varchar(255) NOT NULL, password varchar(255), PRIMARY KEY (username))''')  # 3
    session.execute('INSERT INTO USERS VALUES ("chad", "holst")')
    session.connection.commit()


@pytest.mark.usefixtures("setupDB")
def test_validate(session):
    myLogin = Login("chad", "holst", session)
    expected = myLogin.validate()
    actual = [("chad", "holst"), ]
    print(expected, actual)
    assert expected == actual
