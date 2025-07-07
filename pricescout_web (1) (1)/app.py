
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

# Dummy search endpoint
@app.route('/api/search')
def search():
    query = request.args.get('q')
    in_stock = request.args.get('inStock') == 'true'
    # Simulated results for testing
    results = [
        {"title": "iPhone X Screen", "price": 29.99, "source": "MobileSentrix", "in_stock": True, "link": "https://mobilesentrix.com", "image": ""},
        {"title": "Galaxy S10 Battery", "price": 19.49, "source": "Fixez", "in_stock": False, "link": "https://fixez.com", "image": ""},
    ]
    if in_stock:
        results = [r for r in results if r["in_stock"]]
    return jsonify(results)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
