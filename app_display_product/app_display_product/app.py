from flask import Flask, render_template
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError
import logging
from datetime import datetime

app = Flask(__name__)

# Configuration du Logger pour écrire dans le fichier logs.csv à la racine du projet
logging.basicConfig(filename='logs.csv', level=logging.INFO, format='%(asctime)s, %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Paramètres de connexion Elasticsearch
es_host = 'projet_microservice-elasticsearch-1'  # Adresse de l'hôte Elasticsearch
es_port = 9200  # Port par défaut d'Elasticsearch
es_scheme = 'http'
# Créer une instance d'Elasticsearch
es = Elasticsearch([{'host': es_host, 'port': es_port, 'scheme': es_scheme}])

@app.route('/products', methods=['GET'])
def list_products():
    logging.info("API /products appelée")
    # Récupérer les produits depuis Elasticsearch
    try:
        search_result = es.search(index="products", body={"query": {"match_all": {}}})
        products_list = [doc['_source'] for doc in search_result['hits']['hits']]
    except NotFoundError:
        # Gérer l'exception
        products_list =  []
    # Extraire les documents de la réponse
    
    return render_template('products.html', products=products_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
