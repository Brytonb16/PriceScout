
import requests
from bs4 import BeautifulSoup

def scrape_laptopscreen(query, in_stock):
    search_url = "https://www.laptopscreen.com/English/search/?q=" + query
    response = requests.get(search_url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    results = []
    for item in soup.select(".product-item")[:5]:
        title_el = item.select_one(".product-title")
        title = title_el.text.strip() if title_el else "No Title"
        link_el = item.select_one("a")
        link = link_el["href"] if link_el else "#"
        price_el = item.select_one(".price")
        price_text = price_el.text.strip().replace("$", "") if price_el else "0"
        price = float(price_text) if price_text else 0.0
        results.append({
            "title": title,
            "price": price,
            "source": "LaptopScreen",
            "in_stock": True,
            "link": link,
            "image": ""
        })
    return results
