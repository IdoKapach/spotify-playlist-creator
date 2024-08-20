from bs4 import BeautifulSoup
import requests

# this class is responsible for creating the song-list at song-list.txt
class SongListCreator():
    def __init__(self, date):
        response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
        self.soup = BeautifulSoup(response.text, 'html.parser')

    def create_list(self):
        best_song = self.soup.find(id ="title-of-a-story", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet").getText().strip()
        songs = self.soup.findAll(class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
        songs = [song.getText().strip() for song in songs]
        songs = [best_song] + songs

        with open("song-list.txt", mode="w") as file:
            for song in songs:
                file.write(song + "\n")

