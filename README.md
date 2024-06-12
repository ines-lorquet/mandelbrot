# mandelbrot

# Fractales

## Table des matières

- [Un système de résolution automatique de grille de Sokoban ](#un-système-de-résolution-automatique-de-grille-de-sokoban)
  - [Table des matières](#table-des-matières)
  - [L'équipe](#léquipe)
  - [Sokoban](#sokoban)
  - [Contexte](#contexte)
  - [Automatisation](#automatisation)

## L'équipe
3 étudiants en 1ère année de Bachelor IT spécialité Intelligence Artificielle à [La Plateforme_](https://laplateforme.io/) à Marseille

- Said Kheloufi
  <a href="https://www.linkedin.com/in/said-kheloufi/">
    <img src="images/linkedin.png" width=25>
  </a>
  <a href="https://github.com/said-kheloufi">
    <img src="images/github.png" width=25>
  </a>

- Ines Lorquet
  <a href="https://www.linkedin.com/in/ines-lorquet-35b90128b/">
    <img src="images/linkedin.png" width=25>
  </a>
  <a href="https://github.com/ines-lorquet">
    <img src="images/github.png" width=25>
  </a>

- Bruno Coulet
  <a href="https://www.linkedin.com/in/bruno-coulet-35b90128b/">
    <img src="images/linkedin.png" width=25>
  </a>
  <a href="https://github.com/bruno-coulet">
    <img src="images/github.png" width=25>
  </a>

## Fractales

Sokoban est un jeu vidéo de réflexion classique dans lequel le joueur incarne un manutentionnaire chargé de déplacer des caisses dans un entrepôt. L'objectif est de pousser toutes les caisses vers des emplacements cibles prédéfinis, marqués par des points ou des cases spécifiques. Le joueur ne peut pousser qu'une seule caisse à la fois et ne peut pas les tirer, ce qui ajoute une dimension stratégique et demande de planifier soigneusement chaque mouvement. Sokoban est connu pour ses niveaux de difficulté croissante et pour le défi intellectuel qu'il pose aux joueurs.

## Contexte

...

### Triangle de Sierpiński

Le triangle de Sierpiński est un motif fractal formé en répétant ce processus :

- Commencez avec un grand triangle.
- Divisez-le en quatre petits triangles en reliant les milieux des côtés.
- Enlevez le triangle central.
- Répétez ces étapes pour chaque petit triangle restant.

Le motif obtenu est un triangle avec une structure qui se répète à l'infini, de plus en plus petit.

### Mandelbrot


ChatGPT
L'ensemble de Mandelbrot est une forme fractale complexe obtenue par un processus mathématique. Voici une explication simple :

Commencez avec une équation simple : 
𝑧
𝑛
+
1
=
𝑧
𝑛
2
+
𝑐
z 
n+1
​
 =z 
n
2
​
 +c, où 
𝑧
z et 
𝑐
c sont des nombres complexes.
Choisissez un point 
𝑐
c sur le plan complexe.
Répétez l'équation pour voir si la valeur de 
𝑧
z reste finie ou devient infinie.
Coloriez le point 
𝑐
c : Si 
𝑧
z reste finie, le point appartient à l'ensemble de Mandelbrot et est colorié en noir. Si 
𝑧
z devient infinie, le point est colorié en fonction de la vitesse à laquelle 
𝑧
z diverge.

Le résultat est une forme complexe et belle avec des motifs détaillés qui se répètent à l'infini lorsqu'on zoome.

### Julia

### Flocon de neige de Koch

### Burning ship



# auto-sokoban# Lingua Franca
# Jeu Sokoban avec résolution automatique

## Table des matières

- [Un système de résolution automatique de grille de Sokoban ](#un-système-de-résolution-automatique-de-grille-de-sokoban)
  - [Table des matières](#table-des-matières)
  - [L'équipe](#léquipe)
  - [Sokoban](#sokoban)
  - [Contexte](#contexte)
  - [Automatisation](#automatisation)

## L'équipe
3 étudiants en 1ère année de Bachelor IT spécialité Intelligence Artificielle à [La Plateforme_](https://laplateforme.io/) à Marseille

- Said Kheloufi
  <a href="https://www.linkedin.com/in/said-kheloufi/">
    <img src="images/linkedin.png" width=25>
  </a>
  <a href="https://github.com/said-kheloufi">
    <img src="images/github.png" width=25>
  </a>

- Ines Lorquet
  <a href="https://www.linkedin.com/in/ines-lorquet-35b90128b/">
    <img src="images/linkedin.png" width=25>
  </a>
  <a href="https://github.com/ines-lorquet">
    <img src="images/github.png" width=25>
  </a>

- Bruno Coulet
  <a href="https://www.linkedin.com/in/bruno-coulet-35b90128b/">
    <img src="images/linkedin.png" width=25>
  </a>
  <a href="https://github.com/bruno-coulet">
    <img src="images/github.png" width=25>
  </a>

## Sokoban

Sokoban est un jeu vidéo de réflexion classique dans lequel le joueur incarne un manutentionnaire chargé de déplacer des caisses dans un entrepôt. L'objectif est de pousser toutes les caisses vers des emplacements cibles prédéfinis, marqués par des points ou des cases spécifiques. Le joueur ne peut pousser qu'une seule caisse à la fois et ne peut pas les tirer, ce qui ajoute une dimension stratégique et demande de planifier soigneusement chaque mouvement. Sokoban est connu pour ses niveaux de difficulté croissante et pour le défi intellectuel qu'il pose aux joueurs.

## Contexte

...

### Automatisation

Automatiser le jeu Sokoban présente plusieurs avantages intéressants :

  - **Recherche en Intelligence Artificielle** : Sokoban est un excellent banc d'essai pour les algorithmes d'intelligence artificielle et d'apprentissage automatique. En automatisant Sokoban, les chercheurs peuvent tester et affiner des techniques d'IA pour la planification, la recherche de chemin, et la prise de décision.

  - **Analyse de Niveaux**Les outils automatisés peuvent analyser des milliers de niveaux de Sokoban pour identifier des schémas et des stratégies de résolution courantes. 

  - **Optimisation des Stratégies** : Un code peut explorer différentes stratégies de résolution et optimiser les mouvements pour minimiser le nombre de coups nécessaires ou le temps de résolution.

  - **Accessibilité** :  Automatiser certaines parties du jeu peut rendre Sokoban plus accessible à des personnes qui trouvent les niveaux trop difficiles ou qui ont des limitations physiques les empêchant de jouer manuellement.

L'automatisation du jeu Sokoban ouvre de nombreuses opportunités pour la recherche, l'éducation, et l'amélioration des expériences de jeu, tout en proposant des défis intellectuels et techniques stimulants.

  

  
