from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/data')
def data():
    with open('network_data.json', encoding='utf-8') as f:
        graph = json.load(f)
    return jsonify(graph)

if __name__ == '__main__':
    app.run(debug=True)
