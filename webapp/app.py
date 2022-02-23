#!/usr/bin/env python3
import os
import subprocess
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
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

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'cc'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=['POST'])
def upload():
    if request.method =='POST':
        files = request.files.getlist("file[]")
        print(request.files)
        for file in files:
            path = os.path.dirname(file.filename)
            path2 = os.path.join(app.config['UPLOAD_FOLDER'], path)
            if not os.path.exists(path2):
                os.mkdir(path2)
            filename = os.path.join(path, secure_filename(os.path.basename(file.filename)))
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'Files uploaded.'

def submit():
    if request.method == 'POST':
        subprocess.call("rm -f ./a.out", shell=True)
        retcode = subprocess.call("/usr/bin/g++ ./uploads/walk.cc", shell=True)
        if retcode:
            print("failed to compile walk.cc")
        exit    

        subprocess.call("rm -f ./output", shell=True)
        retcode = subprocess.call("./test.sh", shell=True)

        print("Score: " + str(retcode) + " out of 2 correct.")

        print("*************Original submission*************")
        with open('./uploads/walk.cc', 'r') as fs:
            print(fs.read())
    # if request.method == 'POST':
    #     subprocess.call("compile.sh", shell=True)
    # result = subprocess.check_output('python', 'compile.py')

    return render_template("result.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
