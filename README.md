# iMusic to Spotify Playlist Converter

This project allows you to easily transfer playlists from Apple Music to Spotify. It uses **Selenium** to scrape song names from an Apple Music playlist and **Spotipy** (a Python client for the Spotify Web API) to search for these songs and create a playlist in Spotify.

---

## Features

- Automatically extracts song names from any public Apple Music playlist.
- Creates a new playlist on Spotify with the extracted songs.
- Skips songs that are unavailable on Spotify.
- User authentication via Spotify API.

---

## Installation

### Prerequisites

Before running this project, ensure you have the following installed:

- **Python 3.x**
- **Spotify Developer Account**
- **Apple Music Playlist URL**

### Clone the repository

```bash
git clone https://github.com/<your-username>/iMusic-to-Spotify-Converter.git
cd iMusic-to-Spotify-Converter
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Spotify API Setup

1. Head over to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/login) and create a new app.
2. Obtain the following credentials from your app:
   - **Client ID**
   - **Client Secret**
3. Set up a `.env` file in the root of your project directory as follows:

```bash
SPOTIPY_CLIENT_ID=<Your Spotify Client ID>
SPOTIPY_CLIENT_SECRET=<Your Spotify Client Secret>
```

---

## Usage

1. **Run the script** to extract songs from an Apple Music playlist and create a new Spotify playlist:

```bash
python pipe.py
```

2. **Enter the Apple Music Playlist URL** when prompted. The script will then:
   - Scrape the song names using **Selenium**.
   - Search Spotify for these songs using the **Spotify API**.
   - Create a new private Spotify playlist and add the found songs to it.

---

## How It Works

1. **Selenium Scraper**:

   - A Selenium script fetches the playlist webpage from Apple Music and extracts song names.

2. **Spotipy API**:
   - The **Spotipy** library is used to interact with Spotify's API to search for each song and add it to the user's playlist.

---

## Dependencies

- **Selenium**: To scrape song data from Apple Music.
- **Spotipy**: Python library to interact with the Spotify Web API.
- **BeautifulSoup**: (Optional) For additional web scraping functionalities.
- **Requests**: To handle HTTP requests.

You can install all dependencies using:

```bash
pip install selenium spotipy beautifulsoup4 requests
```

---

## Resources

- Spotify API Documentation: [Create Playlist](https://developer.spotify.com/documentation/web-api/reference/create-playlist)
- Spotipy Documentation: [Spotipy Docs](https://spotipy.readthedocs.io/en/2.24.0/)
- Selenium Documentation: [Selenium Docs](https://www.selenium.dev/documentation/)

---

## Contributing

Feel free to submit issues or pull requests for improvements and new features!

---

## Acknowledgments

- Thanks to [Spotipy](https://spotipy.readthedocs.io/en/2.24.0/) for simplifying the interaction with Spotify's API.
- Thanks to the [Spotify Developer](https://developer.spotify.com) team for providing an excellent API!

---

Let me know if you'd like any changes or additions!
