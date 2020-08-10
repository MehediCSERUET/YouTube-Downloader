from pytube import YouTube
from pytube import Playlist
import re
import os

def single():
    key = input('Input what you want to download:')
    #yt = pytube.YouTube(key)
    #stream = yt.streams.first()
    #stream.download()
    YouTube(key).streams.get_highest_resolution().download()
def playlist():
    pl = input("Enter playlist link:")
    playlist = Playlist(pl)

    # this fixes the empty playlist.videos list
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    print(len(playlist.video_urls))

    folder_name = pl.split('?')[1]
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for url in playlist.video_urls:
        print("Downloading: "+str(url))
        YouTube(url).streams.get_highest_resolution().download(folder_name)

        
if __name__ == "__main__":
    while(True):
        choice = input("Do you want to continue: y/n?")
        if choice == 'n' or choice == 'N':
            break
        else:
            choice2 = input("Press s for single and p for playlist download: ")
            if choice2 == 'S' or choice2 == 's':
                single()
            elif choice2 == 'p' or choice2 == 'P':
                playlist()
            else:
                print("Wrong choice")