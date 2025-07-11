
from flask import Flask, request, jsonify, render_template
from flask_caching import Cache
from scrapers.fixez import scrape_fixez
from scrapers.mobilesentrix import scrape_mobilesentrix
from scrapers.distro_ubif import scrape_distro_ubif
from scrapers.mengtor import scrape_mengtor
from scrapers.laptopscreen import scrape_laptopscreen
from dotenv import load_dotenv
import os
import logging

load_dotenv()

logging.basicConfig(filename="search.log", level=logging.INFO,
                    format="%(asctime)s %(message)s")

app = Flask(__name__)
cache = Cache(app, config={"CACHE_TYPE": "SimpleCache", "CACHE_DEFAULT_TIMEOUT": 300})

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/search")
@cache.cached(timeout=300, query_string=True)
def search():
    query = request.args.get("q", "")
    in_stock = request.args.get("inStock", "false").lower() == "true"
    logging.info(f"Search: {query} | In Stock Only: {in_stock}")

    results = []
    scrapers = [
        ("Fixez", scrape_fixez, [query, in_stock]),
        ("MobileSentrix", scrape_mobilesentrix, [query, in_stock]),
        ("Distro.ubif.net", scrape_distro_ubif, [query, in_stock, os.getenv("DISTRO_USER"), os.getenv("DISTRO_PASS")]),
        ("Mengtor", scrape_mengtor, [query, in_stock]),
        ("LaptopScreen", scrape_laptopscreen, [query, in_stock])
    ]

    for name, func, args in scrapers:
        try:
            results += func(*args)
        except Exception as e:
            logging.error(f"Error in {name} scraper: {e}")

    if not results:
        return jsonify([{"title": "No results found. All scrapers failed or returned nothing.", "price": 0.0, "source": "System", "in_stock": False, "link": "#", "image": ""}])

    results = sorted(results, key=lambda x: x["price"])
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
