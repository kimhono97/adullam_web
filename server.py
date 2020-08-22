from flask import Flask, render_template, request, session, redirect, url_for
import yt_api as yt
import json

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

@app.route("/sermon", methods=["GET"])
def sermon():
    global ytd
    playlists = ytd.getPlaylists()
    try:
        tab = int(request.args.get('t'))
        if tab < 0 or tab >= len(playlists):
            tab = 0
    except:
        tab = 0
        for pl in playlists:
            if "주일" in pl['ptitle']:
                break
            tab += 1
    
    videos = ytd.getVideos(playlists[tab]['pid']).copy()
    videos.reverse()
    tabs = list(enumerate(playlists))

    return render_template("sermon.html", tab=tab, tabs=tabs, videos=videos[:11])

@app.route("/update")
def update():
    global ytd
    ytd.refresh()
    return "Success!"

if __name__ == "__main__":
    ytd = yt.YT_Data(yt.key, yt.ch_id['adullam'])
    #app.run(threaded=True, debug=False)
    app.run(host="172.30.1.25", threaded=True)
