from flask import Flask, render_template , request
from flask import *
from datetime import datetime
import pickle
import joblib
import numpy as np
pickled_model = pickle.load(open(r'/Users/nageswararaokolapalli/Documents/Python Tutorial Sample Works/Sample projects/Price Prediction/Final/Price/my_model.sav', 'rb'))

app = Flask(__name__)

@app.route("/",methods=["GET", "POST"])
def home():
    if request.method == 'POST':
        a=10
        b=10
        c=10
        d=10
        e=10
        f=10
        g=10
        h=10
        if request.form['degree']=="B-Tech":
            a=0
        elif request.form['degree']=="M-Tech":
            a=1
        if request.form['domain']=="Artificial Intelligence":
            b=0
        elif request.form['domain']=="Electronics":
            b=1
        if request.form['course']=="Computer Vision":
            c=0
        elif request.form['course']=="Natural Language Processing":
            c=1
        elif request.form['course']=="Deep Learning":
            c=2
        if request.form['course']=="Embedded Systems":
            c=0
        elif request.form['course']=="IOT + AI":
            c=1
        elif request.form['course']=="Robotics":
            c=2
        elif request.form['course']=="MATLAB":
            c=3
        elif request.form['course']=="HFSS":
            c=4
        if request.form['level']=="Easy":
            d=0
        elif request.form['level']=="Moderate":
            d=1
        elif request.form['level']=="Advanced":
            d=2
        if request.form['type']=="Major":
            e=0
        elif request.form['type']=="Minor":
            e=1
        if request.form['doc']=="Yes":
            f=0
        elif request.form['doc']=="No":
            f=1
            g=1
        if request.form['plag']=="Yes":
            g=0
        elif request.form['plag']=="No":
            g=1
        print(request.form['plag'])
        if request.form['dead']=="<10 Days":
            h=0
        elif request.form['dead']==">10 Days":
            h=1
        if  (a==0 or a==1) and (b==0 or b==1) and (c==0 or c==1 or c==2 or c==3 or c==4) and (d==0 or d==1 or d==2) and (e==0 or e==1) and (f==0 or f==1) and (g==0 or g==1) and (h==0 or h==1):
            temp = list()
            temp = temp + [a,b,c,d,e,f,g,h]
            data = np.array([temp])
            predicted_price = int(pickled_model.predict(data)[0])
            return render_template("2.html",pred=predicted_price)
        else:
            s="Please Select all the Feilds"
            return render_template("s.html",war=s)
    return render_template("s.html")

@app.route("/predict")
def pred():
    return render_template("2.html")

@app.route("/pred")
def pred1():
    return render_template("1.html")


@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    b=10
    app.run(debug=True,port=1412) 