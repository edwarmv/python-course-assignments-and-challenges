import requests
import bs4
import io

result = requests.get("https://example.com/")

soup = bs4.BeautifulSoup(result.text, "lxml")

selected_node = soup.select_one("head > title")

print(selected_node and selected_node.text)

# Grabbing a Class

result = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")

soup = bs4.BeautifulSoup(result.text, "lxml")

for tag in soup.select(".vector-toc-text"):
    print(tag.text)

# Grabbing an Image

result = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")

soup = bs4.BeautifulSoup(result.text, "lxml")

computer = soup.select_one(".infobox-image img")

if computer:
    image_link = f"https:{computer['src']}"
    image = requests.get(image_link)
    f = io.open("my_computer_image.jpg", "wb")
    f.write(image.content)
    f.close()
