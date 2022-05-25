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
## Semaine du 20/04
* Vacances
## Semaine du 27/04
* Finition du scénario
* création class soundManager qui gère l'aspect des musiques et sons
* nouveau paramètre dans map_register qui est sound
* le son est un attribut de la class Map() -> chaque map a sa musique
* quand teleport_player() -> changement de musique
* collision avec les npcs avec move_back()
* travail sur la création de maps (Maxime=6+, Ethan=1[village de départ])
* abandon des maps et sprite test pour utiliser les finaux
* réflexion récupération objects + écran début et fin jeu + autres
## Semaine du 04/05
* affichage de l'éran de début du jeu sans les boutons (en cours) avec une condition is_playing == True -> enlève l'écran de début
* la musique du monde n'apparait qu'après la fin de l'écran de démarrage ce qui permettra d'avoir une musique spécifique à l'écran de début
* Travail sur le design de l'écran de début par un ami
* création classe Ange() qui hérite de NPC(), les anges sont des ennemies qui téléportent le joueur
* ajout de l'attribut speed dans le constructeur de Entity(), chaque entitée aura une vitesse définit, l'animation du mvt s'ajustera à la vitesse car AnimateSprite() prend en attribut la vitesse.
* ajout des mêmes méthodes pour les anges que pour les npcs dans MapManager()
* nouveau paramètre dans map_register qui est anges + anges = attribut Map() en tant que list(Ange)
* 3/4 village de départ fini
* réglage des bugs des sprites (si un sprite possède des pixels noirs puisque set_colorkey(0,0,0), le sprite devient transparent -> set_colorkey(get_at((0,0))) et changement du fond des pngs pour choisir une couleur peu utiliser en arrière plan)
* changement du nom du jeu en "Liminal"
* travail sur toutes les autres maps (Tiled) par Maxime (c'est très long à faire)
## Semaine 11/05
* Devoirs communs
* Bac blanc FR
* mon anniversaire
* malade
* =(
## Semaine du 25/05
* ajout des maps finales avec npcs, anges, runes
* ajout de plusieurs fonction de vérification de collision ou d'état
* ajout d'états comme is_playing ou is_dreaming
* finition écran début pause fin
* réglage des bugs
* ajout des musqiques et des sons
* affiche le nombre de rune récupéré
* finition générale du jeu

# Inspirations et sources
* Yume Nikki pour map et musique
* ambiance dreamcore, weirdcore et liminal space
* spritesheet : rpg_maker.fr
* sons : banque de son
* tutos : graven, fab_tats, forums divers, site Tiled
* le step



