import pygame

class SoundManager():

    def __init__(self):
        #dictionnaire des sons du jeu
        self.sounds = {
            'test_world': pygame.mixer.Sound("../sounds/unlitworld.ogg"),
            'snowworld': pygame.mixer.Sound("../sounds/snowworld.ogg"),
            'dungeon': pygame.mixer.Sound("../sounds/dungeon.ogg"),
            'pinksea': pygame.mixer.Sound("../sounds/pinksea.ogg"),
            'eyeball': pygame.mixer.Sound("../sounds/eyeball.ogg"),
            'ADT': pygame.mixer.Sound("../sounds/ADT.ogg"),
            'room': pygame.mixer.Sound("../sounds/room.ogg"),
            'room2': pygame.mixer.Sound("../sounds/room2.ogg"),
            'white_desert': pygame.mixer.Sound("../sounds/white_desert.ogg"),
            'number_world': pygame.mixer.Sound("../sounds/number_world.ogg"),
            'haunted': pygame.mixer.Sound("../sounds/haunted.ogg"),
            'circus': pygame.mixer.Sound("../sounds/circus.ogg"),
            'dark_water': pygame.mixer.Sound("../sounds/dark_water.ogg"),
            'hell': pygame.mixer.Sound("../sounds/hell.ogg"),
            'neon': pygame.mixer.Sound("../sounds/neon.ogg"),
            'YSBD': pygame.mixer.Sound("../sounds/YSBD.ogg"),
            'rune': pygame.mixer.Sound("../sounds/rune.mp3"),
            'dormir': pygame.mixer.Sound("../sounds/dormir.mp3"),
            'teleport': pygame.mixer.Sound("../sounds/teleport.mp3"),
            'lance_pause': pygame.mixer.Sound("../sounds/lance_pause.mp3"),
            'pause_ferme': pygame.mixer.Sound("../sounds/pause_ferme.mp3"),
        }

    #jouer un son infiniment
    def play(self, name):
        self.sounds[name].play(loops=-1, fade_ms=0)

    #jouer un son une fois
    def play1(self, name):
        self.sounds[name].play()

    #stopper un son
    def stop(self, name):
        self.sounds[name].stop()