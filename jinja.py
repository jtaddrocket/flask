### Building Url Dynamically 
### Variable Rule 
### Jinja2 Template Engine
'''
{{ }} expressions to print output in HTML 
{%...%} conditions, for loops 
{#...#} this is for comments
'''

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

@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"
    return render_template("result.html", result=res)

@app.route("/successres/<int:score>")
def successres(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"

    exp = {'score': score, 'res':res}
    return render_template("result1.html", result=exp)

## if condition
@app.route("/successif/<int:score>")
def successif(score):

    return render_template("result2.html", result=score)

if __name__ == "__main__":
    app.run(debug=True)