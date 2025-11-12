thonimport json
import requests
from extractors.twitch_parser import parse_twitch_video_data
from outputs.data_exporter import export_data
from config.settings import SETTINGS

def run_scraper():
    search_keywords = SETTINGS["keywords"]
    all_videos = []

    for keyword in search_keywords:
        response = requests.get(f"https://api.twitch.tv/kraken/search/videos?query={keyword}&limit=100")
        video_data = parse_twitch_video_data(response.json())
        all_videos.extend(video_data)
    
    export_data(all_videos, 'output.json')

if __name__ == "__main__":
    run_scraper()