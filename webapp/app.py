#!/usr/bin/env python3
import os
import subprocess
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

"""
UPLOAD_FOLDER = '/usr/bin/g++ uploads/walk.cc'
ALLOWED_EXTENSIONS = {'cc'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])

def upload_file():
    if request.method == 'POST':
        subprocess.call("rm -f ./a.out", shell=True)
        retcode = subprocess.call("/usr/bin/g++ uploads/walk.cc", shell=True)
        if retcode:
            print("failed to compile walk.cc")
        exit

        subprocess.call("rm -f ./output", shell=True)
        retcode = subprocess.call("./test.sh", shell=True)

        print("Score: " + str(retcode) + " out of 2 correct.")

        print("*************Original submission*************")
        with open('uploads/walk.cc', 'r') as fs:
            print(fs.read())
"""

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result")
def submit():
    if request.method == 'POST':
        subprocess.call("rm -f ./a.out", shell=True)
    retcode = subprocess.call("/usr/bin/g++ uploads/walk.cc", shell=True)
    if retcode:
        print("failed to compile walk.cc")
    exit

    subprocess.call("rm -f ./output", shell=True)
    retcode = subprocess.call("./test.sh", shell=True)

    print("Score: " + str(retcode) + " out of 2 correct.")

    print("*************Original submission*************")
    with open('uploads/walk.cc', 'r') as fs:
        print(fs.read())

    return render_template("result.html", fs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
