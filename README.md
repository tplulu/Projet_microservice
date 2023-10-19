# Projet_microservice

Rapport de Mi-Parcours

Vous trouverez dans le projet un schéma de l'organisation des containers et de leurs utilité.

Description du Projet

Le projet en cours est une application de gestion de produits basée sur une architecture de microservices. L'objectif est de créer une application web où les utilisateurs peuvent ajouter de nouveaux produits, afficher une liste de produits et les détails associés, le tout stocké dans une base de données MySQL. Le projet est scindé en plusieurs services distincts pour suivre une approche de microservices, ce qui permet une évolutivité et une maintenance faciles.

Architecture

Microservices
Service d'Ajout de Produits (Add-Product-Service) : Ce service est chargé de gérer l'ajout de nouveaux produits dans la base de données. Il expose une API POST pour ajouter un produit et communique avec la base de données pour stocker les informations du produit.

Service de Lecture des Produits (Read-Product-Service) : Ce service récupère la liste des produits depuis la base de données et expose une API GET pour afficher ces produits. Il communique avec la base de données pour lire les informations des produits.

Service d'Affichage de Produits (Display-Product-Service) : Ce service est responsable de la création d'une interface utilisateur pour afficher les produits de manière organisée. Il communique avec le service de lecture des produits pour récupérer les données des produits.

Base de Données
Nous utilisons une base de données MySQL pour stocker les informations des produits. Les produits sont stockés dans une table nommée "product," qui contient des colonnes telles que l'ID, le nom, la description et le prix des produits.

Conteneurs Docker
Chaque service est encapsulé dans un conteneur Docker distinct pour assurer un environnement isolé. Nous utilisons Docker Compose pour gérer et exécuter ces conteneurs de manière cohérente.

Technologies Utilisées
    -Flask : Un framework Python léger pour la création d'API web et d'applications web.
    -Flask-SQLAlchemy : Une extension pour Flask qui simplifie l'interaction avec les bases de données SQLAlchemy.
    -MySQL : Une base de données relationnelle pour stocker les informations sur les produits.
    -Docker : Une plateforme de conteneurs pour encapsuler les services, simplifiant le déploiement et la gestion.
    -Docker Compose : Un outil pour définir et gérer des applications multi-conteneurs.

Progrès Accomplis
    Jusqu'à présent, nous avons créé trois services distincts (Ajout de produits, Lecture des produits et Affichage de produits) et configuré une base de données MySQL pour stocker les produits. Les services d'Ajout et de Lecture de produits fonctionnent avec des API REST, tandis que le service d'Affichage de produits fournit une interface utilisateur pour une expérience conviviale.

Prochaines Étapes
Les prochaines étapes du projet comprennent :

Intégration de tests automatisés pour garantir la stabilité.
Déploiement sur un serveur en production.


Rapport de fin - Projet Microservices

Introduction
Ce rapport détaille le projet de développement full stack en architecture microservices réalisé conformément aux spécifications fournies. L'objectif de ce projet était de créer une application composée de différents composants techniques pour démontrer une architecture microservices. Les principaux composants de l'application comprennent un frontend, un backend avec une base de données, une architecture Docker, un orchestrateur de conteneurs, un service de reverse proxy, des tests et des éléments de production. Ce rapport mettra en évidence les composants que nous avons réalisés.

Composants Techniques de Base
Frontend : Nous avons développé un frontend qui propose au moins deux routes, y compris une page d'accueil et une route générique. Les routes sont accessibles via des URL distinctes.

Backend et Base de Données : Notre backend est doté d'une base de données dans un conteneur spécifique. Nous avons choisi une base de données mysql, qui est fonctionnelle et comprend au moins une table avec un schéma explicite.

Dockerfiles : Notre projet contient au moins 2 Dockerfiles, l'un pour le frontend et l'autre pour le backend.

Docker Compose : Nous avons créé un fichier docker-compose.yml pour l'orchestration de nos conteneurs.

Images Docker : Nous avons créé des images Docker pour nos composants et les avons poussées sur Docker Hub. Les images peuvent être consultées publiquement à l'adresse [mentionnez l'URL de l'image].

Tests : Nous avons mis en place des fichiers de test qui vérifient la santé de nos conteneurs, le bon fonctionnement de l'application frontend et backend, ainsi que le bon fonctionnement de la base de données.

Architecture
Nous avons schématisé l'architecture de notre projet, en incluant :

Les différents composants/services de l'application.
Les liens entre ces composants/services, y compris les protocoles et les types de requêtes (POST, GET, etc.).
Les ports exposés du côté client et du côté backend.
Notre projet est accessible via une connexion sécurisée SSL/HTTPS.

Automatisation des Tests : Nous avons automatisé des tests dans notre fichier docker-compose.yml.


README.md : Notre README.md à la racine de notre dépôt GitHub contient des instructions complètes pour construire et exécuter le projet. Il offre également une démonstration en ligne sans erreur.

Conclusion
En conclusion, ce projet a permis de créer une application en architecture microservices avec un frontend, un backend, une base de données, une architecture Docker, des tests et des éléments de production. Il est déployé sur un fournisseur Cloud et est accessible en ligne. Ce projet a été réalisé en respectant les meilleures pratiques de développement et d'architecture microservices.