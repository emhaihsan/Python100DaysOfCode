from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    article_texts.append(article_tag.get_text())
    article_links.append(article_tag.find(name="a", href=True)["href"])

article_upvotes = [score.getText().split()[0] for score in soup.find_all(name="span", class_="score")]


max_upvotes_index = article_upvotes.index(max(article_upvotes))
best_article = article_texts[max_upvotes_index]
best_links = article_links[max_upvotes_index]

print(f"{best_article}\n{best_links}\n{max(article_upvotes)}")