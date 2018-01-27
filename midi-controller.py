import pygame
import sys

pygame.init()
pygame.display.set_mode((200,100))
pygame.mixer.music.load("major-scale.mid")
pygame.mixer.music.set_volume(1.0)
pygame.mixer.music.play(-1)
