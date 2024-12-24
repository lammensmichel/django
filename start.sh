#!/bin/bash

# Vérifier si Docker et Docker Compose sont installés
if ! [ -x "$(command -v docker)" ]; then
  echo "Docker n'est pas installé. Veuillez l'installer avant de continuer."
  exit 1
fi

if ! [ -x "$(command -v docker-compose)" ]; then
  echo "Docker Compose n'est pas installé. Veuillez l'installer avant de continuer."
  exit 1
fi

# Vérifiez si le fichier manage.py existe déjà dans le répertoire
if [ -f "manage.py" ]; then
  echo "Le projet Django existe déjà. Aucun nouveau projet ne sera créé."
else
  echo "Aucun projet Django trouvé. Création du projet..."
  # Exécuter la commande pour créer un nouveau projet Django
  docker-compose run --rm web django-admin startproject myproject .
fi

# Lancer docker-compose
echo "Lancement des services Docker Compose..."
docker-compose up 
