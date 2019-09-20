from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')




@app.route('/results', methods = ["post","get"])
def results():
    #process data from form
    userdata = dict(request.form)
    print(userdata)
    generation= userdata ['generation']
    output = model.gen(generation)
    return "generation"
