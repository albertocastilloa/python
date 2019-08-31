#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 11:18:48 2019

@author: albertocastillo
"""

from flask import Flask, jsonify

app = Flask(__name__)

#3 Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'home' page...")
    return "Welcome to my 'Home'page!"

@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "<a href='huevos.com'>Welcome to my 'About page'</a> \n I'm Alberto and Flesk is for pussies"

@app.route("/contact")
def contact():
    print("Server received request for 'Contact' page...")
    return("Do not even dare to contact me... pussy")

my_dict = {'Hello' : 'World',
           'XXX': 'SSSSS'}

@app.route("/normal")
def normal():
    print("Server received request for 'Normal' page...")
    return my_dict

@app.route("/jsonified")
def jsonified():
    return jsonify(my_dict)


if __name__ == "__main__":
    app.run(debug=True)