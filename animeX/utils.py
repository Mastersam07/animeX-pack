import os
import requests
import wget
from bs4 import BeautifulSoup


def banner():
    """
        Banner
    """
    banner_ascii = """
  /$$$$$$            /$$                         /$$   /$$
 /$$__  $$          |__/                        | $$  / $$
| $$  \ $$ /$$$$$$$  /$$ /$$$$$$/$$$$   /$$$$$$ |  $$/ $$/
| $$$$$$$$| $$__  $$| $$| $$_  $$_  $$ /$$__  $$ \  $$$$/
| $$__  $$| $$  \ $$| $$| $$ \ $$ \ $$| $$$$$$$$  >$$  $$
| $$  | $$| $$  | $$| $$| $$ | $$ | $$| $$_____/ /$$/\  $$
| $$  | $$| $$  | $$| $$| $$ | $$ | $$|  $$$$$$$| $$  \ $$
|__/  |__/|__/  |__/|__/|__/ |__/ |__/ \_______/|__/  |__/
"""

    return banner_ascii


def get_version():
    __version__ = '0.1.7'
    return __version__


def get_search_result(search_item):
    """
        Searches for a given anime
    """
    search_url = "https://www.animeout.xyz/"
    params = {
        "s": search_item
    }
    r = requests.get(search_url, params=params)
    search_result_html = BeautifulSoup(r.text, "html.parser")

    search_result = []
    for i in search_result_html.findAll("h3", {"class": "post-title"}):
        search_result.append({
            "name": i.text,
            "url": i.find("a")["href"]
        })
    return search_result


def get_anime_episodes(anime_url):
    """
        Get the episodes in the anime by parsing all links that are videos
    """
    r = requests.get(anime_url)
    anime_result = BeautifulSoup(r.text, "html.parser")

    episodes = []
    for i in anime_result.findAll("a"):
        try:
            if i["href"][-3:] in ["mkv", "mp4]"]:
                episodes.append(i["href"])
        except:
            pass
    return episodes


def get_download_url(anime_url):
    """
        Get the video download URL
    """
    r = requests.get(anime_url)
    pre_download_page = BeautifulSoup(r.text, "html.parser")
    pre_download_url = pre_download_page.find("a", {"class": "btn"})["href"]

    r = requests.get(pre_download_url)
    download_page = BeautifulSoup(r.text, "html.parser")
    # using a try catch because .text returned empty on some OS
    try:
        download_url = download_page.find(
            "script", {"src": None}).text.split('"')[1]
    except:
        download_url = download_page.find(
            "script", {"src": None}).contents[0].split('"')[1]
    return download_url


def download_episode(anime_name, download_url):
    """
        Download anime and store in the folder the same name
        Don't download files that exist and clear tmp files after download
    """
    filename = os.path.basename(download_url)
    download_path = os.path.join(anime_name, filename)
    if not os.path.exists(download_path):
        print("\nDownloading", filename)
        wget.download(download_url, download_path)
        clear_tmp(anime_name)


def make_directory(anime_name):
    """
        Create folder to store anime
    """
    if not os.path.exists(anime_name):
        os.mkdir(anime_name)


def clear_tmp(directory):
    # clear tmp files
    for i in os.listdir(directory):
        if i[-3:] == "tmp":
            os.remove(os.path.join(directory, i))
