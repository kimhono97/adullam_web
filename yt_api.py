import requests
import json

class YT_Data:
    def __init__(self):
        self.key = "AIzaSyDoG6P2w263G7gjtYsi9ryhOhy_NdsLUGQ"
        self.__ch_id = "UCXZe6SLnxBSB0S6XBaxHK4g"
        self.__playlists = self.__findPlaylists()
    def __findPlaylists(self):
        url = "https://www.googleapis.com/youtube/v3/playlists?part=snippet&channelId={0}&key={1}"
        req = requests.get(url % (self.__ch_id, self.__key))
        d = json.loads(req.text)
        out = []
        for pl in d['items']:
            i = {}
            i['id'] = pl['id']
            i['title'] = pl['snippet']['title']
            i['thumbnail'] = pl['snippet']['thumbnails']['default']
            out.append(i)
        return out
    def __findVideos(self):
        url = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults={0}&playlistId={1}&key={2}"
        out = {}
        for pl in self.__playlists:
            plid = pl['id']
            out[plid] = []
            req = requests.get(url % (20, plid, self.__key))
            d = json.loads(req.text)
            for vd in d['items']:
                
    def getPlaylists(self):
        return self.__playlists

if __name__ == "__main__":
    yt = YT_Data()
