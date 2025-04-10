# scripts/test_query.py

from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

query = input("Enter prefix to search: ")
response = es.search(
    index="suggestions",
    body={
        "query": {
            "match": {
                "query": {
                    "query": query
                }
            }
        }
    }
)

print("Suggestions:")
for hit in response["hits"]["hits"]:
    print("-", hit["_source"]["query"])
