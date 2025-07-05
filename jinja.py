### Building Url Dynamically 
### Variable Rule 
### Jinja2 Template Engine

from flask import Flask, render_template, request
'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''
### WSGI Application
app = Flask(__name__)

@app.route("/submit",methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name=request.form['name']
        return f'Hello {name}!'
    return render_template("form.html")

@app.route("/success/<score>")
def success(score):
    return f"Your score is {score}"

if __name__ == "__main__":
    app.run(debug=True)