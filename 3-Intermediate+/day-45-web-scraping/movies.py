# This script uses the requests and BeautifulSoup libraries to scrape the
# top 10 movies from Empire's list of the best movies of all time. The URLs
# of each movie are stored in a text file named "movies.txt".

import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage to scrape
url = "https://www.empireonline.com/movies/features/best-movies-2/"

# Send a GET request to the webpage and store the response
response = requests.get(url)

# Parse the HTML content of the webpage using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the <h3> tags with the class "listicleItem_listicle-item__title__BfenH"
# and store them in a list called "movies"
movies = soup.find_all('h3', class_='listicleItem_listicle-item__title__BfenH')

# Open a file named "movies.txt" in write mode
with open('movies.txt', 'w') as f:
    # Iterate over the movies in reverse order (i.e., highest ranking to lowest)
    for movie in movies[-1:0:-1]:
        # Write the text content of each movie to the file
        f.write(movie.get_text() + '\n')