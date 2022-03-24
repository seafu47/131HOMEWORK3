from flask import Flask
import os

app = Flask(__name__)
name = "Lisa"
city_names = ["Paris", "London", "Rome", "Tahiti"]

@app.route("/")
def home():
	return '''
	<html>
	<head>
		<title>home page</title>
		<h1>Welcome '''+name+'''!</h1>
	</head>	
		<a href=www.google.com>not google</a>
	<body>

	<ul>
		<li>'''+city_names[0]+'''</li>
		<li>'''+city_names[1]+'''</li>
		<li>'''+city_names[2]+'''</li>
		<li>'''+city_names[3]+'''</li>
	</ul>
	</body>
	</html> '''
	
if __name__ == "__main__":
	app.run()

