# backend/suggest.py

from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch("http://localhost:9200")

@app.route("/suggest", methods=["GET"])
def suggest():
    query = request.args.get("q", "")
    if not query:
        return jsonify([])

    response = es.search(index="archived_suggest", body={
        "query": {
            "match_phrase_prefix": {
                "content": query
            }
        }
    })

    suggestions = [hit["_source"]["content"] for hit in response["hits"]["hits"]]
    return jsonify(suggestions)

if __name__ == "__main__":
    app.run(debug=True)
