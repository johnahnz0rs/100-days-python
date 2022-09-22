import requests
from bs4 import BeautifulSoup

# with open("website.html") as file:

#     content = file.read()

# soup = BeautifulSoup(content, "html.parser")

# print(soup)


response = requests.get("https://news.ycombinator.com/news")
ycombinator = BeautifulSoup(response.text, "html.parser")


# first_article = ycombinator.select_one("a.titlelink")
# first_article_title = first_article.get_text()
# first_article_link = first_article["href"]

# first_article_meta = ycombinator.select_one(".subtext .score ").get_text()
# first_article_upvotes = first_article_meta.split(" ")[0]


# print(f"title: {first_article_title}\nlink: {first_article_link}\nupvotes: {first_article_upvotes}")

articles = ycombinator.select(".titlelink")
# print(articles)
titles = []
links = []
for a in articles:
    titles.append(a.get_text())
    links.append(a["href"])

list_of_upvotes = ycombinator.select(".subtext .score")
upvotes = [int(u.get_text().split()[0]) for u in list_of_upvotes]
max_score = max(upvotes)
max_score_index = upvotes.index(max_score)

highest_voted_article = {
    'title': titles[max_score_index],
    'link': links[max_score_index],
    'upvote': upvotes[max_score_index]
}

print(highest_voted_article)



# print(titles)
# print(links)
# print(upvotes)

