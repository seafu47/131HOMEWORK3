from app import myapp_obj
from flask import redirect, url_for, render_template, request, flash

name = "Lisa"
city_names = ["Paris", "London", "Rome", "Tahiti"]
myapp_obj.config['SECRET_KEY'] = "1357"



@myapp_obj.route("/", methods=["GET", "POST"])
def home():
	if request.method == "POST":
		city = request.form['cityname']
		flash(city)
	
	
	return render_template('home.html', name = name, cities = city_names)
	

