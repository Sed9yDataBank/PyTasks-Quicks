""" 
Checks For The New Episodes Of Any TV Series Or Anime.
"""

import os
import sys

from utils import is_internet_connected, path_check, zero_prefix
from new_episode_check import tv_episode_check, anime_episode_check


# Browse the TV Series folder
def tv_series(path, name_list, mode):
    print('\n\nChecking TV Series...\n')

    for name in name_list:
        path_check(path, name)

        series = ' '.join(name.split()[:-2])
        season = int(name.split()[-1])
        ep_season_occurrence = 's' + zero_prefix(season) + 'e'

        dir_contents = [ep.lower() for ep in os.listdir(path + name)]
        dir_contents_idx = [ep.find(ep_season_occurrence.lower()) for ep in dir_contents]
        dir_episodes = [ep[x+4:x+6] for x, ep in zip(dir_contents_idx, dir_contents)]
        dir_episodes.sort(key=int)

        new_ep = int(1 if os.listdir(path + name) == [] else int(dir_episodes[-1]) + 1)
        tv_episode_check(
            series, season,
            'https://en.wikipedia.org/wiki/',
            mode, new_ep
        )
    print('\n---------------------------------------------')


# Browse the Anime folder
def anime(path, name_list):
    print('\n\nChecking Anime...\n')

    for name in name_list:
        path_check(path, name)

        dir_contents = [ep.split('.')[0] for ep in os.listdir(path + name)]
        dir_contents.sort(key=int)
        new_ep = int('1' if os.listdir(path + name) == [] else str(int(dir_contents[-1]) + 1))
        anime_episode_check(
            name,
            'http://www.chia-anime.tv/episode/',
            new_ep
        )
    print('\n-------------------------------------------------------')


if not is_internet_connected():
    print('No Internet connection')
    sys.exit(0)

tv_list = [
    'Normal People Season 1',
    'The Big Bang Theory Season 12',
]

anime_list = [
    'Castlevania',
    'One Piece',
    'Detective Conan: The Scarlet Bullet'
]

path_anime = '/home/your_path/videos/Anime/'
path_tv = '/home/your_path/videos/TV/'

modes = ['Local File', 'Timed']

tv_series(path_tv, tv_list, modes[1])
anime(path_anime, anime_list)
