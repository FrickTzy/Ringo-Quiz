import pygame
import requests
from time import sleep

test_url = 'https://archive.org/download/PinkFloyd07CarefullWithThatAxeEugene/02%20-%20Learning%20To%20Fly.wav'


class myfile(object):
    def __init__(self,url):
        self.file = requests.get(url, stream=True)

    def read(self,*args):
        if args:
            return self.file.raw.read(args[0])
        else:
            return self.file.raw.read()


if __name__ == "__main__":
    pygame.mixer.init()
    fi = myfile(test_url)
    pygame.mixer.music.load(fi)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        sleep(1)