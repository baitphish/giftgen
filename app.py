from flask import Flask, render_template, request
import generate_codes
import json

app = Flask(__name__)
config = load_config('config.json')

@app.route('/', methods=['GET', 'POST'])
def index():
    platforms = config["platforms"] + config["custom_stores"] 
    return render_template('index.html', platforms=platforms)

@app.route('/results', methods=['POST'])
def results():
    platform = request.form['platform']
    num_codes = int(request.form['num_codes'])
    # Add batch generation if you implement it!

    codes = generate_codes.generate_gift_card_codes(config, num_codes)
    return render_template('results.html', codes=codes)

if __name__ == '__main__':
    app.run(debug=True)
