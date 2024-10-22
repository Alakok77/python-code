"""mod doc"""
def main():
    """doc"""
    artists = []
    txt = ""
    artist = ""
    song = ""
    songs = []
    for _ in range(int(input())):
        txt = input()
        artist = txt[:txt.index("-")]
        songs.append(txt[txt.index("-") + 1:])
        if artist not in artists:
            artists.append(artist)
            artists.append(songs)
        else:
            song = txt[txt.index("-") + 1:]
            artists[artists.index(artist) + 1].append(song)
        songs = []
    for i, j in enumerate(artists):
        if not i%2:
            print(j)
        else:
            for k in j:
                print(k.strip())
main()
