python 3.10.0

# Base de données MySql

 - Créer une table "django"

# Environnement virtuel

 - python -m venv venv
 - .\venv\Scripts\activate
 - python pip install -r requirements.txt

# Ficher .env

 - Créer à la racine un fichier .env avec les variables si dessous :
 - NAME = nom de la table
 - USER = login
 - PASSWORD = mot de passe
 - HOST = ip du serveur
 - PORT = port du serveur
 - ca-cert = chemin vers ca-cert
 - client-client = chemin vers client-client
 - client-key = chemin vers client-key

# Migration

 - python manage.py makemigrations (si neccessaire)
 - python manage.py migrate

# Lancer le serveur

 - python manage.py runserver
