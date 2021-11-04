import pygame 
from sys import exit
import time

pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption('Nytt på Nytt Mini Game Show')
clock = pygame.time.Clock()
#text_font = pygame.font.Font(None, 50) # None sier hvilken font, fint ttf fil!
#text_font_avsnitt = pygame.font.Font(None, 10)
#text_surface = text_font.render('Nytt på Nytt Mini Game Show!', False, 'Orange')


def startside():
# Definerer her fonten til de ulike tekt boksene:
    text_font = pygame.font.Font(None, 70) # None sier hvilken font, fint ttf fil!
    text_font_overskirft = pygame.font.Font(None, 50)
    text_font_avsnitt = pygame.font.Font(None, 40)
    text_font_knapp = pygame.font.Font(None, 60)


#  Definerer her innhold i tekstboksene:
    text_overskrift = text_font.render('Nytt på Nytt Mini Game Show!', False, 'Orange')
    text_surface_overskrift = text_font_overskirft.render('Instruks:', False, 'Black')
    text_surface_avsnitt1 = text_font_avsnitt.render('Hver av de tre spillerene inntar hver sin plass rundt bordet med sin konsoll', False, 'Black')
    text_surface_avsnitt2 = text_font_avsnitt.render('En vil ta programlederplassen, og 2 vil fungere som gjester under showet!', False, 'Black')
    text_surface_avsnitt3 = text_font_avsnitt.render('Spørsmålene vil være basert på ukens ord, akkurat som på Nytt på Nytt. Her ', False, 'Black')
    text_surface_avsnitt4 = text_font_avsnitt.render('skal hver av gjestene sette sammen sitt ord, ved alerternativene på skjermen.', False, 'Black')
    text_surface_avsnitt5 = text_font_avsnitt.render('Ordet må så begrunnes av gjesten til de andre to. Samme vil skje for gjest 2.', False, 'Black')
    text_surface_avsnitt6 = text_font_avsnitt.render('Når begge har avlagt og begrunnet sitt svar. Er det opptil programleder om å ', False, 'Black')
    text_surface_avsnitt7 = text_font_avsnitt.render('velge hvilket som var best! Dette vil så skje over 3 runder, og vinner vil tilslutt', False, 'Black')
    text_surface_avsnitt8 = text_font_avsnitt.render('bli kåret! ', False, 'Black')
    text_surface_avsnitt9 = text_font_avsnitt.render('Når alle er klare! Trykk på start knappen på programleder konsollen!', False, 'Black')
    

    knapp_surface = pygame.Surface((250,100))
    knapp_surface_tekst = text_font_knapp.render('Start!', None, 'White')
    

# Rendrer her innholdet i tekstboksene basert på font og innhold:
    screen.fill('White')
    knapp_surface.fill('Red')
    screen.blit(text_overskrift,(400,100))
    screen.blit(text_surface_overskrift,(200, 250))
    screen.blit(text_surface_avsnitt1, (200, 300))
    screen.blit(text_surface_avsnitt2, (200, 330))
    screen.blit(text_surface_avsnitt3, (200, 360))
    screen.blit(text_surface_avsnitt4, (200, 390))
    screen.blit(text_surface_avsnitt5, (200, 420))
    screen.blit(text_surface_avsnitt6, (200, 450))
    screen.blit(text_surface_avsnitt7, (200, 480))
    screen.blit(text_surface_avsnitt8, (200, 510))
    screen.blit(text_surface_avsnitt9, (200, 600))
    
    ## Knappen:
    screen.blit(knapp_surface,(200,700))
    screen.blit(knapp_surface_tekst, (270,730))

    #pygame.display.update()

def runde():
    screen.fill('Orange')
    pygame.display.update()

def resultater(spill_vinner):
# Definerer fonten til teksten her:
    screen.fill('Orange')
    text_font = pygame.font.Font(None, 90)
    text_font_overskirft = pygame.font.Font(None, 200)
    
# Definerer innhold som skal rendres:
    text_overskrift = text_font.render('Vinneren av Nytt på Nytt Mini game Show er: ', False, 'White')
    text_vinner = text_font_overskirft.render(spill_vinner, False, 'Yellow')

#Rendrer ut på skjermen:
    screen.blit(text_overskrift,(400,200))
    pygame.display.update()

    #time.sleep(5)

    screen.blit(text_vinner,(750,750))

    #pygame.display.update()


    



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            exit() 
        startside()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                resultater('Spiller 1!')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                resultater('Spiller 1 ye')
        pygame.display.update()
    clock.tick(60)