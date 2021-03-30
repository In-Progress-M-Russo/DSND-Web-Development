from worldbankapp import app

from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/project-one')
def project_one():
    return render_template('project_one.html')

#Custom error route
#Documentation available at https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
