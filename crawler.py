#!/usr/bin/env python
# encoding=utf-8

import requests
from platform import python_version
from bs4 import BeautifulSoup
import codecs

DOWNLOAD_URL = 'http://movie.douban.com/top250'


def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/47.0.2526.80 Safari/537.36 '
    }
    data = requests.get(url).content
    return data


def main():
    print(download_page(DOWNLOAD_URL))


def parse_html(html):
    soup = BeautifulSoup(html)
    movie_list_soup = soup.find('ol', {'class': 'grid_view'})

    movie_name_list = []

    for movie_li in movie_list_soup.find_all('li'):
        detail = movie_li.find('div', {'class': 'hd'})
        movie_name = detail.find('span', {'class': 'title'}).getText()
        movie_name_list.append(movie_name)

    next_page = soup.find('span', {'class', 'next'}).find('a')
    if next_page:
        return movie_name_list, DOWNLOAD_URL + next_page['href']
    return movie_name_list, None


if __name__ == '__main__':
    print(python_version())
    main()
    parse_html(download_page(DOWNLOAD_URL))
