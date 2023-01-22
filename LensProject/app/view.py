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

@app.route('/effectivity', methods =['POST', 'GET'])
def effectivity():
    if request.method == 'POST':
        form_data = request.form
        print(form_data)
        sphere = float(form_data['sphere'])
        test_bvd = float(form_data['test_bvd'])
        fit_bvd = float(form_data['fit_bvd'])

        if form_data['cyl'] != '':
            cyl = float(form_data['cyl'])
            axis = float(form_data['axis'])
            comp_power = functions.compensated_power(sphere, test_bvd, fit_bvd, cyl)
            return render_template('effectivity.html',form_data = form_data, comp_power = comp_power)
        else:
            cyl = 0
            axis = None
            comp_power = [functions.compensated_power(sphere, test_bvd, fit_bvd, cyl), 0]
            return render_template('effectivity.html',form_data = form_data, comp_power = comp_power)

    if request.method == 'GET':
        comp_power = [0, 0]
        return render_template('effectivity.html', comp_power = comp_power)

@app.route('/lensthickness', methods = ["POST", "GET"])
def lensthickness():
    if request.method == "GET":
        return render_template("lensthickness.html")
    if request.method == "POST":
        functions.lens_thickness()
        return render_template("lensthickness.html")
    
@app.route("/blanksize", methods = ["POST", "GET"])
def blanksize():
    if request.method == "GET":
        return render_template("blanksize.html")
    if request.method == "POST":
        functions.calculate_simple_blanksize()
        return render_template("blanksize.html")

@app.route("/prism", methods = ["POST", "GET"])
def prism():
    if request.method == "GET":
        return render_template("prism.html")
    if request.method == "POST":
        functions.spherical_prism()
        return render_template("prism.html")

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

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/data/', methods =['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/effectivity' to submit form"
    if request.method == 'POST':
        form_data = request.form
        print(form_data)
        size = functions.calculate_simple_blanksize(51,12,53,60)
        thick = functions.lens_thickness(10,58)
        power = functions.compensated_power(12, 11, 0, 4)
        print(size)
        print(thick)
        print(type(power))
        return render_template('data.html', form_data = form_data, size = size, thick=thick, power = power)
