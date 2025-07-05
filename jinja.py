### Building Url Dynamically 
### Variable Rule 
### Jinja2 Template Engine
'''
{{ }} expressions to print output in HTML 
{%...%} conditions, for loops 
{#...#} this is for comments
'''

from flask import Flask, render_template, request, redirect, url_for
'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''
### WSGI Application
app = Flask(__name__)

# @app.route("/submit",methods=["GET", "POST"])
# def form():
#     if request.method == "POST":
#         name=request.form['name']
#         return f'Hello {name}!'
#     return render_template("form.html")

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


@app.route("/fail/<int:score>")
def fail(score):
    return render_template("result.html", result=score)

@app.route("/submit", methods=["GET", "POST"])
def submit():
    total_score = 0 
    if request.method == "POST":
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])

        total_score = (science + maths + c + datascience) / 4
    else:
        return render_template("getresult.html")

    return redirect(url_for('successres', score=total_score)   )


if __name__ == "__main__":
    app.run(debug=True)