#!/usr/bin/env python3
# -*- coding: utf8 -*-
#Simple flask app

from flask import Flask

app = Flask(__name__)

@app.route("/")
def about_me():
    me = {
        "first_name":"Paola",
        "last_name":"Cortes",
        "hobbies":"Paint and Tennis",
        "test": True

    }
    return me