# scripts/index_data.py

import csv
from elasticsearch import Elasticsearch

ES_HOST = "http://localhost:9200"
INDEX_NAME = "suggestions"
DATA_FILE = "data/mock_search_logs.csv"

es = Elasticsearch(ES_HOST)

def index_data():
    with open(DATA_FILE, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            query_text = row['query']
            doc = {"query": query_text}
            es.index(index=INDEX_NAME, body=doc)
            print(f"Indexed: {query_text}")

if __name__ == "__main__":
    index_data()
