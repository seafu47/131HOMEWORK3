from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
	name = "Lisa"
	city_names = ["Paris", "London", "Rome", "Tahiti"]
	return '''
	<html>
	<head>
		<title>home page</title>
	</head>
	<body>
		<h1>Welcome '''+name+'''</h1>		
		<p> <a href=https://www.google.com/"> not google </a> </p>
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

