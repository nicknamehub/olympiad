from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('main_page.html')

@app.errorhandler(404)
def error404(e):
	return render_template('404.html')

@app.route('/vk')
def vk():
	return render_template('vk.html')