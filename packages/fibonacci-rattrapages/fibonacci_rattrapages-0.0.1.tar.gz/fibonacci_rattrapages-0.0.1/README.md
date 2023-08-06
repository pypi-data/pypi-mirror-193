# M1-2022-rattrapage
## Evaluation

Vous serez évalués sur :
 * la réalisation technique : réussite des exercices demandés
 * La qualité des commits et PR que vous ferez. Vous devez suivre les bonnes pratiques vues en cours.

## Préparation
1. Faire un fork du projet : [https://github.com/rgt-yncrea/M1-2022-rattrapage](https://github.com/rgt-yncrea/M1-2022-rattrapage)
2. Vous effecturez les étapes suivantes sur le fork

## Modification du projet
1. Créer une branche _add_tests_ depuis la branche _dev_.
2. Dans le dossier _tests/_, créer un fichier _test_fibonacci.py_
3. Dans ce fichier, écrire des tests unitaires pour valider l'implémentation de la fonction _fibonacci_.
Vous utiliserez le framework de tests _pytest_
4. Merger la branche _add_tests_ dans la branche _dev_ . On souhaite conserver la branche --> pas de fast forward merge

## Création de workflow
### Vérification du _test coverage_
En vous inspirant du [projet](https://github.com/rgt-yncrea/M1-2022-git-workflow/) 
réalisé pour l'examen, créer un workflow permettant de générer un rapport de couverture de test pour chaque PR 
effectuée sur la branche dev.

### Build du projet 
Créer un workflow qui teste et build le projet lorsqu'un tag est effectué sur la branche _main_.

Par "build", on entend créer les archives .tar.gz et .whl qui pourront être ensuite publiée sur un repository (non demandé pour le projet).

Si les tests ne sont pas tous OK, le build ne doit pas être effectué.

## Pull Request

Lorsque vous aurez terminé votre travail, faites une PR sur le [repository d'origine](https://github.com/rgt-yncrea/M1-2022-rattrapage)
