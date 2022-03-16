from flask import Flask, redirect, url_for, render_template, request, jsonify, flash
from App import app

HOST = "http://127.0.0.1:5000/"


@app.route('/')
def mainPage():  # put application's code here
    return render_template("mainPage.html")


if __name__ == '__main__':
    app.run()