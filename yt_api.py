import requests
import json

class YT_Data:
    def __init__(self, key, ch_id):
        self.__key = key
        self.__ch_id = ch_id
        self.__url_pref = "https://www.googleapis.com/youtube/v3/"
        self.__playlists = self.__findPlaylists()
        self.__videos = self.__findVideos()
        print("<!> YT_Data : Inited")
        
    def __findPlaylists(self):
        url = self.__url_pref + "playlists?part=snippet&maxResults=%d&channelId=%s&key=%s"
        req = requests.get(url % (30, self.__ch_id, self.__key))
        d = json.loads(req.text)
        out = []
        for pl in d['items']:
            i = {}
            i['pid'] = pl['id']
            i['ptitle'] = pl['snippet']['title']
            i['pthumbnail'] = pl['snippet']['thumbnails']['high']
            out.append(i)
        return out
    
    def __findVideos(self):
        url = self.__url_pref + "playlistItems?part=snippet&maxResults=%d&playlistId=%s&key=%s"
        out = {}
        for pl in self.__playlists:
            plid = pl['pid']
            out[plid] = []
            req = requests.get(url % (30, plid, self.__key))
            d_items = []
            d = json.loads(req.text)
            if 'error' in d.keys():
                continue
            d_items += d['items']
            while 'nextPageToken' in d.keys():
                req = requests.get(url % (30, plid, self.__key) + ('&pageToken=%s' % d['nextPageToken']))
                d = json.loads(req.text)
                d_items += d['items']
            for vd in d_items:
                i = {}
                if vd['snippet']['title'] in ['Deleted video', 'Private video']:
                    continue
                i['vid'] = vd['snippet']['resourceId']['videoId']
                i['vtitle'] = vd['snippet']['title']
                i['vdesc'] = vd['snippet']['description']
                tmp = vd['snippet']['publishedAt']
                i['vpubat'] = tmp[:10] + " " + tmp[11:-1]
                tmp = vd['snippet']['thumbnails']
                if 'high' in tmp.keys():
                    i['vthumbnail'] = tmp['high']
                elif len(tmp) > 0:
                    i['vthumbnail'] = tmp[list(tmp.keys())[-1]]
                else:
                    i['vthumbnail'] = 'https://www.worldloppet.com/wp-content/uploads/2018/10/no-img-placeholder.png'
                out[plid].append(i)
        return out

    def getPlaylists(self):
        return self.__playlists

    def getVideos(self, pid):
        return self.__videos[pid]
    
    def refresh(self):
        self.__playlists = self.__findPlaylists()
        self.__videos = self.__findVideos()
        print("<!> YT_Data : Refreshed")
        return

key = "AIzaSyDoG6P2w263G7gjtYsi9ryhOhy_NdsLUGQ"
tkey = "AIzaSyAVGzJe12gm1LzSxPvgYIRQwYQM0Hxjb7I" #temp keyi
ch_id = {"adullam" : "UCXZe6SLnxBSB0S6XBaxHK4g"}

if __name__ == "__main__":
    yt = YT_Data(key, ch_id['adullam'])
    playlists = yt.getPlaylists()
    print(json.dumps(playlists, indent='\t'))
    videos = yt.getVideos(playlists[0]['pid'])
    print(json.dumps(videos, indent="\t"))


#   youtube.com/watch?v=<vid>
#   youtube.com/watch?v=<vid>&t=<min>m<sec>s
#   youtube.com/watch?v=<vid>&list<pid>

#   youtube.com/channel/<ch_id>
#   youtube.com/playlist?list=<pid>
