# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 19:27:57 2020

@author: user
"""


import flask
import werkzeug

app = flask.Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def handle_request():
    imagefile = flask.request.files['image']
    filename = werkzeug.utils.secure_filename(imagefile.filename)
    print("\nReceived image File name : " + imagefile.filename)
    imagefile.save(filename)
    MusicDOA(filename);
    
    return "Image Uploaded Successfully"
def MusicDOA():
    

app.run(host="0.0.0.0", port=5000, debug=True)