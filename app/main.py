import sqlite3
from os import urandom
from flask import render_template, redirect, request, url_for, session, Flask
import urllib.request
from urllib.request import urlopen
import json
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def start():
    return render_template("index.html");

@app.route("/FBI", methods = ['GET', 'POST'])
def kanye_east():
    url = "https://api.kanye.rest"
    w = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    r = urllib.request.urlopen(w).read()
    x = json.loads(r)
    return render_template("fbi.html", kanye = x["quote"])

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
