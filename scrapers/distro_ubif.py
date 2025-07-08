
def scrape_distro_ubif(query, in_stock, username, password):
    # Simulated login using username/password from .env
    return [{
        "title": f"Distro: {query}",
        "price": 21.99,
        "source": "Distro.ubif.net",
        "in_stock": True,
        "link": f"https://distro.ubif.net/search?q={query}",
        "image": ""
    }]
