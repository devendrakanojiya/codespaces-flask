from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")

@app.route("/admin")
def admin():
    return render_template("admin.html", title="Admin")

if __name__ == '__main__':
    app.run()
