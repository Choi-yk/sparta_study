import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for tr in trs:
    title = tr.select_one('td.info > a.title.ellipsis')
    rank = tr.select_one('tr > td.number')

    if title is not None:
        music_rank = rank.text[0:2].strip()
        music_title = title.text.strip()  # strip()
        artist = tr.select_one('td.info > a.artist.ellipsis').text
        print(music_rank, music_title, artist)
        # print(rank.text[0], rank.text[1])