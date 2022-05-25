import pygame

from entity import Player, NPC, Rune
from src.dialog import DialogBox
from src.map import MapManager
from src.sounds import SoundManager


class Game:

    def __init__(self):
        # generer la fenètre du jeu
        self.screen = pygame.display.set_mode((1080, 720))
        pygame.display.set_caption("Liminal")



        #importer les backgrounds
        self.begin_screen = pygame.image.load("../images/begin_screen.jpg")
        self.begin_screen = pygame.transform.scale(self.begin_screen, (self.screen.get_size()))
        self.pausing_screen = pygame.image.load("../images/weird_field.png")
        self.pausing_screen = pygame.transform.scale(self.pausing_screen, (self.screen.get_size()))
        self.smile = pygame.image.load("../images/play_button.png")
        self.smile = pygame.transform.scale(self.smile, (30, 30))
        self.smile_rect = self.smile.get_rect()
        self.smile_rect.x = 535
        self.smile_rect.y = 415
        self.moon = pygame.image.load("../images/lune.png")
        self.ending_screen = pygame.image.load("../images/panowald2.png")
        self.ending_screen = pygame.transform.scale(self.ending_screen, (self.screen.get_size()))
        self.moon = pygame.transform.scale(self.moon, (550, 550))

        #generer joueur et instances
        self.player = Player()
        self.map_manager = MapManager(self.screen, self.player)
        self.dialog_box = DialogBox()
        self.sound_manager = SoundManager()

        # score
        self.score = 0

        #voir si le jeu a commencé
        self.is_playing = False

        #voir si le jeu est en pause
        self.is_pausing = False

        #voir si le joueur rêve
        self.is_dreaming = False

        #voir si le jeu est terminé
        self.is_ending = False


    def handle_input(self):
        """ Interprète les entrée clavier en action dans le jeu
            :return: None
            """
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation('up')
            if pressed[pygame.K_s]:
                self.player.move_up_speed()
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation('down')
            if pressed[pygame.K_s]:
                self.player.move_down_speed()
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation('right')
            if pressed[pygame.K_s]:
                self.player.move_right_speed()
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation('left')
            if pressed[pygame.K_s]:
                self.player.move_left_speed()

    def update(self):
        self.map_manager.update()

    def run(self):

        clock = pygame.time.Clock()
        self.sound_manager.play("dark_water")

        # boucle du jeu
        running = True

        while running:

            if self.is_playing:
                self.smile_rect.x = 1200
                self.smile_rect.y = 1200
                if self.is_pausing:
                    self.screen.blit(self.pausing_screen, (0, 0))
                    self.screen.blit(self.moon, (-35, -15))
                    pygame.display.flip()
                if self.is_ending:
                    self.sound_manager.play("circus")
                    self.screen.blit(self.ending_screen, (0, 0))
                    font1 = pygame.font.Font("../dialogs/Cinzel-Medium.ttf", 50)
                    ending_text = font1.render("END", 1, (255, 0, 255))
                    self.screen.blit(ending_text, (500, 400))
                    pygame.display.flip()
                else:
                    self.player.save_location()
                    self.handle_input()
                    self.update()
                    self.map_manager.draw()
                    self.dialog_box.render(self.screen)
                    self.score = len(self.map_manager.liste_rune)
                    if self.is_dreaming:
                        font = pygame.font.Font("../dialogs/Cinzel-Medium.ttf", 25)
                        score_text = font.render(f"RUNES : {self.score}", 1, (255, 0, 255))
                        self.screen.blit(score_text, (20, 20))
                    pygame.display.flip()
            else:
                self.screen.blit(self.begin_screen, (0, 0))
                self.screen.blit(self.smile, self.smile_rect)
                pygame.display.flip()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.map_manager.check_npc_collisions(self.dialog_box)
                    if self.is_pausing == False and event.key == pygame.K_ESCAPE:
                        self.is_pausing = True
                        self.sound_manager.play1("lance_pause")
                    if self.is_pausing == True and event.key == pygame.K_1:
                        self.is_pausing = False
                        self.sound_manager.play1("pause_ferme")
                    if event.key == pygame.K_0 and self.is_dreaming == True:
                        self.map_manager.wake_up()
                        self.is_dreaming = False
                    if self.map_manager.current_map == "house-main":
                        self.is_dreaming = False
                    if event.key == pygame.K_2 and self.is_dreaming == False:
                        self.is_dreaming = True
                        self.map_manager.check_collision_bed()
                    if event.key == pygame.K_SPACE and self.is_dreaming == True:
                        self.map_manager.check_boot()
                        self.map_manager.check_liste_rune()
                        if self.map_manager.check_end():
                            self.is_ending = True

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.smile_rect.collidepoint(event.pos):
                        self.is_playing = True
                        self.sound_manager.stop("dark_water")
                        self.map_manager.teleport_player("player1")

            clock.tick(60)

        pygame.quit()
