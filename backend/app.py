from flask import Flask, request, render_template, jsonify
from web_scraper import scrape_data

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    results = None
    if request.method == 'POST':
        search_query = request.form['search_query']
        results = scrape_data(search_query)  # Chama a função de scraping com a consulta
    return render_template('index.html', results=results)

@app.route('/api/scrape', methods=['GET'])
def scrape():
    data = scrape_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)