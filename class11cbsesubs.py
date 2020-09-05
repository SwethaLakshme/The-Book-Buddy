from app import app
from flask import Flask, render_template, url_for

@app.route('/class11cbse_biology')
def class11cbse_biology():
    return render_template('cbse/11th/biology.html')

@app.route('/class11cbse_accounts')
def class11cbse_accounts():
    return render_template('cbse/11th/accounts.html')

@app.route('/class11cbse_business_studies')
def class11cbse_business_studies():
    return render_template('cbse/11th/business_studies.html')

@app.route('/class11cbse_chemistry')
def class11cbse_chemistry():
    return render_template('cbse/11th/chemistry.html')

@app.route('/class11cbse_economics')
def class11cbse_economics():
    return render_template('cbse/11th/economics.html')

@app.route('/class11cbse_maths')
def class11cbse_maths():
    return render_template('cbse/11th/maths.html')

@app.route('/class11cbse_physics')
def class11cbse_physics():
    return render_template('cbse/11th/physics.html')