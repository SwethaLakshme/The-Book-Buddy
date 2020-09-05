from app import app
from flask import Flask, render_template, url_for

@app.route('/class12cbse_biology')
def class12cbse_biology():
    return render_template('cbse/12th/biology.html')

@app.route('/class12cbse_accounts')
def class12cbse_accounts():
    return render_template('cbse/12th/accounts.html')

@app.route('/class12cbse_business_studies')
def class12cbse_business_studies():
    return render_template('cbse/12th/business_studies.html')

@app.route('/class12cbse_chemistry')
def class12cbse_chemistry():
    return render_template('cbse/12th/chemistry.html')

@app.route('/class12cbse_economics')
def class12cbse_economics():
    return render_template('cbse/12th/economics.html')

@app.route('/class12cbse_maths')
def class12cbse_maths():
    return render_template('cbse/12th/maths.html')

@app.route('/class12cbse_physics')
def class12cbse_physics():
    return render_template('cbse/12th/physics.html')

@app.route('/class12cbse_english')
def class12cbse_english():
    return render_template('cbse/12th/english.html')