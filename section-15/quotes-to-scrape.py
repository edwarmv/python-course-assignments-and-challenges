import requests
import bs4

req_url = "http://quotes.toscrape.com/page/{}/"

page_index = 1

authors_set = set()

quotes_list = []

top_ten_tags_list = []

while True:
    req = requests.get(req_url.format(page_index))

    soup = bs4.BeautifulSoup(req.text, "lxml")

    authors = soup.select(".quote .author")

    if len(authors) == 0:
        break

    for author in authors:
        authors_set.add(author.text)

    quotes = soup.select(".quote .text")

    if len(quotes) == 0:
        break

    for quote in quotes:
        quotes_list.appnd(quote.text)

    if page_index == 1:
        top_ten_tags = soup.select(".tag-item a")

        for tag in top_ten_tags:
            top_ten_tags_list.append(tag.text)

    page_index += 1

print("Quotes")
print(quotes_list)

print("Authors")
print(authors_set)

print("Top ten tags")
print(top_ten_tags_list)
