# Mises à jour :
## Semaine du 24/02
* création fenêtre jeu
* création boucle infinie
* importation pygame, pyscroll, pytmx
* création test "carte" sur Tiled
* séparation des fichier avec les class
* création class "game" et class "player"
* création sprite test "player"
* ajout du "player" sur "carte"
* fonctions de déplacement du joueur
* management des différentes couche de calque sur Tiled
* ajout point de spawn
## Semaine du 30/03
* organisation des fichier dans des dossiers (refactor)
* ajout des collision (feet)
* fonction move_back() qui ramène à old_position (save_location) au lieu de -x
* sprite de direction du joueur (get_image -> sprite sheet)
* début classe "animation" (test)
* utilisation de super()
* début class "Map" chargée de s'occuper du stockage des maps et du switch entre deux (test)
* correction de bugs sur Tiled
## Semaine du 06/04
* gestion des map terminée (MapManager, Map, Portal)
* déplacement du code collision et relatif à la map de game.py à map.py
* création carte en cours + recherche pour passer derrière les batiments à plusieurs étages (Maxime)
* test switch_world avec la nouvelle gestion (house = test)
* utilisation décorateurs (@dataclass)
* Problèmes de PC
## Semaine du 13/04
* création donjon test + house2 -> switch world OK
* class Animation -> NPC, player à l'aide des coordonnées de la sprite sheet OK
* class Dialogue -> f(perso) OK
* fonctionnalité de dialogues en appuyant sur space devant un NPC (space pour passer)
* découpage des bâtiments avec un calque diff pour passer derrière
* class Entity -> généralise class Player pour tous entité (NPC, player)
* class Map -> register_map(...,npcs)
* mvt des NPC grâce à un chemin prédéfini (test)
* recherches importation musique + collision NPC + objects à récupérer
* réfléxion quant au scénario du jeu final

