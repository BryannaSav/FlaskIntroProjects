from flask import Flask, redirect, request, session, render_template
app=Flask(__name__)
app.secret_key="keykey"
@app.route('/')
def index():
    if 'click' not in session:
        session['click']=0
    return render_template ("index.html", click=session['click'])
@app.route('/clicker')
def clicker():
    session['click']+=1
    return redirect ('/')
@app.route('/reset')
def reset():
    session['click']=0
    return redirect ('/')
app.run(debug=True)
