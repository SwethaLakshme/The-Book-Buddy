from app import app
from flask import Flask, render_template, url_for

@app.route('/class11state_accounts')
def class11state_accounts():
    return render_template('state/11th/accounts.html')

@app.route('/class11state_botany')
def class11state_botany():
    return render_template('state/11th/botany.html')

@app.route('/class11state_zoology')
def class11state_zoology():
    return render_template('state/11th/zoology.html')

@app.route('/class11state_business_maths')
def class11state_business_maths():
    return render_template('state/11th/business_maths.html')

@app.route('/class11state_chemistry')
def class11state_chemistry():
    return render_template('state/11th/chemistry.html')

@app.route('/class11state_commerce')
def class11state_commerce():
    return render_template('state/11th/commerce.html')

@app.route('/class11state_computer_science')
def class11state_computer_science():
    return render_template('state/11th/computer_science.html')

@app.route('/class11state_economics')
def class11state_economics():
    return render_template('state/11th/economics.html')

@app.route('/class11state_english')
def class11state_english():
    return render_template('state/11th/english.html')

@app.route('/class11state_french')
def class11state_french():
    return render_template('state/11th/french.html')

@app.route('/class11state_maths')
def class11state_maths():
    return render_template('state/11th/maths.html')

@app.route('/class11state_microbiology')
def class11state_microbiology():
    return render_template('state/11th/microbiology.html')

@app.route('/class11state_physics')
def class11state_physics():
    return render_template('state/11th/physics.html')

@app.route('/class11state_tamil')
def class11state_tamil():
    return render_template('state/11th/tamil.html')