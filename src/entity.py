import pygame

from src.animation import AnimateSprite

class Entity(AnimateSprite):

    def __init__(self, name, sprite_name, x, y, speed, len_images=3, len_image=32):
        super().__init__(sprite_name, speed, len_images, len_image)
        self.image = self.get_image(0, 0)
        self.image.set_colorkey(self.image.get_at((0, 0)))
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.rect_dialogue = pygame.Rect(0, 0, self.rect.width+10, self.rect.height+10)
        self.old_position = self.position.copy()
        self.speed_entity = speed
        self.object_speed = 0

    #enregistre les coordonées actuelles du joueur
    def save_location(self): self.old_position = self.position.copy()

    # mouvements des entités et accélérations
    def move_right(self):
        self.change_animation("right")
        self.position[0] += self.speed_entity

    def move_right_speed(self):
        self.change_animation("right")
        self.position[0] += (self.speed_entity + self.object_speed)

    def move_left(self):
        self.change_animation("left")
        self.position[0] -= self.speed_entity

    def move_left_speed(self):
        self.change_animation("left")
        self.position[0] -= (self.speed_entity + self.object_speed)

    def move_up(self):
        self.change_animation("up")
        self.position[1] -= self.speed_entity

    def move_up_speed(self):
        self.change_animation("up")
        self.position[1] -= (self.speed_entity + self.object_speed)

    def move_down(self):
        self.change_animation("down")
        self.position[1] += self.speed_entity

    def move_down_speed(self):
        self.change_animation("down")
        self.position[1] += (self.speed_entity + self.object_speed)

    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom
        self.rect_dialogue.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom
        self.rect_dialogue.midbottom = self.rect.midbottom
    
class Player(Entity):
    
    def __init__(self):
        super().__init__("player", "player2", 0, 0, 2)

class NPC(Entity):

    def __init__(self, name, sprite_name, speed=0, nb_points=1, dialog=[], len_images=3, len_image=32):
        super().__init__(name, sprite_name, 0, 0, speed, len_images, len_image)
        self.nb_points = nb_points
        self.points = []
        self.dialog = dialog
        self.name = name
        self.current_point = 0

    def move(self):
        """ Permet aux npcs, aux runes et aux anges de se déplacer selon un chemin définit
            :return: None
            """
        current_point = self.current_point
        target_point = self.current_point + self.speed_entity
        
        if target_point >= self.nb_points:
            target_point = 0

        current_rect = self.points[current_point]
        target_rect = self.points[target_point]

        if current_rect.y < target_rect.y and abs(current_rect.x - target_rect.x) < 3:
            self.move_down()
        elif current_rect.y > target_rect.y and abs(current_rect.x - target_rect.x) < 3:
            self.move_up()
        elif current_rect.x > target_rect.x and abs(current_rect.y - target_rect.y) < 3:
            self.move_left()
        elif current_rect.x < target_rect.x and abs(current_rect.y - target_rect.y) < 3:
            self.move_right()

        if self.rect.colliderect(target_rect):
            self.current_point = target_point

    def teleport_spawn(self):
        location = self.points[self.current_point]
        self.position[0] = location.x
        self.position[1] = location.y
        self.save_location()

    def load_points(self, tmx_data):
        """ Cherche le chemin de l'entité sur la map et ajoute le rect de chaque point de passage à une liste
            :return: None
            """
        for num in range(1, self.nb_points+1):
            point = tmx_data.get_object_by_name(f"{self.name}_path{num}")
            rect = pygame.Rect(point.x, point.y, point.width, point.height)
            self.points.append(rect)

class Ange(NPC):
    def __init__(self, name, sprite_name, speed, nb_points):
        super().__init__(name, sprite_name, speed, nb_points)

class Rune(NPC):
    def __init__(self, name):
        self.name = name
        self.dialogue = [f"bravo tu as obtenu la {self.name}"]
        super().__init__(name, "objet", 1, 1, dialog=self.dialogue, len_images=4, len_image=16)


