# Mémoire de master 2 en *Technologies numériques appliquées à l'histoire* à l'École nationale des Chartes

Ce mémoire est intitulé *Modélisation, enrichissement sémantique et diffusion d'un corpus 
textuel semi-structuré: le cas des catalogues de vente de manuscrits*. Il a été réalisé
à l'occasion de mon stage de fin d'études au sein du projet 
[Manuscript Sales Catalogues](https://odhn.ens.psl.eu/en/article/mss-rereading-history-literary-canon)
/ [Katabase](https://katabase.huma-num.fr/) à l'École normale supérieure.

---

## Structure du dépôt

Le mémoire et la présentation de soutenance sont disponibles en `pdf` à la racine, le 
code `LaTeX` utilisé pendant la rédaction se trouve dans `texte_sources/` (pour le texte)
et `presentation_sources/` pour la présentation de soutenance; les livrables techniques dans 
`livrables/`. Il est à noter que des extraits de code et de données brutes sont également 
présents dans les annexes de ce mémoire. 

```
racine du dossier
  |__paulkervegan_memoire.pdf : le mémoire au format PDF
  |__LICENSE : la licence sous laquelle ce mémoire est disponible
  |__README.md : le présent document
  |
  |__livrables/ : les livrables techniques
  |    |__3_WikidataEnrichment/ : le code pour la résolution d'entités nommées à l'aide de Wikidata
  |    |__Application/ : le code de l'application Katabase et de son API
  |    |__README.md : un document détaillant le contenu des livrables
  |
  |__presentation_sources/ : le code LaTeX du support de présentation
  |    |__includes/ : les fichiers inclus dans la présentation
  |    |__*.sty : les feuilles de styles du thème `hector` (voir plus bas)
  |    |__paulkervegan_presentation.pdf : la présentation en PDF
  |    |__paulkervegan_presentation.tex : le code de la présentation LaTeX
  |
  |__texte_sources/ : le code LaTeX du présent mémoire
       |__annexes/ : les documents présents en annexes
       |__bibliographie/ : les fichiers `.bib` contenant la bibliographie utilisée dans ce mémoire
       |__code/ : le code exécutable et les données brutes présentées dans le mémoire ou le code utilisé pour produire des données utilisées dans le mémoire
       |__img/ : les images utilisées dans le corps du texte
       |__paulkervegan_memoire.pdf : le PDF de ce mémoire
       |__*.tex : les fichiers `.tex` composant ce mémoire
       |__clean_aux.sh : un court script shell
```

---

## Résumé

Le présent mémoire présente certains aspects d'une chaîne de traitement consacrée à un 
corpus de catalogues de vente de manuscrits datant du XIXe siècle au début du XXe siècle. 
Ces catalogues forment un corpus de données semi-structurées, puisqu'ils sont organisés 
sous la forme d'une liste de manuscrits qui sont toujours décrits de façon semblable.
Grâce à cette nature semi-structurée des documents, il est possible de développer une 
chaîne de traitement entièrement basée sur la détection de motifs, c'est-à-dire sur 
l'identification d'éléments récurrents d'une entrée à l'autre. 

Le fil conducteur de ce 
mémoire est donc une analyse de la manière dont la nature semi-structurée du corpus peut 
être mobilisée pour analyser, manipuler et diffuser des données textuelles. 

Le présent texte s'intéresse notamment à la manière dont les documents sont encodés et 
aux aspects des catalogues imprimés qui sont sélectionnés pour produire un encodage 
manipulable automatiquement. Ensuite, ce mémoire présente une chaîne de traitement pour 
aligner les noms d'auteur.ice de manuscrits mentionné.e.s dans les catalogues avec la 
base de connaissance en ligne *Wikidata*. Cette chaîne de traitement s'appuie sur des 
algorithmes de détection et de transformation de motifs dans le texte, ainsi que sur 
un algorithme faisant des recherches sur l'API de Wikidata. Elle permet de constituer à 
l'aide de `SPARQL` une base de connaissances. Celle-ci servira notamment à mener une étude 
des facteurs biographiques influençant le prix des manuscrits. Enfin est présenté le 
fonctionnement de *KatAPI*, une API pour le partage automatisé de données produites par 
le projet. En plus de présenter les standards sur lesquels s'appuie cette API sont 
décrits les principes architecturaux et le fonctionnement interne de l'application.

---

## Mots clés

catalogues de vente, *Manuscript Sales Catalogues / Katabase*, traitement automatisé du 
langage, détection de motifs, Web sémantique, *Linked Open Data*, API, FAIR, REST

---

## Thème `hector` de la présentation

La présentation a été réalisée en utilisant un thème `LaTeX / beamer` conçu à l'occasion. 
Il peut être librement repris, adapté et réutilisé pour une autre présentation `LaTeX`. 
Il suffit de copier les fichiers `presentation_sources/*.sty` dans un dossier contenant le 
code `LaTeX` pour une présentation et de pointer vers ce thème dans le préambule:

```tex
\usetheme{hector}
```

---

## Citer ce mémoire

```bibtex
@thesis{kervegan_modelisation_2022,
        location = {Paris},
        title = {Modélisation, enrichissement sémantique et diffusion d'un corpus textuel semi-structuré: le cas des catalogues de vente de manuscrits},
        url = {https://github.com/paulhectork/tnah2022_memoire/},
        pagetotal = {195},
        institution = {École nationale des Chartes},
        type = {Mémoire pour le diplôme de master "Technologies numériques appliquées à l'histoire"},
        author = {Kervegan, Hector, Paul},
        urldate = {2022-09-02},
        date = {2022}
}
```
