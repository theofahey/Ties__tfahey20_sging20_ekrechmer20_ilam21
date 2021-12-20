from flask import Flask, render_template, request, session, url_for, redirect
from user import User
import os
from os import path, remove
from story_manager import Story_manager


app = Flask(__name__)
app.secret_key = os.urandom(32)