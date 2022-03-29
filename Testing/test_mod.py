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

# Filter class test:
# Test Case: 1
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

# Test Case: 2
def test_homePage():
    response=tester.get("/")

    assert response.status_code == 302, "Page should redirect"

# Test Case: 3
def test_mainPage():
    response=tester.get("/unregisteredMain")

    assert response.status_code == 200, "Page should exist and load without errors"

# Test Case: 4
def test_registeredMain():
    response=tester.get("/registeredMain/test1")

    assert response.status_code == 200, "Page should exist and load without errors"
    
# Test Case: 5
def test_query():
    response=tester.get("/query=a")

    assert response.status_code == 200, "Page should exist and load without errors"

# Test Case: 6
def test_login():
    response=tester.get("/login")

    assert response.status_code == 200, "Page should exist and load without errors"

# Test Case: 7
def test_signUp():
    response=tester.get("/createProfile/test1")

    assert response.status_code == 200, "Page should exist and load without errors"

# Test Case: 8
def test_createProfile():
    response=tester.get("/signUp")

    assert response.status_code == 200, "Page should exist and load without errors"

# Test Case: 9
def test_viewProfile():
    response=tester.get("/profile/view/test1")

    assert response.status_code == 200, "Page should exist and load without errors"

# Test Case: 10
def test_editProfile():
    response=tester.get("/profile/edit/test1")

    assert response.status_code == 200, "Page should exist and load without errors"

# Test Case: 11
def test_questionHistory():
    response=tester.get("/questions/test1")

    assert response.status_code == 200, "Page should exist and load without errors"

# Test Case: 12
def test_answerHistory():
    response=tester.get("/answers/test1")

    assert response.status_code == 200, "Page should exist and load without errors"

# Test Case: 13
def test_postQuestion():
    response=tester.get("/post/question")

    assert response.status_code == 200, "Page should exist and load without errors"

# Test Case: 14
def test_viewPost():
    response=tester.get("/post/view/1")

    assert response.status_code == 200, "Page should exist and load without errors"

# Test Case: 15
def test_addCompany():
    response=tester.get("/addCompany/test1")

    assert response.status_code == 200, "Page should exist and load without errors"

# Test Case: 16
def test_fakePage():
    response=tester.get("/somepageurl")

    assert response.status_code == 404, "Page should not exist"
    

# Test Case: 17
def test_loginFormValid():
    response=tester.post("/login", data={
        "username": "dmah",
        "password": "dmah"
    })

    assert response.status_code==302, "Login should be valid and redirect"

# Test Case: 18
def test_loginFormValid():
    response=tester.post("/login", data={
        "username": "invalidUser",
        "password": "invalidPass"
    })

    assert response.status_code==200, "Login should be invalid and not redirect"

# tests for sign up functionality:
# Test Case: 19
def test_signUpDoesNotExist():
    response = tester.post("/signUp", data={
        "username": "newUser",
        "password": "newPassword"
    })
    assert response.status_code == 302, "User should provide new username that does not exist to redirect after sign up"

# requires username "chad" in USERS
# Test Case: 20
def test_signUpDoesExist():
    response = tester.post("/signUp", data={
        "username": "chad",
        "password": "holst"
    })
    assert response.status_code == 200, "User provided username that already exists so sign up failed"

# requires username "chad" in USERS
# test for create profile functionality:
# Test Case: 21
def test_createProfileSuccessfulRedirect():
    response = tester.post("/createProfile/chad", data={
                           "fName": "chad",
                           "mNames": "daniel",
                           "lName": "holst",
                           "email": "fake@email.com",
                           "curComp": "DGC",
                           "prof": "Engineer",
                           "skills": "machinery design",
                           "desc": "hands on",
                           "proj": "designing engine"
                           })
    assert response.status_code == 302, "User should provide all input fields to complete profile and redirect"
    
# requires username of "chad" in USERS:
# test for editing profile functionality:
# Test Case: 22
def test_editProfile():
    response = tester.post("/profile/edit/chad", data={
        "fName": "chad",
        "mNames": "daniel",
        "lName": "holst",
        "email": "editMyFakeEmail@email.com",
        "curComp": "DGC",
        "prof": "Engineer",
        "skills": "circuit building",
        "desc": "hands on",
        "proj": "designing electrical grid"
    })
    assert response.status_code == 302, "User should provide all input fields to complete profile and redirect"

# requires username "chad" in USERS
# test for add company functionality:
# Test Case: 23
def test_addCompanySuccessful():
    response = tester.post("/addCompany/chad", data={
                           "company": "Apple",
                           "position": "Software Engineer",
                           "start": "April,2005",
                           "end": "June, 2022"
                           })
    assert response.status_code == 200, "User should provide all data in input fields for adding company info to profile"

# requires post with similar search bar input, "testSearch"
# tests for search post functionality:
# Test Case: 24
def test_searchForQueryRoute():
    response = tester.post("/query=test", data={
                           "basicSearch": "testSearch",
                           })

    assert response.status_code == 302, "Question search should redirect to search query route"

# requires post with similar search bar input, "testSearch"
# Test Case: 25
def test_questionPostSearch():
    response = tester.post("/post/question/", data={
                           "basicSearch": "testSearch"
                           })
    assert response.status_code == 302, "Question search should redirect to search query route"

# requires post with similar search bar input, "testSearch" and post with qid of 1
# Test Case: 26
def test_viewPostSearch():
    response = tester.post("/post/view/1", data={
                           "basicSearch": "testSearch"
                           })
    assert response.status_code == 302, "Question search should redirect to search query route"

# creating new question and adding it to local database
# Test Case: 27
def test_questionForm():
    tester.post("/login", data={
        "username": "dmah",
        "password": "dmah"
    })

    response=tester.post("/post/question", data={
        "title": "Sample Title",
        "ques": "Sample Body",
        "prof": "Software",
        "tags": None
    })

    assert response.status_code == 302, "After question post, user should be redirected"

# creating answer to existing question and storing it in database
# Test Case: 28
def test_answerForm():
    tester.post("/login", data={
        "username": "dmah",
        "password": "dmah"
    })

    response=tester.post("/post/view/1", data={
        "ans": "Sample answer"
    })

    assert response.status_code == 200, "After question post, user should be redirected"
