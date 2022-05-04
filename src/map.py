from dataclasses import dataclass
import pygame, pytmx, pyscroll

from src.entity import NPC, Player, Ange
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
    sound: str

class MapManager:

    def __init__(self, screen, player):
        self.screen = screen
        self.player = player
        self.maps = dict()  # 'house' -> Map("house", walls, group)
        self.current_map = "Teiko"
        self.sound_manager = SoundManager()

        self.register_map("world", "test_world", portals=[
            Portal(from_world="world", origin_point="enter_house", target_world="house", teleport_point="spawn_house"),
            Portal(from_world="world", origin_point="enter_house2", target_world="house2", teleport_point="spawn_house"),
            Portal(from_world="world", origin_point="enter_dungeon", target_world="dungeon", teleport_point="spawn_dungeon")
        ], npcs=[
            NPC("paul", "paul", nb_points=4, dialog=["Salut copain", "j'ai une formidable quête pour toi", "veux-tu l'entendre ?"])
        ])
        self.register_map("house", "test_world", portals=[
            Portal(from_world="house", origin_point="exit_house", target_world="world", teleport_point="enter_house_exit")
        ])
        self.register_map("house2", "dungeon", portals=[
            Portal(from_world="house2", origin_point="exit_house", target_world="world", teleport_point="enter_house2_exit")
        ])
        self.register_map("dungeon", "test_world", portals=[
            Portal(from_world="dungeon", origin_point="exit_dungeon", target_world="world", teleport_point="enter_dungeon_exit")
        ])
        self.register_map("Teiko", "dungeon", portals=[
            Portal(from_world="Teiko", origin_point="teleport_Teiko", target_world="Teiko", teleport_point="player")
        ], npcs=[], anges=[
            Ange("ange1", "boss", nb_points=1),
            Ange("ange2", "ange", nb_points=1)
        ])
        self.register_map("house-1", "test_world")

        self.teleport_player("player2")
        self.teleport_npcs()
        self.teleport_anges()
        #self.sound_manager.play(self.get_map().sound)

    def check_npc_collisions(self, dialog_box):
        for sprite in self.get_group().sprites():
            if sprite.rect.colliderect(self.player.rect) and type(sprite) is NPC:
                dialog_box.execute(sprite.dialog)

    def check_collisions(self):

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
            rect_npc.append(ange.rect)

        for sprite in self.get_group().sprites():

            if type(sprite) is NPC:
                if sprite.rect.colliderect(self.player.rect):
                    sprite.speed = 0
                else:
                    sprite.speed = 1
            else:

                if sprite.feet.collidelist(rect_npc) > -1:
                    sprite.move_back()
                else:
                    sprite.speed = 2

                if sprite.feet.collidelist(rect_ange) > -1:
                    sprite.move_back()

            if sprite.feet.collidelist(self.get_walls()) > -1:
                sprite.move_back()

    def teleport_player(self, name):

        point = self.get_object(name)
        self.player.position[0] = point.x
        self.player.position[1] = point.y
        self.player.save_location()

    def register_map(self, name, sound, portals=[], npcs=[], anges=[]):

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

        #enregistrer la nouvelle map chargée
        self.maps[name] = Map(name, walls, group, tmx_data, portals, npcs, anges, sound)

    def get_map(self): return self.maps[self.current_map]

    def get_group(self): return self.get_map().group

    def get_walls(self): return self.get_map().walls

    def get_object(self, name): return self.get_map().tmx_data.get_object_by_name(name)

    def teleport_npcs(self):
        for map in self.maps:
            map_data = self.maps[map]
            npcs = map_data.npcs

            for npc in npcs:
                npc.load_points(map_data.tmx_data)
                npc.teleport_spawn()

    def teleport_anges(self):
        for map in self.maps:
            map_data = self.maps[map]
            anges = map_data.anges

            for ange in anges:
                ange.load_points(map_data.tmx_data)
                ange.teleport_spawn()

    #dessiner et faire le centrage
    def draw(self):
        self.get_group().draw(self.screen)
        self.get_group().center(self.player.rect.center)

    def update(self):
        self.get_group().update()
        self.check_collisions()

        for npc in self.get_map().npcs:
            npc.move()