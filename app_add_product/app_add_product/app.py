from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ElasticsearchException
import json
import uuid

app = Flask(__name__)

# Configuration Elasticsearch
es_host = 'projet_microservice-elasticsearch-1'
es_port = 9200
es_scheme = 'http'
es = Elasticsearch([{'host': es_host, 'port': es_port, 'scheme': es_scheme}])

@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.get_json()
    unique_id = str(uuid.uuid4())

    # Création d'un document pour Elasticsearch
    product_document = {
        'id': unique_id,
        'name': data['name'],
        'description': data['description'],
        'prix': data['prix']
    }

    try:
        # Ajouter le document à l'index 'products'
        response = es.index(index='products', body=product_document)
        return jsonify({'message': 'Product added successfully', 'id': response['_id']}), 201
    except ElasticsearchException as e:
        print("Error adding product to Elasticsearch:", str(e))
        return jsonify({'message': 'Error adding product to Elasticsearch'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
