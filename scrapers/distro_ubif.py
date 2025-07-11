
import requests
from bs4 import BeautifulSoup

def scrape_distro_ubif(query, in_stock, username, password):
    session = requests.Session()
    login_url = "https://distro.ubif.net/login"
    session.post(login_url, data={
        "email": username,
        "password": password
    })
    search_url = f"https://distro.ubif.net/search?q=" + query
    response = session.get(search_url, timeout=10)
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
        results.append({{
            "title": title,
            "price": price,
            "source": "Distro.ubif.net",
            "in_stock": True,
            "link": link,
            "image": ""
        }})
    return results
