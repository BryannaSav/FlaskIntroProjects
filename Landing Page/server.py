from flask import Flask, session, redirect, request, render_template
app = Flask(__name__)
app.secret_key="some key"
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos/new')
def dojos():
    return render_template('dojos.html')

app.run(debug=True)