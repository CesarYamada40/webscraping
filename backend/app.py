from flask import Flask, jsonify
from web_scraper import scrape_data

app = Flask(__name__)

@app.route('/')
def home():
    return "Bem-vindo à página inicial!"

@app.route('/api/scrape', methods=['GET'])
def scrape():
    data = scrape_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)