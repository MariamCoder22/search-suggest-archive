# backend/elastic_client.py

from elasticsearch import Elasticsearch

def get_es():
    return Elasticsearch("http://localhost:9200")
