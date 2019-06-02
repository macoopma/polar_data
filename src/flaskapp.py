# https://www.youtube.com/watch?v=QnDWIZuWYW0 
# https://www.polar.com/accesslink-api/?python#polar-accesslink-api

from flask import Flask, render_template 
app = Flask(__name__)

@app.route ("/")
def home():
    return render_template('home.html')

@app.route ("/report")
def report():
    return "<H1>Report</H1>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

