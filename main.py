import pygame
pygame.init()

# creer une première classe qui va representer notre joueur
class Player(pygame.sprite.Sprite) :

    def __init__(self):
        super().__init__()
        self.health = 20
        self.max_health = 20
        self.attack = 2
        self.velocity = 5
        self.image = pygame.image.load('assets/Bas_1.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 100

# charger notre joueur
player = Player()

# generer la fenetre de notre jeu
pygame.display.set_caption("Don John")
screen = pygame.display.set_mode((1080, 720))

running = True

# boucle tant que cette condition est vrai
while running:

    # appliquer l'image de mon joueur
    screen.blit(player.image, player.rect)

    # mettre à jour l'écran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # que l'évènement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")

    #screen.fill(black)
    pygame.display.flip()