import requests
import bs4

base_url = "https://books.toscrape.com/catalogue/category/books_1/page-{}.html"

two_star_titles = []

for n in range(1, 51):
    scrape_url = base_url.format(n)
    req = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(req.text, "lxml")
    books = soup.select(".product_pod")

    for book in books:
        if len(book.select(".star-rating.Two")) != 0:
            book_title = book.select("a")[1]["title"]
            two_star_titles.append(book_title)

print(two_star_titles)
