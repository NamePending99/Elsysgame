# Active libraries

import pygame
import time
from sys import exit
from pygame import surface
from pygame.display import update
from pygame import image
from gpiozero import Button


# GPIO PINS MÅ SETTES TIL RIKTIG KNAPP (1/6)
p1Next = Button(16)
p1Select = Button(18)

p2Next = Button(22)
p2Select = Button(24)

hostStart = Button(8)
host_p1 = Button(10)
host_p2 = Button(12)


# initialize libaries
pygame.init()

# global variables
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 300))  # SJEKK SKJERM STØRRELSE (2/6)
ord_dict = {1: ['kanon', 'kristen', 'slanke', 'gresskar', 'porno'], 2: ['kultur', 'øl', 'alder', 'pave', 'grilldress'], 3: ['liste', 'bolle', 'nav', 'jåle', 'snø'],
            4: ['trønder', 'ærlighet', 'banne', 'influensa', 'bok'], 5: ['politiker', 'kjærlighet', 'skip', 'kannibal', 'vin'], 6: ['høyre', 'halal', 'fotballspiller', 'vaksine', 'bolig'],
            7: ['myte', 'taliban', 'svenske', 'smitte', 'squash'], 8: ['bonde', 'elsparkesykkel', 'regjering', 'spøkelse', 'restaurant'], 9: ['olje', 'lefse', 'forfatter', 'trone', 'sv'],
            10: ['skatt', 'pave', 'småbruk', 'coach', 'vaksine'], 11: ['munch', 'kokain', 'fotball', 'strøm', 'flodhest']}
seksjoner = pygame.image.load(
    "/Users/Bruker/OneDrive/Documents/VS Code/ElsysCode/sections.png")  # SETT INN RIKTIG DIR (3/6)
sel_arrow = pygame.image.load(
    "/Users/Bruker/OneDrive/Documents/VS Code/ElsysCode/down-arrow.png")  # SETT INN RIKTIG DIR (4/6)


def main():

    running = True
    runde_teller = 0
    startside()

    ps1 = 0
    ps2 = 0
    reset = 0

    globalscore_p1 = 0
    globalscore_p2 = 0
    counter = 0

    while running:
        pygame.display.set_caption("N&N Minigame")
        for event in pygame.event.get():
            time.sleep(0.2)
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

            if hostStart.when_pressed == True:
                spiller1_ord = player_selection()
                spiller2_ord = player_selection()
                score(spiller1_ord, spiller2_ord)

            if host_p1 == True:
                print("Spiller 1 får poeng")
                ps1 += 1

            if host_p2 == True:
                ps2 += 1
                print("Spiller 2 får poeng")

            if (ps1 != 0) or (ps2 != 0):
                if ps1 > ps2:
                    globalscore_p1 += 1
                    ps1 = ps2 = 0
                    counter += 1

                    spiller1_ord = player_selection()
                    spiller2_ord = player_selection()
                    score(spiller1_ord, spiller2_ord)
                else:
                    globalscore_p2 += 1
                    ps1 = ps2 = 0
                    counter += 1

                    spiller1_ord = player_selection()
                    spiller2_ord = player_selection()
                    score(spiller1_ord, spiller2_ord)

            if counter >= 2:
                loop = False

                if globalscore_p1 > globalscore_p2:
                    loop = resultater("Spiller 1")
                    globalscore_p1 = 0
                    globalscore_p2 = 0
                    counter = 0
                    if loop == True:
                        startside()
                else:
                    loop = resultater("Spiller 2")
                    globalscore_p1 = 0
                    globalscore_p2 = 0
                    counter = 0
                    if loop == True:
                        startside()

            pygame.display.update()
            clock.tick(60)


def startside():
    # Definerer her fonten til de ulike tekt boksene:
    # None sier hvilken font, fint ttf fil!
    text_font = pygame.font.Font(None, 70)
    text_font_overskirft = pygame.font.Font(None, 50)
    text_font_avsnitt = pygame.font.Font(None, 40)
    text_font_knapp = pygame.font.Font(None, 60)


#  Definerer her innhold i tekstboksene:
    text_overskrift = text_font.render(
        'Nytt på Nytt Mini Game Show!', False, 'Orange')
    text_surface_overskrift = text_font_overskirft.render(
        'Instruks:', False, 'Black')
    text_surface_avsnitt1 = text_font_avsnitt.render(
        'Hver av de tre spillerene inntar hver sin plass rundt bordet med sin konsoll', False, 'Black')
    text_surface_avsnitt2 = text_font_avsnitt.render(
        'En vil ta programlederplassen, og 2 vil fungere som gjester under showet!', False, 'Black')
    text_surface_avsnitt3 = text_font_avsnitt.render(
        'Spørsmålene vil være basert på ukens ord, akkurat som på Nytt på Nytt. Her ', False, 'Black')
    text_surface_avsnitt4 = text_font_avsnitt.render(
        'skal hver av gjestene sette sammen sitt ord, ved alerternativene på skjermen.', False, 'Black')
    text_surface_avsnitt5 = text_font_avsnitt.render(
        'Ordet må så begrunnes av gjesten til de andre to. Samme vil skje for gjest 2.', False, 'Black')
    text_surface_avsnitt6 = text_font_avsnitt.render(
        'Når begge har avlagt og begrunnet sitt svar. Er det opptil programleder om å ', False, 'Black')
    text_surface_avsnitt7 = text_font_avsnitt.render(
        'velge hvilket som var best! Dette vil så skje over 3 runder, og vinner vil tilslutt', False, 'Black')
    text_surface_avsnitt8 = text_font_avsnitt.render(
        'bli kåret! ', False, 'Black')
    text_surface_avsnitt9 = text_font_avsnitt.render(
        'Når alle er klare! Trykk på start knappen på programleder konsollen!', False, 'Black')

    knapp_surface = pygame.Surface((250, 100))
    knapp_surface_tekst = text_font_knapp.render('Start!', None, 'White')


# Rendrer her innholdet i tekstboksene basert på font og innhold:
    screen.fill('White')
    knapp_surface.fill('Red')
    screen.blit(text_overskrift, (400, 100))
    screen.blit(text_surface_overskrift, (200, 250))
    screen.blit(text_surface_avsnitt1, (200, 300))
    screen.blit(text_surface_avsnitt2, (200, 330))
    screen.blit(text_surface_avsnitt3, (200, 360))
    screen.blit(text_surface_avsnitt4, (200, 390))
    screen.blit(text_surface_avsnitt5, (200, 420))
    screen.blit(text_surface_avsnitt6, (200, 450))
    screen.blit(text_surface_avsnitt7, (200, 480))
    screen.blit(text_surface_avsnitt8, (200, 510))
    screen.blit(text_surface_avsnitt9, (200, 600))

    # Knappen:
    screen.blit(knapp_surface, (200, 700))
    screen.blit(knapp_surface_tekst, (270, 730))


def resultater(spill_vinner="PLACEHOLDER"):
    # Definerer fonten til teksten her:
    screen.fill('Orange')
    text_font = pygame.font.Font(None, 90)
    text_font_overskirft = pygame.font.Font(None, 200)

# Definerer innhold som skal rendres:
    text_overskrift = text_font.render(
        'Vinneren av Nytt på Nytt Mini game Show er: ', False, 'White')
    text_vinner = text_font_overskirft.render(spill_vinner, False, 'Yellow')

# Rendrer ut på skjermen:
    screen.blit(text_overskrift, (400, 200))
    screen.blit(text_vinner, (100, 100))

    pygame.display.update()
    time.sleep(5)

    return True


def player_selection():

    # Her har jeg laget hjelpefunksjoner og andre ting som trengs:

    # Bilde for starten
    screen.fill('Orange')
    seksjoner = pygame.image.load("sections.png")  # SET RIKTIG DIR (5/6)

    # Startposisjon til pilen:
    sel_arrow = pygame.image.load("down-arrow.png")  # SETT RIKTIG DIR (6/6)
    sel_arrow_X = 255
    sel_arrow_Y = 155

    # Hjelpefunsjoner:
    def arrow_pos(x, y):
        screen.blit(sel_arrow, (x, y))

    def text_to_screen(text, x_pos, y_pos):
        temp_font = pygame.font.SysFont(None, 24)
        img = temp_font.render('{}'.format(text), True, 'Blue')
        screen.blit(img, (x_pos, y_pos))

    word_comb = ""
    n = 0
    while n < 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # if keystroke is change arrow position, and selection logic

            if p1Next.when_pressed == True or p2Next.when_pressed == True:  # movement of arrow logic
                if (sel_arrow_X == 255) and (sel_arrow_Y == 155):
                    sel_arrow_X = 530
                elif sel_arrow_X == 530 and sel_arrow_Y == 155:
                    sel_arrow_Y = 350
                    sel_arrow_X = 255
                elif sel_arrow_X == 255 and sel_arrow_Y == 350:
                    sel_arrow_X = 530
                else:
                    sel_arrow_X = 255
                    sel_arrow_Y = 155
            # selection logic, every "if" is for the first word, the elifs are for second words
            if p1Select.when_pressed == True or p2Select == True:
                if (sel_arrow_X == 255) and (sel_arrow_Y == 155) and (len(word_comb) == 0):
                    word_comb = ord_dict[1][0]
                    n += 1
                elif (sel_arrow_X == 255) and (sel_arrow_Y == 155) and (len(word_comb) > 1):
                    word_comb += ord_dict[1][0]
                    n += 1
                if (sel_arrow_X == 530) and (sel_arrow_Y == 155) and (len(word_comb) == 0):
                    word_comb = ord_dict[1][1]
                    n += 1
                elif (sel_arrow_X == 530) and (sel_arrow_Y == 155) and (len(word_comb) > 0):
                    word_comb += ord_dict[1][1]
                    n += 1
                if (sel_arrow_X == 255) and (sel_arrow_Y == 350) and (len(word_comb) == 0):
                    word_comb = ord_dict[1][2]
                    n += 1
                elif (sel_arrow_X == 255) and (sel_arrow_Y == 350) and (len(word_comb) > 0):
                    word_comb += ord_dict[1][2]
                    n += 1
                if (sel_arrow_X == 530) and (sel_arrow_Y == 350) and (len(word_comb) == 0):
                    word_comb = ord_dict[1][3]
                    n += 1
                elif (sel_arrow_X == 530) and (sel_arrow_Y == 350) and (len(word_comb) > 0):
                    word_comb += ord_dict[1][3]
                    n += 1

        screen.fill('Orange')
        screen.blit(seksjoner, (100, 25))
        text_to_screen(word_comb, 190, 50)
        text_to_screen(ord_dict[1][0], 190, 240)
        text_to_screen(ord_dict[1][1], 450, 240)
        text_to_screen(ord_dict[1][2], 190, 480)
        text_to_screen(ord_dict[1][3], 450, 480)
        arrow_pos(sel_arrow_X, sel_arrow_Y)
        pygame.display.update()
    time.sleep(1)
    return word_comb


def score(answer_p1, answer_p2):

    # STYLE
    pygame.display.set_caption("N&N Minigame")

    orange = [255, 165, 0]
    white = [255, 255, 255]
    screen.fill(orange)

    # ELEMENTS
    text_font = pygame.font.Font(None, 50)  # Delete after merge if duplicate
    page_header = text_font.render(
        'Spillvert, gi poeng til spiller med best svar', False, white)
    text_p1 = text_font.render('Spiller 1', False, white)
    text_p2 = text_font.render('Spiller 2', False, white)
    text_answer_p1 = text_font.render(answer_p1, False, white)
    text_answer_p2 = text_font.render(answer_p2, False, white)

    # Draw text elements
    screen.blit(page_header, (1278//4, 50))  # Draw page_header
    screen.blit(text_p1, (1278//6, 300))  # Draw text_p1
    screen.blit(text_p2, ((1278//6*4), 300))  # Draw text_p2
    screen.blit(text_answer_p1, (1278//6, 500))  # Answer_p1
    screen.blit(text_answer_p2, (1278//6*4, 500))  # Answer_p2

    # Center Line
    startX = 1278//2
    startY = 110
    endX = 1278//2
    endY = 750
    width = 20
    pygame.draw.line(screen, white, (startX, startY), (endX, endY), width)

    # Cross Line
    startX2 = 0
    startY2 = 110
    endX2 = 1278
    endY2 = startY2
    pygame.draw.line(screen, white,
                     (startX2, startY2), (endX2, endY2), width)

    pygame.display.update()


if __name__ == "__main__":
    # call the main function
    main()
