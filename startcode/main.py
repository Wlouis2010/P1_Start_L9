import pygame, sys
from pygame.locals import QUIT

a = 500
b = 500
pygame.init()
venster = pygame.display.set_mode((a, b))

pygame.display.set_caption("game")
venster.fill((255,255,255))
huidigekleur = (0,0,0)
achtergrond = (255,255,255)
radius = 5
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if pygame.mouse.get_pressed() == (True, False, False):
            pygame.draw.circle(venster, (huidigekleur), pygame.mouse.get_pos(),radius)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                huidigekleur = (255,0,0) #rood
            if event.key == pygame.K_2:
                huidigekleur = (255,100,10) #oranje
            if event.key == pygame.K_3:
                huidigekleur = (255,255,0) #geel
            if event.key == pygame.K_4:
                huidigekleur = (0, 255, 0) #groen
            if event.key == pygame.K_5:
                huidigekleur = (0, 0, 255) # blauw
            if event.key == pygame.K_6:
                huidigekleur = (165,42,255) # paars
            if event.key == pygame.K_7:
                huidigekleur = (165,42,42) # bruin
            if event.key == pygame.K_8:
                huidigekleur = (0, 0, 0) # zwart
            if event.key == pygame.K_9:
                huidigekleur = (255, 255, 255) # wit
            if event.key == pygame.K_b:
                venster.fill((0, 0, 0))
                achtergrond = ((0,0,0,))
                huidigekleur = (255, 255, 255)  # wit

            if event.key == pygame.K_w:
                venster.fill((255,255,255))
                achtergrond = ((255,255,255))
                huidigekleur = (0, 0, 0)  # zwart
            if event.key == pygame.K_s:
                pygame.image.save(venster,"tekening"+".jpg")
            if event.type == pygame.MOUSEWHEEL:
                if 
                   adius += 1
                   if radius < 255:
                       radius = 1



        if pygame.mouse.get_pressed() == (False, False, True):
            pygame.draw.circle(venster, (achtergrond), pygame.mouse.get_pos(), radius)
    pygame.display.update()

