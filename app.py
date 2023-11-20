from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import check as check

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    if(request.method == 'POST'):
        username=request.form['username']
        password=request.form['password']
        validity=check(username,password)
        if(validity==True):
            return redirect(url_for('home'))
        else:
            return redirect(url_for('login'))
    render_template('login.html')
    
@app.route('/home')
def home():
    user=displayuser(username)
    entries={
        'username':user.username,
        'password':user.password,
    }
    return render_template('home.html', entries=entries)
@app.route('/')
def register():
    if(request.method=='post'):
        username=request.form['username']
        password=request.form['password']
        createuser(username,password)
        redirect(url_for('login'))
        
    return render_template('register.html')

       
app.run(debug=True, port=5000)