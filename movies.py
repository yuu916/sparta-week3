import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
import certifi

ca = certifi.where()
client = MongoClient('mongodb+srv://sparta:test@cluster0.bwwoewj.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta


URL = "https://movies.yahoo.co.jp/"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(URL, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#ranking > div.movie-list_list__4ZcXc.movie-list_displayTypeResponsive__70q18.riff-Grid__root.riff-mb-3.riff-pt-px > div.riff-flex.riff-flex-wrap.riff-ml--3 > div')

for movie in movies:
    rank = movie.select_one('span').text 
    title = movie.select_one('a.movie-list_title__lrmGG').text 
    star = movie.select_one('p > span').text 
    # print(movie.text)
    # print(rank, title, star)

    doc = {
            'title': title,
            'rank': rank,
            'star': star
    }
    db.movies.insert_one(doc)
