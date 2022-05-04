import pygame

from entity import Player, NPC
from src.dialog import DialogBox
from src.map import MapManager


class Game:

    def __init__(self):
        # generer la fenètre du jeu
        self.screen = pygame.display.set_mode((1080, 720))
        pygame.display.set_caption("Don John")

        #importer les backgrounds
        self.begin_screen = pygame.image.load("../images/weird_field.png")
        self.begin_screen = pygame.transform.scale(self.begin_screen,(self.screen.get_size()))

        #generer joueur et instances
        self.player = Player()
        self.map_manager = MapManager(self.screen, self.player)
        self.dialog_box = DialogBox()

        #voir si le jeu a commencé
        self.is_playing = False


    def handle_input(self):

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation('up')
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation('down')
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation('right')
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation('left')

    def update(self):
        self.map_manager.update()

    def run(self):

        clock = pygame.time.Clock()

        # boucle du jeu
        running = True

        while running:

            if self.is_playing:
                self.player.save_location()
                self.handle_input()
                self.update()
                self.map_manager.draw()
                self.dialog_box.render(self.screen)
                pygame.display.flip()
            else:
                self.screen.blit(self.begin_screen, (0, 0))
                pygame.display.flip()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.map_manager.check_npc_collisions(self.dialog_box)
                    if self.is_playing == False and event.key == pygame.K_a:
                        self.is_playing = True
                        self.map_manager.teleport_player("player1")


            clock.tick(60)

        pygame.quit()
