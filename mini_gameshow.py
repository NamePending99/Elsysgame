import pygame 
from sys import exit

pygame.init()
screen = pygame.display.set_mode((900,600))
pygame.display.set_caption('Nytt på Nytt Mini Game Show')
clock = pygame.time.Clock()
text_font = pygame.font.Font(None, 50) # None sier hvilken font, fint ttf fil!

text_surface = text_font.render('Nytt på Nytt Mini Game Show!', False, 'Orange')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 
    screen.fill('White')
    screen.blit(text_surface,(200,100))
    pygame.display.update()
    
    
    
    clock.tick(60)