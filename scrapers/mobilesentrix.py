
def scrape_mobilesentrix(query, in_stock):
    return [{
        "title": f"MobileSentrix: {query}",
        "price": 17.99,
        "source": "MobileSentrix",
        "in_stock": True,
        "link": f"https://www.mobilesentrix.com/search?q={query}&submit=true",
        "image": ""
    }]
