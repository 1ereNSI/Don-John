import pygame

class SoundManager():

    def __init__(self):
        self.sounds = {
            'test_world': pygame.mixer.Sound("../sounds/unlitworld.ogg"),
            'dungeon': pygame.mixer.Sound("../sounds/snowworld.ogg")
        }

    def play(self, name):
        self.sounds[name].play()

    def stop(self, name):
        self.sounds[name].stop()