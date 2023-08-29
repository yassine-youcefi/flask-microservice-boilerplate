from elasticsearch import Elasticsearch
from elasticsearch.exceptions import RequestError

class ElasticSearchUtils:
    def __init__(self, host='localhost', port='9200'):
        self.host = host
        self.port = port
        self.client = Elasticsearch(hosts=[{'host': host, 'port': port}])

    def search_index(self, index, query):
        try:
            response = self.client.search(index=index, body=query)
            return response['hits']['hits']
        except RequestError as e:
            # Handle Elasticsearch request error
            return []