import sqlite3
from os import urandom
from flask import render_template, redirect, request, url_for, session, Flask
import urllib.request
from urllib.request import urlopen
import json
import random
import os
from jinja2 import Template
from database import Usernamepassword, MadlibTable


app = Flask(__name__)
app.secret_key = os.urandom(32)

#initializing db
db_file = "database.db"
userpass = Usernamepassword(db_file, "password")
madlibTable = MadlibTable(db_file, "madlib")

####################################


def replace(story, words):
    '''
    Input str story with # in place of blanks and str[] words
    Replaces # with words
    Returns the story with replaces words
    '''
    output = ""
    for x in story:
        if x == "#":
            if len(words[0]) != 0:
                output += words.pop(0)
            else:
                output += "____"
                words.pop(0)
        else:
            output += x

    return output


@app.route("/", methods=['GET', 'POST'])
def start():
    return render_template("index.html",
                            isLoggedIn = session.get("username") is not None);

@app.route("/FBI-input", methods = ['GET', 'POST'])
def kanye_east_fillin():
    return render_template("FBIfill.html")

@app.route("/signup")
def signup():
    username= request.args['username']
    password= request.args['password']
    passauth= request.args['passauth']
    if (username=="" or password==""):
        return render_template('signup.html', syntaxerror="Cannot submit blank username or password")
    elif (password!=passauth):
        return render_template('signup.html', syntaxerror="Passwords must match")
    elif not userpass.userExists(username):
        userpass.insert(username, password) # committing actions to database must be done every time you commit a command
        session["username"]=username
        return redirect("/loggedin")
    else:
        return render_template('signup.html', syntaxerror = "This username already exists")



@app.route("/login")
def login():
    username= request.args['username']
    password= request.args['password']

    if (username=="" or password==""):
        return render_template('index.html', error="Cannot submit blank username or password")
    elif not userpass.userExists(username):
        return render_template('index.html', error="Username does not exist")
    elif not userpass.passMatch(username, password):
        return render_template('index.html', error = "Incorrect password")
    else:
        session["username"] = username
        return redirect('/loggedin')

@app.route("/signupdisplay")
def _dispsignuppage():
    if (session.get("username") is not None):
        # if there's an existing session, shows welcome page
        return redirect ("/")
    if ("username" != None):
        return render_template( 'signup.html' )



@app.route("/loggedin")
def loggedin(): # does not show info in URL, shows /loggedin instead
    return redirect("/")

@app.route("/logout")
def logout():
    #if "username" in session:
    session["username"] = None
    session.pop("username", None)
    return redirect('/')

@app.route("/create", methods=["GET", "POST"])
def create():
    if session.get("username") is None:
        return redirect("/")

    if request.method == "GET":
        return render_template('create.html')
    else:
        topic = request.form['topic']
        username = session.get("username")
        title = request.form['title']
        post = request.form['postcontent']

        if topic=="empty" or title=="" or post=="":
            return render_template('create.html', error="Must have a topic, title, and content")
        else:
            blog.insert(username, title, post, topic)
            return view(topic, title, post, blog.getNewestId())

@app.route("/FBI", methods = ['GET', 'POST'])
def kanye_east():
    document_path = os.getcwd()
    if "app" in document_path:
        document_path +='/fbiStory.txt'
    else:
        document_path +='/app/fbiStory.txt'
    with open(document_path, 'r') as f:
        lines = f.read()
        f.close()
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
    # not sure if api is configured correctly
    title1 = data['items'][num]['title']
    hist1 = data['items'][num]['details']
    title2 = data['items'][num2]['title']
    hist2 = data['items'][num2]['details']
    words = []
    if request.method == "POST":
        for b in range(1,13):
            words.append(request.form[str(b)])
    words.insert(0, title1.title())
    words.insert(2, x["quote"])
    #words.insert(7, words[3])
    words.insert(12, title2.title())
    # print(words)
    lines = replace(lines, words)

    return render_template("fbi.html",  lines = lines, isFilled=True, isLoggedIn=session.get("username") is not None)


@app.route("/viewPosts")
def viewPosts():
    if session.get("username") is None:
        return redirect("/")

    return render_template(
        "viewposts.html",
        username=session.get("username"),
        posts= [[x[0],x[1],x[2].replace("\"",""), x[3].replace("\"","")] for x in madlibTable.fetchAllByUsername(session.get("username"))]
        )

@app.route("/save", methods=["GET", "POST"])
def save():
    if request.method == "GET" or session.get("username") is None:
        return redirect("/")

    madlibTable.makeEntry(
        session.get("username"),
        request.form.get("prompt"),
        request.form.get("content"))

    return render_template("savedPost.html")


@app.route("/Dog-input", methods=['GET', 'POST'])
def dogstory_fillin():
    return render_template("dogfill.html");

@app.route("/Dog", methods = ['GET', 'POST'])
def dogstory():
    document_path = os.getcwd()
    if "app" in document_path:
        document_path +='/dogStory.txt'
    else:
        document_path +='/app/dogStory.txt'
    with open(document_path, 'r') as f:
        lines = f.read()
        f.close()
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

    words = []

    if request.method == "POST":
        for b in range(1,13):
            words.append(request.form[str(b)])

    words.insert(0, totalbreed[0])
    words.insert(3, totalbreed[1])
    words.insert(4, totalbreed[2])
    words.insert(5, totalbreed[3])
    lines = replace(lines, words)
    print(totalbreed)
    return render_template("dog.html", lines = lines, pic1 = breedpics[0], pic2=breedpics[1], pic3=breedpics[2], pic4=breedpics[3],isFilled=True, isLoggedIn=session.get("username") is not None)


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





@app.route("/Funny-input", methods=['GET', 'POST'])
def funny_fillin():
    return render_template("funnyfill.html")


@app.route("/Funny", methods = ['GET', 'POST'])
def funny():

    document_path = os.getcwd()
    if "app" in document_path:
        document_path +='/funnyStory.txt'
    else:
        document_path +='/app/funnyStory.txt'
    with open(document_path, 'r') as f:
        lines = f.read()
        f.close()

    list1 = [""] * 3
    for i in range(3):
        url = "https://v2.jokeapi.dev/joke/Programming,Spooky,Christmas?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
        w = urllib.request.Request(url,headers={'User-Agent': 'Mozilla/5.0'})
        r = urllib.request.urlopen(w).read()
        x = json.loads(r)
        if "joke" in x:
            list1[i] = x['joke']
        else:
            list1[i] = x['setup'] + " ... " + x['delivery']

    words = []

    if request.method == "POST":
        for b in range(1,17):
            words.append(request.form[str(b)])

    words.insert(1, list1[0])
    words.insert(5, list1[1])
    words.insert(15, list1[2])
    # print(list1[15])
    lines = replace(lines, words)

    return render_template("funny.html", lines = lines, joke1 = list1[0], joke2 = list1[1], joke3 = list1[2], isFilled=True, isLoggedIn=session.get("username") is not None)
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
