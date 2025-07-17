
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/search')
def search():
    query = request.args.get('q', '')
    in_stock = request.args.get('inStock', 'false').lower() == 'true'
    # Dummy results for testing
    return jsonify([
        {"title": "Test Part A", "price": 19.99, "source": "MobileSentrix", "in_stock": True, "link": "https://example.com"},
        {"title": "Test Part B", "price": 21.99, "source": "Fixez", "in_stock": False, "link": "https://example.com"}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
