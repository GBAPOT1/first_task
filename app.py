#!flask/bin/python
from flask import Flask, request, render_template, url_for
import csv

app = Flask(__name__)
 
@app.route("/")
def home():
    return render_template('echo.html')

@app.route("/csv", methods=['POST'])
def readcsv():
	file = request.form['mylist']

	with open( file , 'r') as f:
		csv_reader = csv.reader(f)
		
		return render_template('echo.html', list = [row for row in csv_reader])

 
if __name__ == "__main__":
    app.run(debug=True)