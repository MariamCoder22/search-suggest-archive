# elasticsearch/create_index.py

from elasticsearch import Elasticsearch
import json

# Constants
INDEX_NAME = "suggestions"
ES_HOST = "http://localhost:9200"

# Connect to Elasticsearch
es = Elasticsearch(ES_HOST)

# Load mapping and analyzer config
with open("elasticsearch/index_config.json") as f:
    index_config = json.load(f)

# Delete index if it already exists
if es.indices.exists(index=INDEX_NAME):
    print(f"Deleting existing index: {INDEX_NAME}")
    es.indices.delete(index=INDEX_NAME)

# Create new index with mapping and analyzers
print(f"Creating new index: {INDEX_NAME}")
es.indices.create(index=INDEX_NAME, body=index_config)

print("✅ Index created successfully.")
