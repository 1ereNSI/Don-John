import pygame

class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name, speed, len_images=3, len_image=32):
        super().__init__()
        self.sprite_sheet = pygame.image.load(f'../sprites/{sprite_name}.png')
        self.animation_index = 0
        self.clock = 0
        self.len_images = len_images
        self.len_image = len_image
        self.images = {
            'down': self.get_images(0),
            'left': self.get_images(32),
            'right': self.get_images(64),
            'up': self.get_images(96)
        }

        self.speed_change = speed

    def change_animation(self, name):
        """ Change le sprite d'une entité donnée en parcourant sa spritesheet
            :return: None
            """
        self.image = self.images[name][self.animation_index]
        self.image.set_colorkey(self.image.get_at((0, 0)))
        self.clock += self.speed_change * 5

        if self.clock >= 100:

            self.animation_index += 1 #passe à l'image suivante

            if self.animation_index >= len(self.images[name]):
                self.animation_index = 0

            self.clock = 0

    def get_images(self, y):
        """ Récupère chaque image à une ordonnée donnée et les ajoute à une liste images
            :return: images
            """
        images = []

        for i in range(0, self.len_images):
            x = i * self.len_image
            image = self.get_image(x, y)
            images.append(image)

        return images

    def get_image(self, x, y):
        """ Récupère une image de surface 32x32 aux coordonnées données
            :return: image
            """
        image = pygame.Surface([self.len_image, self.len_image])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 32, 32))
        return image