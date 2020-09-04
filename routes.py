from app import app
from flask import Flask, render_template, url_for
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cbsetextbook')
def cbsetextbook():
    return render_template('cbsetextbook.html')

@app.route('/stateboardtextbook')
def stateboardtextbook():
    return render_template('stateboardtextbook.html')