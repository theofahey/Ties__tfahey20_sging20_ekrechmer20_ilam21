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
    num = random.randrange(0,20)
    num2 = random.randrange(0,20)
    while(num2 == num):
        num2 = random.randrange(0,20)
    title1 = data['items'][num]['title']
    hist1 = data['items'][num]['details']
    title2 = data['items'][num2]['title']
    hist2 = data['items'][num]['details']
    return render_template("fbi.html", kanye = x["quote"], name = title1, crim = hist1,name2 = title2, crim2 = hist2)
def dogstory():
    url = "https://dog.ceo/api/breeds/list/all"
    w = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    r = urllib.request.urlopen(w).read()
    x = json.loads(r)
    breedlist = x['message']
    totalbreed = [""]*4
    breedpics = [""]*4
    for x in range(4):
        res = key, val = random.choice(list(breedlist.items()))
        subreed1 = ""
        if len(res[1]):
            num = len(res[1]);
            subreed1 = res[1][random.randrange(0,num)]


        familybreed1 = res[0]

        totalbreed[x] = subreed1 + " " + familybreed1

        breedpics[x] = getpics(subreed1, familybreed1)

    return render_template("dog.html", breed1 = totalbreed[0], breed2 = totalbreed[1], breed3 = totalbreed[2], breed4 = totalbreed[3],pic1 = breedpics[0] )
def getpics(subreed, familybreed):
    if (subreed != ""):
        picurl = "https://dog.ceo/api/breed/" + familybreed + "/"+ subreed +  "/images"
    else:
        picurl = picurl = "https://dog.ceo/api/breed/" + familybreed + "/images"
    requesting = urllib.request.Request(picurl,headers={'User-Agent': 'Mozilla/5.0'})
    reading = urllib.request.urlopen(requesting).read()
    x = json.loads(reading)
    flist = x['message']
    finalurl = random.choice(flist);
    return finalurl

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
