from flask import Flask, sessions, redirect, request, render_template
app=Flask(__name__)
app.secret_key="some key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')
    
app.run(debug=True)