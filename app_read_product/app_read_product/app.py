from flask import Flask, jsonify
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError

app = Flask(__name__)

# Configuration du client Elasticsearch
es_host = 'projet_microservice-elasticsearch-1'  # Adresse de l'hôte Elasticsearch
es_port = 9200  # Port par défaut d'Elasticsearch
es_scheme = 'http'
es = Elasticsearch([{'host': es_host, 'port': es_port, 'scheme': es_scheme}])

@app.route('/read_product', methods=['GET'])
def read_product():
    try:
        # Récupérer les produits depuis Elasticsearch
        search_result = es.search(index="products", body={"query": {"match_all": {}}})
        products = [doc['_source'] for doc in search_result['hits']['hits']]
    except NotFoundError:
        # Si l'index n'existe pas, renvoyer une liste vide ou un message d'erreur
        return jsonify({'error': 'Products not found'}), 404

    # Convertir les résultats en format JSON
    product_list = []
    for product in products:
        product_data = {
            'id': product.get('id'),
            'name': product.get('name'),
            'description': product.get('description'),  
            'prix': product.get('prix')
        }
        product_list.append(product_data)

    return jsonify({'products': product_list})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
