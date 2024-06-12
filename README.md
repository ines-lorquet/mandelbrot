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

...

## Contexte

...

### Triangle de Sierpiński

Le **triangle de Sierpiński** est un motif fractal formé en répétant ce processus :

- Commencez avec un grand triangle.
- Divisez-le en quatre petits triangles en reliant les milieux des côtés.
- Enlevez le triangle central.
- Répétez ces étapes pour chaque petit triangle restant.

Le motif obtenu est un triangle avec une structure qui se répète à l'infini, de plus en plus petit.

### Mandelbrot

L'ensemble de **Mandelbrot** est une forme fractale complexe obtenue par un processus mathématique. Voici une explication simple :

- L'ensemble de Mandelbrot est défini par la formule : \[ z_{n+1} = z_n^2 + c \] où \( z \) et \( c \) sont des nombres complexes. Cette formule est répétée pour déterminer si le point \( c \) appartient à l'ensemble de Mandelbrot.

- Répétez l'équation pour voir si la valeur de 𝑧 reste finie ou devient infinie.

- Coloriez le point 𝑐 : Si 𝑧 reste finie, le point appartient à l'ensemble de Mandelbrot et est colorié en noir. Si 𝑧 devient infinie, le point est colorié en fonction de la vitesse à laquelle 𝑧 diverge.

Le résultat est une forme complexe et belle avec des motifs détaillés qui se répètent à l'infini lorsqu'on zoome.

### Julia

Les ensembles de **Julia** sont des formes fractales obtenues par des formules mathématiques. Voici une explication simple :

- Choisissez un point de départ sur le plan complexe.
- Appliquez une formule mathématique (itération) à ce point.
- Répétez la formule plusieurs fois.
- Coloriez le point selon la rapidité avec laquelle il s'éloigne.

Le résultat est un motif complexe et coloré qui se répète à différentes échelles, créant une structure fractale

### Flocon de neige de Koch

Le **flocon de neige de Koch** est un motif fractal créé en répétant un processus simple. Voici comment il est formé :

- Commencez avec un **triangle équilatéral**.

- Divisez chaque côté en trois **segments égaux**.

- **Remplacez le segment** du milieu par deux segments formant un angle, créant ainsi un petit triangle qui pointe vers l'extérieur.

- **Répétez** ces étapes pour chaque côté nouvellement formé.

En répétant ce processus encore et encore, le bord du flocon de neige devient de plus en plus complexe, créant une forme de flocon de neige détaillée et infiniment fine.

### Burning ship

Le "Burning Ship" est une fractale générée en utilisant une méthode itérative spécifique. Voici les étapes pour générer cette fractale :

- Commencez avec le **plan complexe** : Chaque point sur une grille représente un nombre complexe.

- **Appliquez une formule spécifique** : Pour chaque point \( (x, y) \) sur la grille, utilisez la formule itérative suivante :
\[ z_{n+1} = (|Re(z_n)| + i|Im(z_n)|)^2 + c \] où \( z_0 = 0 \) et \( c \) est le point complexe \( (x, y) \). Ici, \( Re(z_n) \) et \( Im(z_n) \) sont les parties réelle et imaginaire de \( z_n \), et \( |\cdot| \) indique la valeur absolue.

- **Répétez l'itération** : Répétez cette formule pour chaque point jusqu'à ce que le résultat s'échappe à l'infini (ou jusqu'à un nombre maximum d'itérations).

- **Attribuez des couleurs** : Les points qui ne s'échappent pas après le nombre maximum d'itérations sont colorés d'une manière spécifique, tandis que ceux qui s'échappent sont colorés différemment.

Le résultat est une image complexe et souvent spectaculaire, qui ressemble à un navire en feu, d'où son nom "Burning Ship" (navire en feu).
