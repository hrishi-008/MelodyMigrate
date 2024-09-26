import scrape_music as sm
import spotify_playlist as sp

sample_url = "https://music.apple.com/in/playlist/talha-ys/pl.u-qxylK2xT3bmP7aB"

def main():
    url = input("Enter the URL of the Apple Music playlist: ")
    sm.main(url)
    sp.main()

if __name__ == '__main__':
    main()