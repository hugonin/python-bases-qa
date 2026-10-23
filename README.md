# Python bases QA

## Objectif
Exercice de consolidation Python dans le cadre de ma montée en compétence vers l'automatisation de tests

## Contenu
Le fichier resultats.py est composé d'une liste de résultats de test et de 5 fonctions:
*  ``` percentage_success```: taux de réussite en pourcentage, hors tests ignorés
*  ``` failed_ids```: liste des identifiants en échec
*  ``` count_by_module```: nombre de test par module
*  ``` test_le_plus_long```:  test le plus long
*  ``` check_statuts```: lève une erreur explicite si un statut inconnu apparaît dans la liste

## Lancer le script
```python resultats.py```

## Ce que j'ai appris
* Une fonction doit retourner une valeur pour être exploitée (return au lieu de print)
* Manipulation des dictionnaires
* Lire un traceback
* Un test qui passe avec un seul jeu de données peut masquer un bug, comme je l’ai constaté sur ```test_le_plus_long```