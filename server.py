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


if __name__ == "__main__":
    app.run(threaded=True, debug=True)
    #app.run(host="172.30.1.25", threaded=True)