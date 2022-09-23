import requests
from bs4 import BeautifulSoup




# response = requests.get("https://news.ycombinator.com/news")
# ycombinator = BeautifulSoup(response.text, "html.parser")



response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
website_html = BeautifulSoup(response.text, "html.parser")


titles_list = website_html.select("section .article-title-description h3.title")
# print(titles) # this will be a list of strings - it was a list of h3 tags



movie_titles = [title.getText() for title in titles_list]
top_100_movies = movie_titles[::-1]
# print(top_100_movies)

with open("movies.txt", mode="w") as file:
    for movie in top_100_movies:
        file.write(f"{movie}\n")



