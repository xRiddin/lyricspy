import requests

song = input("enter the song name\n")
line = requests.get(f"https://some-random-api.com/lyrics?title={song}")
db = line.json()
lyrics = db["lyrics"]
title = db["title"]
artist = db["author"]
print(title + " by " + artist)

print(lyrics)
