import os
import sys

from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

def main():
    musicPath = raw_input("Provide path to music folder (Default: '~/Main/Etc/Music/'):\n")
    if musicPath is '':
        musicPath = "/Users/aden/Main/Etc/Music/"

    print("Cleaning ID3 Tags with Beets...")
    cmd = "beet import \"{0}\" -qCl \"{0}untagged.log\"".format(musicPath)
    os.system(cmd)

    music = [os.path.join(root, name)
             for root, dirs, files in os.walk(musicPath)
             for name in files if name.endswith(".mp3")]

    albums = {}


for f in music:
    tag = MP3(f, ID3=EasyID3)
    try:
        artist = tag['artist'][0].encode('utf-8')
        album = tag['album'][0].encode('utf-8')
    except Exception:
        sys.exc_clear()
        print "No valid Artist or Album on " + f

    try:
        albums.update({artist: album})
    except Exception:
        sys.exc_clear()
        print "Cannot update the dictionary for " + f


main()

