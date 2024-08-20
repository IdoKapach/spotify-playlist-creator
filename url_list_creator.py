
# this class is responsible for creating the url-list at url-list.txt
class UrlListCreator():
    def __init__(self, sp):
        self.sp = sp


    def create_list(self):
        with open("song-list.txt") as file:
            song_list=file.readlines()

        song_list = [song.replace(" ", "-") for song in song_list]
        url_list=[]
        for song in song_list:
            response = self.sp.search(q=f"remaster%2520track%3{song}", type="track")
            if len(response["tracks"]["items"]) > 0:
                url = response["tracks"]["items"][0]["uri"]
                url_list.append(url)

        with open("url-list.txt", "w") as file:
            for url in url_list:
                file.write(url.strip("spotify:track:") + "\n")