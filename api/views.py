from config import settings
from flask import Flask, jsonify
from utils.elasticsearch import ElasticSearchUtils



app = Flask(__name__)
es_utils = ElasticSearchUtils(host=settings.ELASTICSEARCH_HOST, port=settings.ELASTICSEARCH_PORT)


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    print('Welcome ',settings.ELASTICSEARCH_PORT)

    index = 'property'
    query = {
        "query": {
            "match_all": {}
        }
    }
    
    results = es_utils.search_index(index, query)
    
    # Process the results and return as JSON
    response_data = [{'_id': hit['_id'], '_source': hit['_source']} for hit in results]
    return jsonify(response_data)

