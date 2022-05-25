from dataclasses import dataclass
from random import randint
import pygame, pytmx, pyscroll

from src.entity import NPC, Player, Ange, Rune
from src.sounds import SoundManager


@dataclass
class Portal:
    from_world: str
    origin_point: str
    target_world: str
    teleport_point: str

@dataclass
class Map:
    name: str
    walls: list[pygame.Rect]
    group: pyscroll.PyscrollGroup
    tmx_data: pytmx.TiledMap
    portals: list[Portal]
    npcs: list[NPC]
    anges: list[Ange]
    runes: list[Rune]
    sound: str

class MapManager:

    def __init__(self, screen, player):
        self.screen = screen
        self.player = player
        self.maps = dict()  # 'house' -> Map("house", walls, group)
        self.current_map = "Teiko"
        self.liste_dreamap = ["dreamworld"]
        self.sound_manager = SoundManager()
        self.liste_rune = []

        self.register_map("world", "ADT", portals=[
            Portal(from_world="world", origin_point="enter_house", target_world="house", teleport_point="spawn_house"),
            Portal(from_world="world", origin_point="enter_house2", target_world="house2", teleport_point="spawn_house"),
            Portal(from_world="world", origin_point="enter_dungeon", target_world="dungeon", teleport_point="spawn_dungeon")
        ], npcs=[
            NPC("paul", "boby", speed=1, nb_points=2, dialog=["Il n'a fait que me suivre", "J'ai eu peur", "maintenant il en a après toi"])
        ], runes=[
            Rune("rune_world")
        ])
        self.register_map("house", "snowworld", portals=[
            Portal(from_world="house", origin_point="exit_house", target_world="world", teleport_point="enter_house_exit")
        ], runes=[
            Rune("rune_house")
        ])
        self.register_map("house2", "snowworld", portals=[
            Portal(from_world="house2", origin_point="exit_house", target_world="world", teleport_point="enter_house2_exit")
        ], npcs=[
            NPC("npc_house2", "bobeille", speed=0, nb_points=1, dialog=["Lorem ipsum dolor sit amet", "Qui modi praesentium aut suscipit consequatur", "sit praesentium voluptatum quo dignissimos impedit", "nam veniam esse aut quia assumenda"])
        ])
        self.register_map("dungeon", "dungeon", portals=[
            Portal(from_world="dungeon", origin_point="exit_dungeon", target_world="world", teleport_point="enter_dungeon_exit"),
            Portal(from_world="dungeon", origin_point="enter_Teikodream", target_world="Teikodream",
                   teleport_point="spawn_Teikodream")
        ], runes=[
            Rune("rune_dungeon")
        ], anges=[
            Ange("ange_dungeon", "ange", speed=1, nb_points=4)
        ])
        self.register_map("Teiko", "hell", portals=[
            Portal(from_world="Teiko", origin_point="teleport_Teiko", target_world="Teiko", teleport_point="player"),
            Portal(from_world="Teiko", origin_point="house-1_enter", target_world="house-1",
                   teleport_point="house-1_spawn"),
            Portal(from_world="Teiko", origin_point="house-2_enter", target_world="house-2",
                   teleport_point="house-2_spawn"),
            Portal(from_world="Teiko", origin_point="house-3_enter", target_world="house-3",
                   teleport_point="house-3_spawn"),
            Portal(from_world="Teiko", origin_point="house-main_enter", target_world="house-main",
                   teleport_point="house-main_spawn")
        ])
        self.register_map("house-1", "room2", portals=[
            Portal(from_world="house-1", origin_point="house-1_exit", target_world="Teiko", teleport_point="house-1_spawn_exit")
        ])
        self.register_map("house-2", "room2", portals=[
            Portal(from_world="house-2", origin_point="house-2_exit", target_world="Teiko",
                   teleport_point="house-2_spawn_exit")
        ])
        self.register_map("house-3", "room2", portals=[
            Portal(from_world="house-3", origin_point="house-3_exit", target_world="Teiko",
                   teleport_point="house-3_spawn_exit")
        ])
        self.register_map("house-main", "room2", portals=[
            Portal(from_world="house-main", origin_point="house-main_exit", target_world="Teiko",
                   teleport_point="house-main_spawn_exit")
        ])
        self.register_map("Laboratoire_-_version_finito", "number_world", portals=[
            Portal(from_world="Laboratoire_-_version_finito", origin_point="enter_salle_disco", target_world="salle_disco",
                   teleport_point="spawn_salle_disco1"),
            Portal(from_world="Laboratoire_-_version_finito", origin_point="teleport_labo1", target_world="Laboratoire_-_version_finito",
                   teleport_point="spawn_teleport_labo1"),
            Portal(from_world="Laboratoire_-_version_finito", origin_point="teleport_labo2", target_world="Laboratoire_-_version_finito",
                   teleport_point="spawn_teleport_labo2"),
            Portal(from_world="Laboratoire_-_version_finito", origin_point="enter_Teikodream2", target_world="Teikodream",
                   teleport_point="spawn_Teikodream2")
        ], runes=[
            Rune("rune_labo1"),
            Rune("rune_labo2"),
            Rune("rune_labo3"),
            Rune("rune_labo4")
        ], anges=[
            Ange("ange_labo1", "ange", speed=1, nb_points=2),
            Ange("ange_labo2", "ange", speed=1, nb_points=2),
            Ange("ange_labo3", "ange", speed=1, nb_points=2),
            Ange("ange_labo4", "ange", speed=1, nb_points=2),
            Ange("ange_labo5", "ange", speed=1, nb_points=2),
            Ange("ange_labo6", "ange", speed=1, nb_points=2),
            Ange("ange_labo7", "ange", speed=1, nb_points=4)
        ], npcs=[
            NPC("npc_labo1", "boba", speed=0, nb_points=1, dialog=["J'ai découvert un passage secret", "il est derrière les téléporteurs"])
        ])
        self.register_map("salle_disco", "YSBD", portals=[
            Portal(from_world="salle_disco", origin_point="enter_laboratory2", target_world="Laboratoire_-_version_finito",
                   teleport_point="spawn_laboratory2")
        ], runes=[
            Rune("rune_disco")
        ], npcs=[
            NPC("npc_disco1", "boba", speed=1, nb_points=2, dialog=["Tu es venu danser ?"]),
            NPC("npc_disco2", "bob", speed=1, nb_points=4, dialog=["Boogie Woogie !", "Passion Step !"])
        ])
        self.register_map("darkworld", "eyeball", portals=[
            Portal(from_world="darkworld", origin_point="enter_forest1", target_world="forest_world",
                   teleport_point="spawn_forest"),
            Portal(from_world="darkworld", origin_point="enter_glitchworld", target_world="glitchworld",
                   teleport_point="spawn_glitchworld"),
            Portal(from_world="darkworld", origin_point="enter_dreamworld", target_world="dreamworld",
                   teleport_point="spawn_exit_darkworld")
        ], runes=[
            Rune("rune_darkworld")
        ], npcs=[
            NPC("npc_darkworld", "bobibob", speed=0, nb_points=1, dialog=["J'ai fait une grande découverte !", "Une porte derrière une porte !", "Par contre il faisait vraiment sombre"])
        ])
        self.register_map("glitchworld", "neon", portals=[
            Portal(from_world="glitchworld", origin_point="enter_darkworld3", target_world="darkworld",
                   teleport_point="spawn_exit_glitchworld"),
            Portal(from_world="glitchworld", origin_point="enter_salle_disco", target_world="salle_disco",
                   teleport_point="spawn_salle_disco2")
        ], runes=[
            Rune("rune_glitchworld")
        ])
        self.register_map("forest_world", "haunted", portals=[
            Portal(from_world="forest_world", origin_point="enter_lost_wood1", target_world="forest_world",
                   teleport_point="spawn_lost_wood1"),
            Portal(from_world="forest_world", origin_point="enter_desert", target_world="evankhell",
                   teleport_point="spawn_desert"),
            Portal(from_world="forest_world", origin_point="enter_lost_wood2", target_world="forest_world",
                   teleport_point="spawn_lost_wood2"),
            Portal(from_world="forest_world", origin_point="enter_darkworld2", target_world="darkworld",
                   teleport_point="spawn_exit_forestworld")
        ], runes=[
            Rune("rune_forestworld")
        ], npcs=[
            NPC("npc_forest", "beb", speed=0, nb_points=1, dialog=["Bizarrement je n'ai pas froid", "comme si quelque chose me réchauffait", "je me sens mal"])
        ])
        self.register_map("evankhell", "white_desert", portals=[
            Portal(from_world="evankhell", origin_point="enter_forest", target_world="forest_world",
                   teleport_point="spawn_evankhell"),
            Portal(from_world="evankhell", origin_point="enter_ear", target_world="evankhell",
                   teleport_point="spawn_ear"),
            Portal(from_world="evankhell", origin_point="enter_ear2", target_world="evankhell",
                   teleport_point="spawn_ear2")
        ], runes=[
            Rune("rune_evankhell1"),
            Rune("rune_evankhell2")
        ])
        self.register_map("Teikodream", "pinksea", portals=[
            Portal(from_world="Teikodream", origin_point="enter_dreamworld", target_world="dreamworld",
                   teleport_point="spawn_dreamworld"),
            Portal(from_world="Teikodream", origin_point="enter_dungeon", target_world="dungeon",
                   teleport_point="exit_Teikodream"),
            Portal(from_world="Teikodream", origin_point="enter_laboratory2", target_world="Laboratoire_-_version_finito",
                   teleport_point="spawn_laboratory")
        ], runes=[
            Rune("rune_Teikodream")
        ], npcs=[
            NPC("npc_Teikodream", "bi", speed=0, nb_points=1, dialog=["Si tu me rapportes 15 runes des rêves", "je t'aiderai à descendre dans ce puit"])
        ])
        self.register_map("dreamworld", "test_world", portals=[
            Portal(from_world="dreamworld", origin_point="enter_darkworld", target_world="darkworld",
                   teleport_point="spawn_darkworld"),
            Portal(from_world="dreamworld", origin_point="dreamworld_exit", target_world="Teikodream",
                   teleport_point="dreamworld_spawn_exit")
        ], runes=[
            Rune("rune_dreamworld")
        ])
        self.register_map("end", "pinksea")

        self.teleport_player("player2")
        self.teleport_npcs()
        self.teleport_anges()
        self.teleport_runes()

    def check_npc_collisions(self, dialog_box):
        """ Vérifie les collisions avec les npcs et les runes, si contact : une boite de dialoque apparaît et la rune est téléportée en dehors de la map
            :return: None
            """
        for sprite in self.get_group().sprites():
            if sprite.rect.colliderect(self.player.rect_dialogue) and type(sprite) is NPC:
                dialog_box.execute(sprite.dialog)
            if sprite.rect.colliderect(self.player.rect_dialogue) and type(sprite) is Rune:
                dialog_box.execute(sprite.dialog)
                if dialog_box.reading == False:
                    self.liste_rune.append(sprite.name)
                    self.sound_manager.play1("rune")
                    self.teleport_rune(sprite, "rune")
                print(self.liste_rune)

    def check_collisions(self):
        """ Vérifie les collisions avec les portails, les murs, les npcs, les anges et les runes, si contact
            :return: None
            """

        #portails
        for portal in self.get_map().portals:
            if portal.from_world == self.current_map:
                point = self.get_object(portal.origin_point)
                rect = pygame.Rect(point.x, point.y, point.width, point.height)

                if self.player.feet.colliderect(rect):
                    copy_portal = portal
                    self.sound_manager.stop(self.get_map().sound)
                    self.current_map = portal.target_world
                    self.sound_manager.play(self.get_map().sound)
                    self.teleport_player(copy_portal.teleport_point)

        #collisions
        rect_npc = []
        for npc in self.get_map().npcs:
            rect_npc.append(npc.rect)
        rect_ange = []
        for ange in self.get_map().anges:
            rect_ange.append(ange.rect)
        rect_rune = []
        for rune in self.get_map().runes:
            rect_rune.append(rune.rect)

        for sprite in self.get_group().sprites():

            if type(sprite) is NPC:
                if sprite.rect.colliderect(self.player.rect):
                    print("ui")
                    sprite.speed_entity = 0
                else:
                    sprite.speed_entity = 1

            else:
                if sprite.rect.collidelist(rect_npc) > -1:
                    sprite.move_back()
                if sprite.rect.collidelist(rect_ange) > -1 and type(sprite) is not Ange:
                    self.wake_up()
                if sprite.rect.collidelist(rect_rune) > -1:
                    sprite.move_back()
            if sprite.feet.collidelist(self.get_walls()) > -1:
                sprite.move_back()

    def check_collision_bed(self):
        """ Vérifie si le joueur est en contact avec rect_bed, si oui, la fonction sleep() est utilisée
            :return: None
            """
        if self.current_map == "house-main":
            obj_bed = self.get_object("rect_bed")
            rect_bed = pygame.Rect(obj_bed.x, obj_bed.y, obj_bed.width, obj_bed.height)
            if self.player.feet.colliderect(rect_bed):
                self.sleep()

    def check_liste_rune(self):
        """ Vérifie le nombre de runes récupéré, si celui-ci est égale à 15 et que le joueur est en contact avec rect_porte, le joueur est téléporté à la map end
            :return: None
            """
        if self.current_map == "Teikodream":
            obj_porte = self.get_object("rect_porte")
            rect_porte = pygame.Rect(obj_porte.x, obj_porte.y, obj_porte.width, obj_porte.height)
            if len(self.liste_rune) == 15 and self.player.feet.colliderect(rect_porte):
                self.sound_manager.stop(self.get_map().sound)
                self.current_map = "end"
                self.teleport_player("player")

    def check_boot(self):
        """ Vérifie si le joueur est en contact avec les bottes et ajoute une option d'accélération si vérifiée
            :return: None
            """
        if self.current_map == "darkworld":
            obj_boot = self.get_object("boot")
            rect_boot = pygame.Rect(obj_boot.x, obj_boot.y, obj_boot.width, obj_boot.height)
            if self.player.feet.colliderect(rect_boot):
                self.player.object_speed = 1


    def check_end(self):
        """ Vérifie si le joueur est en contact avec le rect end
            :return: True
            """
        if self.current_map == "end":
            obj_end = self.get_object("end")
            rect_end = pygame.Rect(obj_end.x, obj_end.y, obj_end.width, obj_end.height)
            if self.player.feet.colliderect(rect_end):
                self.sound_manager.stop(self.get_map().sound)
                return True

    def teleport_player(self, name):
        """ Téléporte le joueur aux coordonnées d'un objet donné
            :return: None
            """

        point = self.get_object(name)
        self.sound_manager.play1("teleport")
        self.player.position[0] = point.x
        self.player.position[1] = point.y
        self.player.save_location()

    def teleport_rune(self, name_rune, name):
        """ Téléporte une rune donnée aux coordonnées d'un objet donné
            :return: None
            """
        point = self.get_object(name)
        name_rune.position[0] = point.x
        name_rune.position[1] = point.y
        name_rune.save_location()

    def register_map(self, name, sound, portals=[], npcs=[], anges=[], runes=[]):
        """ Registre toutes les caractéristiques d'une map donnée en prenant en argument le nom de la map, sa musique, ses portails, ses npcs, ses anges et ses runes
            :return: None
            """
        # charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame(f'../map/{name}.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # définir une liste qui va stocker les rectangles de collision
        walls = []

        for obj in tmx_data.objects:
            if obj.type == "collision":
                walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))

        # dessiner le groupe de calques
        group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=5)
        group.add(self.player)

        # récupérer tous les npcs pour les ajouter au groupe
        for npc in npcs:
            group.add(npc)

        for ange in anges:
            group.add(ange)

        for rune in runes:
            group.add(rune)

        #enregistrer la nouvelle map chargée
        self.maps[name] = Map(name, walls, group, tmx_data, portals, npcs, anges, runes, sound)

    # chercher des informations sur la map
    def get_map(self): return self.maps[self.current_map]
    def get_group(self): return self.get_map().group
    def get_walls(self): return self.get_map().walls
    def get_object(self, name): return self.get_map().tmx_data.get_object_by_name(name)

    def teleport_npcs(self):
        """ Téléporte les npcs à leur point de spawn qui correspond au premier point de leur chemin
            :return: None
            """
        for map in self.maps:
            map_data = self.maps[map]
            npcs = map_data.npcs

            for npc in npcs:
                npc.load_points(map_data.tmx_data)
                npc.teleport_spawn()

    def teleport_anges(self):
        """ Téléporte les anges à leur point de spawn qui correspond au premier point de leur chemin
            :return: None
            """
        for map in self.maps:
            map_data = self.maps[map]
            anges = map_data.anges

            for ange in anges:
                ange.load_points(map_data.tmx_data)
                ange.teleport_spawn()

    def teleport_runes(self):
        """ Téléporte les runes à leur poit de spawn qui correspond au premier point de leur chemin
            :return: None
            """
        for map in self.maps:
            map_data = self.maps[map]
            runes = map_data.runes

            for rune in runes:
                rune.load_points(map_data.tmx_data)
                rune.teleport_spawn()

    def wake_up(self):
        """ Téléporte le joueur à son lit
            :return: None
            """
        self.sound_manager.stop(self.get_map().sound)
        self.current_map = "house-main"
        self.sound_manager.play(self.get_map().sound)
        self.teleport_player("bed")

    def sleep(self):
        """ Téléporte le joueur dans le dreamworld (option de map aléatoire si besoin mais pas utilisée ici)
            :return: None
            """
        map_aleatoire = randint(0, len(self.liste_dreamap)-1)
        self.sound_manager.stop(self.get_map().sound)
        self.current_map = self.liste_dreamap[map_aleatoire]
        self.sound_manager.play1("dormir")
        self.sound_manager.play(self.get_map().sound)
        self.teleport_player("player")

    #dessiner et faire le centrage
    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)

    def update(self):
        self.get_group().update()
        self.check_collisions()

        for npc in self.get_map().npcs:
            npc.move()
        for ange in self.get_map().anges:
            ange.move()
        for rune in self.get_map().runes:
            rune.change_animation("left")

