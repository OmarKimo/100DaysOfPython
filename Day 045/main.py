from bs4 import BeautifulSoup
import requests
import re

url = "https://www.empireonline.com/movies/features/best-movies-2/"

website_contents = requests.get(url).text

soup = BeautifulSoup(website_contents, 'html.parser')
# I'm forced to do this beacuse of overflowing elements
data_from_script = str(soup.find(id="__NEXT_DATA__").contents[0])

movies_idxs = [titleIndex.start() + len('"titleText": ') for titleIndex in re.finditer(pattern='"titleText":', string=data_from_script)]

movies = [data_from_script[idx:data_from_script.find('"', idx)] for idx in movies_idxs]
del movies[0]
movies.reverse()
movies[0] = "1) " + movies[0]

#print(movies)

with open('movies.txt', 'w') as f:
    f.write('\n'.join(movies))
