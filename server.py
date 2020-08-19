from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/page/<page>")
def page(page):
    available = ["welcome", "introduce", "worship", "navbar"]
    if not page in available:
        return redirect("/")
    return render_template(page + ".html")

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/introduce")
def introduce():
    return render_template("introduce.html")

@app.route("/worship")
def worship():
    return render_template("worship.html")


if __name__ == "__main__":
    app.run(threaded=True, debug=True)
    #app.run(host="172.30.1.25", threaded=True)