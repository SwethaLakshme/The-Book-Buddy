from app import app
from flask import Flask, render_template, url_for

@app.route('/class10cbse_english')
def class10cbse_english():
    return render_template('cbse/10th/english.html')

@app.route('/class10cbse_history ')
def class10cbse_history ():
    return render_template('cbse/10th/history.html')

@app.route('/class10cbse_civics ')
def class10cbse_civics ():
    return render_template('cbse/9th/civics.html')

@app.route('/class10cbse_geography ')
def class10cbse_geography ():
    return render_template('cbse/10th/geography.html')

@app.route('/class10cbse_economics')
def class10cbse_economics():
    return render_template('cbse/10th/economics.html')

@app.route('/class10cbse_maths')
def class10cbse_maths():
    return render_template('cbse/10th/maths.html')

@app.route('/class10cbse_science')
def class10cbse_science():
    return render_template('cbse/10th/science.html')