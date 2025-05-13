# Flask File Upload - Vulnérabilité d'upload non filtrée

Ce projet est une mini application Flask volontairement vulnérable aux attaques de type **upload de fichier malicieux**.
Il permet d'expérimenter des vecteurs classiques d'exécution de code à distance via des fichiers `.php`, `.jpg.php`, `.phtml`, etc.

---

## Fonctionnement

- Un formulaire permet d'uploader un fichier sans aucun filtrage :
  - Pas de vérification de l'extension
  - Pas de vérification du type MIME
  - Pas de nettoyage du nom de fichier
- Le fichier est stocké dans le dossier `uploads/`, accessible via le serveur

---

### Installation
```bash
git clone https://github.com/AndyDCK/flask-upload-vuln.git
cd flask-upload-vuln
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
```bash
python app.py
```

### Via Apache+PHP (Docker)
Flask ne peut pas exécuter les fichiers .php
Voici comment utiliser Docker pour tester le shell dans un vrai serveur Apache :

### Commandes
```bash
docker build -t php-upload .
docker run -d -p 8080:80 php-upload
```

On peut ensuite accéder au shell via:
http://localhost:8080/uploads/shell.php?cmd=id
