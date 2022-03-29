# cd "C:\Users\coolp\Documents\Dylan\School\Y3 - 2022 WINTER\SENG 401 - Software Architecture\Project\Forum_Project_SENG_401"
# python -m pytest test_mod.py

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
import pytest
import sqlite3
import mysql.connector
import unittest
from unittest.mock import MagicMock

#dbc=mysql.connector.connect(
#    host="localhost",
#    user="root",
#    password="draGGun.!382",
#    database="seng401"
#)

#cursor=dbc.cursor()

#@pytest.fixture()
#def appTest():
#    testMyApp = Flask(__name__)
#    testMyApp.config.update({ "TESTING": True })
#    yield testMyApp

#@pytest.fixture
#def client(appTest):
#    return appTest.test_client()

#@pytest.fixture
#def runner(appTest):
#    return appTest.test_cli_runner()

# Login class tests:
#def test_validate():
#    #from Login import Login

#    myLogin = Login("chad", "holst")
#    actual = myLogin.validate()
#    expected = [("chad", "holst"), ]
#    print(expected, actual)
#    assert expected == actual, "input should be valid and produce list of tuples"


# Filter class test:
def test_professionType():
    from Filter import Filter

    myFilter = Filter()
    professionFilter = "Engineer"
    myListOfTuples = [("I", "Should", "Be", "Removed", "Since", "Index", "7 is", "Not Engineer"),
                      ("I", "Should", "Be", "Stay", "Since", "Index", "7 is", "Engineer")]
    expected = [("I", "Should", "Be", "Stay", "Since", "Index", "7 is", "Engineer"), ]
    actual = myFilter.professionType(myListOfTuples, professionFilter)
    assert expected == actual, "tuple should be removed if profession column from QUESTION_POSTS is different than professionFilter"


tester=app.test_client()    # For route and HTML form tests

def test_homePage(self):
    response=self.tester.get("/")

    assert response.status_code == 302, "Page should redirect"

def test_mainPage(self):
    response=self.tester.get("/unregisteredMain")

    assert response.status_code == 200, "Page should exist and load without errors"

def test_registeredMain(self):
    response=self.tester.get("/registeredMain/test1")

    assert response.status_code == 200, "Page should exist and load without errors"

def test_query(self):
    response=self.tester.get("/query=a")

    assert response.status_code == 200, "Page should exist and load without errors"

def test_login(self):
    response=self.tester.get("/login")

    assert response.status_code == 200, "Page should exist and load without errors"

def test_signUp(self):
    response=self.tester.get("/createProfile/test1")

    assert response.status_code == 200, "Page should exist and load without errors"

def test_createProfile(self):
    response=self.tester.get("/signUp")

    assert response.status_code == 200, "Page should exist and load without errors"

def test_viewProfile(self):
    response=self.tester.get("/profile/view/test1")

    assert response.status_code == 200, "Page should exist and load without errors"

def test_editProfile(self):
    response=self.tester.get("/profile/edit/test1")

    assert response.status_code == 200, "Page should exist and load without errors"

def test_questionHistory(self):
    response=self.tester.get("/questions/test1")

    assert response.status_code == 200, "Page should exist and load without errors"

def test_answerHistory(self):
    response=self.tester.get("/answers/test1")

    assert response.status_code == 200, "Page should exist and load without errors"

def test_postQuestion(self):
    response=self.tester.get("/post/question")

    assert response.status_code == 200, "Page should exist and load without errors"

def test_viewPost(self):
    response=self.tester.get("/post/view/1")

    assert response.status_code == 200, "Page should exist and load without errors"

def test_addCompany(self):
    response=self.tester.get("/addCompany/test1")

    assert response.status_code == 200, "Page should exist and load without errors"

def test_fakePage(self):
    response=self.tester.get("/somepageurl")

    assert response.status_code == 404, "Page should not exist"

def test_loginFormValid():
    response=tester.post("/login", data={
        "username": "dmah",
        "password": "dmah"
    })

    assert response.status_code==302, "Login should be valid and redirect"

def test_loginFormValid():
    response=tester.post("/login", data={
        "username": "invalidUser",
        "password": "invalidPass"
    })

    assert response.status_code==200, "Login should be invalid and not redirect"        
