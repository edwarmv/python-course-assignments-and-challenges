import requests
import bs4

result = requests.get("https://example.com/")

soup = bs4.BeautifulSoup(result.text, "lxml")

selected_node = soup.select_one('head > title')

print(selected_node and selected_node.text)
