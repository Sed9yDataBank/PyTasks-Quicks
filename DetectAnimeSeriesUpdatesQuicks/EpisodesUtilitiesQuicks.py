import os
import requests

from bs4 import BeautifulSoup
from urllib.request import urlopen


def get_url(page_url):
    try:
        req = requests.get(page_url)
    except Exception:
        print('Failed To Establish A Connection With The Website')
        return
    if req.status_code == 404:
        print('Page Not Found')
        return

    content = req.content
    soup = BeautifulSoup(content, 'html.parser')
    return soup


def zero_prefix(num):
    if num < 10:
        return '0' + str(num)
    else:
        return str(num)


def is_internet_connected():
    try:
        urlopen('http://216.58.192.142', timeout=1)  # Google IP
        return True
    except Exception:
        return False


def path_check(path, folder):
    """Check If The Folder Exists, Otherwise Create New One"""
    if folder not in os.listdir(path):
        os.mkdir(path + folder)


def display(series, season, episode, title):
    print(series, 'Season', season + ': Episode', episode, title)


def download_file(file_name, url):
    """Download The Episode"""
    req = requests.get(url)

    if req.status_code == 404 or '404' in req.url:
        print('No Such File Found')
        return

    if file_name in str(req.content):
        print('File Found')
        filename = url.split('/')[-1]
        print('Downloading...')
        with open(filename, 'wb') as fobj:
            fobj.write(req.content)
        print('Download Complete')
    else:
        print('Error')
