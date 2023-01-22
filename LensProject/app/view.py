from datetime import datetime

from flask import Flask, render_template, request

from . import app

from . import functions


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name = name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")


@app.route('/effectivity', methods =['POST', 'GET'])
def effectivity():
    if request.method == 'POST':
        form_data = request.form
        sphere = float(form_data['sphere'])
        cyl = float(form_data['cyl'])
        axis = float(form_data['axis'])
        test_bvd = float(form_data['test_bvd'])
        fit_bvd = float(form_data['fit_bvd'])
        comp_power = functions.compensated_power(sphere, test_bvd, fit_bvd, cyl)
        return render_template('effectivity.html',form_data = form_data, comp_power = comp_power)
    if request.method == 'GET':
        comp_power = [0, 0]
        return render_template('effectivity.html', comp_power = comp_power)
    

@app.route('/data/', methods =['POST', 'GET'])
def data():
   
        return f"The URL /data is accessed directly. Try going to '/effectivity' to submit form"
