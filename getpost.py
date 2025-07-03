from flask import Flask, render_template, request
'''
It creates an instance of the Flask class,
which will be your WSGI (Web Server Gateway Interface) application.
'''
### WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the Flask course</H1></html>"

@app.route("/index",methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

'''
Khi người dùng truy cập /form -> Mặc định GET sẽ redirect đến form.html.
Khi user nhập tên và submit form, form dùng method="post" nên sẽ gửi yêu cầu bằng POST
-> server lấy dữ liệu từ request.form['name'] và phản hồi bằng Hello {name}!.
'''
@app.route("/form",methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name=request.form['name']
        return f'Hello {name}!'
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)