#!/bin/bash

echo "Début des tests..."

# Test de la santé des conteneurs Docker
echo "Test de la santé des conteneurs Docker..."
docker-compose ps

# Test du bon fonctionnement des services
# Remplacez 'add-product-service', 'read-product-service', etc., par les noms réels de vos services
echo "Test du bon fonctionnement des services..."
curl -s http://projet_microservice-add-product-service-1:5000/add_product && echo "Service add-product OK" || echo "Service add-product échec zebi"
curl -s http://projet_microservice-read-product-service-1:5001/read_product && echo "Service read-product OK 2" || echo "Service read-product échec 2"
curl -s http://projet_microservice-display-product-service-1:5002/display_product && echo "Service display-product OK" || echo "Service display-product échec"

# Test du bon fonctionnement d'Elasticsearch
echo "Test du bon fonctionnement d'Elasticsearch..."
curl -s http://projet_microservice-elasticsearch-1:9200/ && echo "Elasticsearch OK" || echo "Elasticsearch échec"

# Test du bon fonctionnement de Kibana
echo "Test du bon fonctionnement de Kibana..."
curl -s http://kibana:5601/ && echo "Kibana OK" || echo "Kibana échec"

# Test du bon fonctionnement de Logstash
echo "Test du bon fonctionnement de Logstash..."
curl -s http://logstash:9600/ && echo "Logstash OK" || echo "Logstash échec"

echo "Tests terminés."
