from flask import Flask, jsonify

app = Flask(__name__)

items = [{"id": 1, "name": "Item One"}, {"id": 2, "name": "Item Two"}]

@app.route("/api/items")
def get_items():
    return jsonify(items)

if __name__ == "__main__" :
    app.run(debug = True)
