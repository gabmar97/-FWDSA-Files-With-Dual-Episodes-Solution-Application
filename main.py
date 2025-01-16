# OG script written by ChatGPT #
# No Credit #
# Open Source #

*import os
import re
import requests
from tkinter import Tk, filedialog

# Configuration for the TVDB API
API_KEY = "your_tvdb_api_key"  # Replace with your TVDB API key
BASE_URL = "https://api.thetvdb.com"

# Authenticate with the TVDB API
def authenticate_tvdb():
    url = f"{BASE_URL}/login"
    payload = {
        "apikey": API_KEY
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()["token"]
    else:
        raise Exception(f"Failed to authenticate with TVDB: {response.text}")

# Fetch episode titles from TVDB
def fetch_episode_titles(token, show_name, season, episode):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    search_url = f"{BASE_URL}/search/series?name={show_name}"
    search_response = requests.get(search_url, headers=headers)

    if search_response.status_code != 200:
        raise Exception(f"Failed to search for series '{show_name}': {search_response.text}")

    series_data = search_response.json()["data"]
    if not series_data:
        raise Exception(f"No series found for '{show_name}'")

    series_id = series_data[0]["id"]
    episodes_url = f"{BASE_URL}/series/{series_id}/episodes/query"
    params = {
        "airedSeason": season,
        "airedEpisode": episode
    }

    episode_response = requests.get(episodes_url, headers=headers, params=params)
    if episode_response.status_code != 200:
        raise Exception(f"Failed to fetch episode details: {episode_response.text}")

    episode_data = episode_response.json()["data"]
    if len(episode_data) < 2:
        raise Exception(f"Not enough episode data found for season {season}, episode {episode}")

    current_episode = episode_data[0]["episodeName"]
    next_episode = episode_data[1]["episodeName"]

    return current_episode, next_episode

# Rename video files
def rename_files_in_directory(directory, show_name):
    token = authenticate_tvdb()

    for filename in os.listdir(directory):
        if not filename.endswith(".mkv"):
            continue

        # Extract the season and episode info from the filename
        match = re.search(r"S(\d+)E(\d+)", filename)
        if not match:
            print(f"Could not parse season/episode from '{filename}', skipping.")
            continue

        season = int(match.group(1))
        episode = int(match.group(2))

        try:
            current_title, next_title = fetch_episode_titles(token, show_name, season, episode)
        except Exception as e:
            print(f"Failed to fetch episode titles for '{filename}': {e}")
            continue

        # Create the new filename
        new_filename = f"Season {season} - Episode {episode} ({current_title}) and Episode {episode + 1} ({next_title}).mkv"
        new_filepath = os.path.join(directory, new_filename)

        old_filepath = os.path.join(directory, filename)
        os.rename(old_filepath, new_filepath)
        print(f"Renamed: '{filename}' -> '{new_filename}'")

if __name__ == "__main__":
    # Create a Tkinter file dialog to select the series directory
    Tk().withdraw()  # Hide the root Tkinter window
    series_directory = filedialog.askdirectory(title="Select the Series Directory")

    if not series_directory:
        print("No series directory selected. Exiting.")
        exit()

    # Extract the series name from the directory
    show_name = os.path.basename(series_directory)

    # Create a Tkinter file dialog to select the season directory
    season_directory = filedialog.askdirectory(title="Select the Season Directory")

    if not season_directory:
        print("No season directory selected. Exiting.")
        exit()

    # Rename files in the selected season directory
    rename_files_in_directory(season_directory, show_name)
