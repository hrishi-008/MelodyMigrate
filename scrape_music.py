from selenium import webdriver
from selenium.webdriver.common.by import By
import time, json
from selenium.webdriver.chrome.options import Options

def extract_songs_from_playlist(url):
    """
    Extract song names from an Apple Music playlist and save them to a JSON file.
    Args:
        url (str): The URL of the Apple Music playlist.
    Returns:
        None
    Raises:
        None
    Example Usage:
        extract_songs_from_playlist("https://music.apple.com/in/playlist/talha-ys/pl.u-qxylK2xT3bmP7aB")
    """
    chrome_options = Options()
    chrome_options.headless = True  # Use headless mode for browser
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    driver.implicitly_wait(5)

    # Find all song names by the given class name
    songs = driver.find_elements(By.CLASS_NAME, 'songs-list-row__song-name')

    # Create a dictionary to store the URL and song list
    variable = {
        'url': url,
        'songs': []
    }

    # Extract song names and add to the list
    for song in songs:
        song_name = song.text
        variable['songs'].append(song_name)  # Append song name directly

    # Save the results to a json file
    with open('playlist_songs.json', 'w') as f:
        json.dump(variable, f, indent=4)

    # Close the browser
    driver.quit()

def main(link: str):
    extract_songs_from_playlist(link)

if __name__ == '__main__':
    main('https://music.apple.com/in/playlist/talha-ys/pl.u-qxylK2xT3bmP7aB')
