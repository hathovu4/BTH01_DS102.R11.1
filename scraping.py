from bs4 import formatter
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

headers = {"User-Agent": "Mozilla/5.0"}

data = []
for i in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    response = requests.get(url, headers=headers)
    response.encoding = "utf-8"
    print(response.status_code)
    soup = BeautifulSoup(response.text, "html.parser")
    cards = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    for card in cards:
        price = card.find("p", class_="price_color").get_text(strip=True)
        price = float(price.replace("£", "").strip())

        rating_tag = card.find("p", class_="star-rating")
        rating_classes = rating_tag.get("class")
        rating_word = rating_classes[1]
        rating = rating_map.get(rating_word)

        title = card.find("h3").find("a").get("title")
        link = card.find("h3").find("a").get("href")
        link = urljoin(url, link)

        status_tag = card.find("p", class_="availability")
        status = status_tag.get_text(strip=True)   
        
        data.append({
            "title": title,
            "price": price,
            "rating": rating,
            "availability": status,
            "link": link,
        })
print(f"\nTổng số sách thu được: {len(data)}")

if data:
    fieldnames = list(data[0].keys())
 
    with open("data.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
 
    print("Đã lưu vào data.csv")