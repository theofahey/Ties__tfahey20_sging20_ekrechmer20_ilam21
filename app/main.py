import sqlite3
from os import urandom
from flask import render_template, redirect, request, url_for, session, Flask
import urllib.request
from urllib.request import urlopen
import json
import random
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def start():
    return render_template("index.html");

@app.route("/FBI-input", methods = ['GET', 'POST'])
def kanye_east_fillin():
    return render_template("madlibtemplate.html")

@app.route("/FBI", methods = ['GET', 'POST'])
def kanye_east():
    url = "https://api.kanye.rest"
    #Opens From Browser in order to ensure not being blocked.
    w = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    r = urllib.request.urlopen(w).read()
    x = json.loads(r)
    url2 = "https://api.fbi.gov/wanted/v1/list"
    w2 = urllib.request.Request(url2,headers={'User-Agent': 'Mozilla/5.0'})
    r2 = urllib.request.urlopen(w2).read()
    data = json.loads(r2)
    length = data['total']
    print(data['items'][random.randrange(0,20)]['title'])
    return render_template("fbi.html", kanye = x["quote"])

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
