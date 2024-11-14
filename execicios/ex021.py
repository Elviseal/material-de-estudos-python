import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

'''app roda mp3, tive muita dificudade porque essa nova versão precisa
 input() para ler o arquivo mp3'''
