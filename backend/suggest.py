# backend/suggest.py

from flask import Flask, request, jsonify
from elastic_client import get_es

app = Flask(__name__)
es = get_es()
INDEX_NAME = "suggestions"

@app.route("/suggest", methods=["GET"])
def suggest():
    query = request.args.get("q", "")
    if not query:
        return jsonify({"error": "Missing 'q' parameter"}), 400

    response = es.search(
        index=INDEX_NAME,
        size=5,
        body={
            "query": {
                "match_phrase_prefix": {
                    "query": query
                }
            }
        }
    )

    suggestions = [hit["_source"]["query"] for hit in response["hits"]["hits"]]
    return jsonify({"suggestions": suggestions})

if __name__ == "__main__":
    app.run(debug=True)
