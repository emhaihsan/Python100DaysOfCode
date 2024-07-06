import requests
from bs4 import BeautifulSoup

url = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

movies = soup.find_all('h3', class_='listicleItem_listicle-item__title__BfenH')


with open('movies.txt', 'w') as f:
    for movie in movies[-1:0:-1]:
        f.write(movie.get_text() + '\n')
