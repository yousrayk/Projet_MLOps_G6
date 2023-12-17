# Projet_MLOps_G6
## Detection of Microcalcifications in mammography
Projet MLOps_G6: Détection des Microcalcifications en mammographie

Le projet MLOps_G6 se concentre sur la détection des microcalcifications dans les mammographies, avec un processus bien défini et des étapes clés.

1. **Définition du Projet et Choix des Métriques:**
   Dans la première phase, le projet a été soigneusement défini, mettant l'accent sur la détection des microcalcifications en mammographie. Les métriques cruciales à surveiller ont été identifiées, notamment l'Accuracy, la Précision, le Recall et le F1, afin d'évaluer la performance du modèle de manière exhaustive.

2. **Acquisition et Exploration des Données:**
   Les données nécessaires ont été obtenues à partir du fichier "mammography.csv" disponible sur Kaggle. Une exploration approfondie de ces données a été entreprise pour comprendre leur nature et garantir leur adéquation pour le modèle.

3. **Modélisation avec RandomForestClassifier:**
   La phase de modélisation a impliqué l'identification du modèle le mieux adapté à la problématique, à savoir le RandomForestClassifier. Ce modèle préexistant a été intégré dans le fichier "modelML.ipynb". Le modèle a été exécuté sur le jeu de données sélectionné, et son comportement a été surveillé pendant la phase de production.

4. **Intégration de FastAPI pour une Gestion Efficace de l'API :**
   FastAPI a été choisi comme framework pour exposer l'API du modèle. Grâce à ses annotations de type et à sa documentation automatique, FastAPI facilite le développement, la validation des données, et assure une documentation interactive pour l'API.

5. **Utilisation de Docker pour l'Isolation et la Portabilité :**
   Docker a été intégré dans le processus pour encapsuler le modèle, assurant ainsi son isolation et sa portabilité. Cette approche garantit une cohérence dans le déploiement du modèle indépendamment de l'environnement.

6. **Déploiement en tant qu'API avec FastAPI et Surveillance avec Prometheus/Grafana:**
   Le modèle a été exposé en tant qu'API grâce à l'utilisation de la bibliothèque FastAPI, enseignée dans les cours MLOps et TDLOG. Le déploiement a été suivi d'une surveillance continue du modèle en production. La surveillance a été réalisée en utilisant le tandem Prometheus/Grafana, des outils puissants enseignés dans le cadre du cours MLOps. Des captures d'écran illustrant le processus de provisionnement et les résultats de la surveillance sont disponibles dans le dossier "Screenshots".

Ce processus complet, depuis la définition du projet jusqu'à la surveillance en production, démontre l'approche MLOps rigoureuse adoptée par l'équipe du Projet MLOps_G6 pour assurer le succès de la détection des microcalcifications en mammographie, en intégrant des outils tels que FastAPI, Docker, et le tandem Prometheus/Grafana.

Les membres de l'équipe sont: 
YAKHOU Yousra,
LAHRIOUI Adam,
MIDINE Zakaria,
KARIM Hiba,
R'BIB Marouan.
