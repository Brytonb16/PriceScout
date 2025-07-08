
from flask import Flask, request, jsonify, render_template
from scrapers.fixez import scrape_fixez
from scrapers.mobilesentrix import scrape_mobilesentrix
from scrapers.distro_ubif import scrape_distro_ubif
from dotenv import load_dotenv
import os
import logging

load_dotenv()  # Load .env variables

logging.basicConfig(filename="search.log", level=logging.INFO,
                    format="%(asctime)s %(message)s")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/search")
def search():
    query = request.args.get("q", "")
    in_stock = request.args.get("inStock", "false").lower() == "true"
    logging.info(f"Search: {query} | In Stock Only: {in_stock}")

    results = []
    results += scrape_fixez(query, in_stock)
    results += scrape_mobilesentrix(query, in_stock)
    results += scrape_distro_ubif(query, in_stock,
                                  os.getenv("DISTRO_USER"),
                                  os.getenv("DISTRO_PASS"))
    results = sorted(results, key=lambda x: x["price"])
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
