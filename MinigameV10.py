# Active libraries

import pygame
import time
import RPi.GPIO as GPIO
import random
from sys import exit
from pygame import surface
from pygame.display import update
from pygame import image
from signal import signal, SIGINT


# initialize libaries
pygame.init()
GPIO.setmode(GPIO.BCM)


def quitBoi():
    print("Babai")
    pygame.QUIT()
    exit()


# global variables
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
ord_dict = {1: ['kanon', 'kristen', 'slanke', 'gresskar', 'porno'], 2: ['kultur', 'øl', 'alder', 'pave', 'grilldress'],
            3: ['liste', 'bolle', 'nav', 'jåle', 'snø'], 4: ['trønder', 'ærlighet', 'banne', 'influensa', 'bok'],
            5: ['politiker', 'kjærlighet', 'skip', 'kannibal', 'vin'], 6: ['høyre', 'halal', 'fotballspiller', 'vaksine', 'bolig'],
            7: ['myte', 'taliban', 'svenske', 'smitte', 'squash'], 8: ['bonde', 'elsparkesykkel', 'regjering', 'spøkelse', 'restaurant'],
            9: ['olje', 'lefse', 'forfatter', 'trone', 'sv'], 10: ['skatt', 'pave', 'småbruk', 'coach', 'vaksine'],
            11: ['munch', 'kokain', 'fotball', 'strøm', 'flodhest']}
seksjoner = pygame.image.load(
    "/home/pi/elsysgame/sections.png")
sel_arrow = pygame.image.load(
    "/home/pi/elsysgame/down-arrow.png")
bakgrunn_startside = pygame.image.load(
    "/home/pi/elsysgame/staertside.png")
seksjoner_s1 = pygame.image.load("/home/pi/elsysgame/spiller1_bakgrunn.png")
seksjoner_s2 = pygame.image.load("/home/pi/elsysgame/spiller2_bakgrunn.png")
sections = pygame.image.load("/home/pi/elsysgame/sections.png")


GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Startknapp
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Poeng P1
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Poeng P2

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Next P1
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Select P1

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Next P2
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Select P2


def main():
    signal(SIGINT, quitBoi)

    running = True
    startside()

    # buttonstates:
    state_start = False
    pre_start = False

    s_next_p1 = False
    pre_next_p1 = False

    s_select_p1 = False
    pre_select_p1 = False

    s_next_p2 = False
    pre_next_p2 = False

    s_select_p2 = False
    pre_select_p2 = False

    globalscore_p1 = 0
    globalscore_p2 = 0

    while running:
        pygame.display.set_caption("N&N Minigame")
        time.sleep(0.2)

        pre_start = state_start
        state_start = GPIO.input(2)

        if pre_start and not state_start:
            print("Starter runde 1")
            rando_int = random.randint(1, 11)
            spiller1_ord = player_selection(rando_int, 1)  # Round 1
            spiller2_ord = player_selection(rando_int, 2)
            point = score(spiller1_ord, spiller2_ord)

            if point == "P1":
                globalscore_p1 += 1
                print("Point P1")
            elif point == "P2":
                globalscore_p2 += 1
                print("Point P2")

            rando_int2 = random.randint(1, 11)
            spiller1_ord = player_selection(rando_int2, 1)  # Round 2
            spiller2_ord = player_selection(rando_int2, 2)
            point = score(spiller1_ord, spiller2_ord)

            if point == "P1":
                globalscore_p1 += 1
                print("Point P1")
            elif point == "P2":
                globalscore_p2 += 1
                print("Point P2")

            rando_int3 = random.randint(1, 11)
            spiller1_ord = player_selection(rando_int3, 1)  # Round 3
            spiller2_ord = player_selection(rando_int3, 2)
            point = score(spiller1_ord, spiller2_ord)

            if point == "P1":
                globalscore_p1 += 1
                print("Point P1")
            elif point == "P2":
                globalscore_p2 += 1
                print("Point P2")

            if globalscore_p1 > globalscore_p2:  # Velger vinner
                globalscore_p1 = 0
                globalscore_p2 = 0
                resultater("Spiller 1")
                startside()
            elif globalscore_p2 > globalscore_p1:
                globalscore_p1 = 0
                globalscore_p2 = 0
                resultater("Spiller 2")
                startside()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

            pygame.display.update()
            clock.tick(30)
    print("Exited")


def startside():
    # Definerer her fonten til de ulike tekt boksene:
    # None sier hvilken font, fint ttf fil!
    print('Startside')
    bakgrunn_startside = pygame.image.load('/home/pi/elsysgame/staertside.png')
    screen.blit(bakgrunn_startside, (0, 0))
    pygame.display.update()


def resultater(spill_vinner):
    orange = [236, 143, 28]
    # Definerer fonten til teksten her:
    screen.fill('orange')
    text_font = pygame.font.Font(None, 90)
    text_font_overskirft = pygame.font.Font(None, 200)

# Definerer innhold som skal rendres:
    text_overskrift = text_font.render(
        'Vinneren av Nytt på Nytt Mini game Show er: ', False, 'White')
    text_vinner = text_font_overskirft.render(spill_vinner, False, 'Yellow')

# Rendrer ut på skjermen:
    screen.blit(text_overskrift, (250, 200))
    screen.blit(text_vinner, (620, 400))

    pygame.display.update()
    print("Starter timer 5s")
    time.sleep(20)
    print("Ferdig med timer 5s")


def player_selection(rando_int, player_int):

    #range = [236, 143, 28] #Denne linjen kan fjernes
    #screen.fill('Orange') # Denne linjen kan fjernes
    

    # Startposisjon til pilen:
    sel_arrow = pygame.image.load("/home/pi/elsysgame/selector.png")
    sel_arrow_X = 255
    sel_arrow_Y = 155

    s_next_p1 = False
    pre_next_p1 = False

    s_select_p1 = False
    pre_select_p1 = False

    s_next_p2 = False
    pre_next_p2 = False

    s_select_p2 = False
    pre_select_p2 = False

    # Hjelpefunsjoner:
    def arrow_pos(x, y):
        screen.blit(sel_arrow, (x, y))

    def text_to_screen(text, x_pos, y_pos):
        #pygame.sysFont
        temp_font = pygame.font.Font('/home/pi/elsysgame/pen_font.ttf', 40)
        img = temp_font.render('{}'.format(text), True, 'white')
        screen.blit(img, (x_pos, y_pos))

    word_comb = ""
    n = 0
    
    
    
    while n < 2:

        pre_next_p1 = s_next_p1
        s_next_p1 = GPIO.input(17)

        pre_select_p1 = s_select_p1
        s_select_p1 = GPIO.input(27)

        pre_next_p2 = s_next_p2
        s_next_p2 = GPIO.input(23)

        pre_select_p2 = s_select_p2
        s_select_p2 = GPIO.input(24)

        if (pre_next_p1 and not s_next_p1) and player_int == 1:
            print("Flytter pil P1")
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

        elif (pre_next_p2 and not s_next_p2) and player_int == 2:
            print("Flytter pil P2")
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

        if (pre_select_p1 and not s_select_p1) and player_int == 1:
            print("Svar angitt")
            if (sel_arrow_X == 255) and (sel_arrow_Y == 155) and (len(word_comb) == 0):
                word_comb = ord_dict[rando_int][0]
                n += 1
            elif (sel_arrow_X == 255) and (sel_arrow_Y == 155) and (len(word_comb) > 1):
                word_comb += ord_dict[rando_int][0]
                n += 1
            if (sel_arrow_X == 530) and (sel_arrow_Y == 155) and (len(word_comb) == 0):
                word_comb = ord_dict[rando_int][1]
                n += 1
            elif (sel_arrow_X == 530) and (sel_arrow_Y == 155) and (len(word_comb) > 0):
                word_comb += ord_dict[rando_int][1]
                n += 1
            if (sel_arrow_X == 255) and (sel_arrow_Y == 350) and (len(word_comb) == 0):
                word_comb = ord_dict[rando_int][2]
                n += 1
            elif (sel_arrow_X == 255) and (sel_arrow_Y == 350) and (len(word_comb) > 0):
                word_comb += ord_dict[rando_int][2]
                n += 1
            if (sel_arrow_X == 530) and (sel_arrow_Y == 350) and (len(word_comb) == 0):
                word_comb = ord_dict[rando_int][3]
                n += 1
            elif (sel_arrow_X == 530) and (sel_arrow_Y == 350) and (len(word_comb) > 0):
                word_comb += ord_dict[rando_int][3]
                n += 1

        elif (pre_select_p2 and not s_select_p2) and player_int == 2:
            print("Svar angitt")
            if (sel_arrow_X == 255) and (sel_arrow_Y == 155) and (len(word_comb) == 0):
                word_comb = ord_dict[rando_int][0]
                n += 1
            elif (sel_arrow_X == 255) and (sel_arrow_Y == 155) and (len(word_comb) > 1):
                word_comb += ord_dict[rando_int][0]
                n += 1
            if (sel_arrow_X == 530) and (sel_arrow_Y == 155) and (len(word_comb) == 0):
                word_comb = ord_dict[rando_int][1]
                n += 1
            elif (sel_arrow_X == 530) and (sel_arrow_Y == 155) and (len(word_comb) > 0):
                word_comb += ord_dict[rando_int][1]
                n += 1
            if (sel_arrow_X == 255) and (sel_arrow_Y == 350) and (len(word_comb) == 0):
                word_comb = ord_dict[rando_int][2]
                n += 1
            elif (sel_arrow_X == 255) and (sel_arrow_Y == 350) and (len(word_comb) > 0):
                word_comb += ord_dict[rando_int][2]
                n += 1
            if (sel_arrow_X == 530) and (sel_arrow_Y == 350) and (len(word_comb) == 0):
                word_comb = ord_dict[rando_int][3]
                n += 1
            elif (sel_arrow_X == 530) and (sel_arrow_Y == 350) and (len(word_comb) > 0):
                word_comb += ord_dict[rando_int][3]
                n += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                    pygame.quit()
        screen.fill('orange')
        if player_int == 1:
            screen.blit(seksjoner_s1, (0,0))
        elif player_int == 2:
            screen.blit(seksjoner_s2, (0,0))
        
        
            
        text_to_screen(word_comb, 190, 50)
        text_to_screen(ord_dict[1][0], 600, 400)
        text_to_screen(ord_dict[1][1], 450, 240)
        text_to_screen(ord_dict[1][2], 190, 480)
        text_to_screen(ord_dict[1][3], 450, 480)
        text_to_screen(ord_dict[1][4], 450, 480)
        arrow_pos(sel_arrow_X, sel_arrow_Y)
        clock.tick()
        print(clock.get_fps())
        pygame.display.update()
    time.sleep(1.5)
    return word_comb


def score(answer_p1, answer_p2):

    # STYLE
    pygame.display.set_caption("N&N Minigame")

    orange = [236, 143, 28]
    white = [255, 255, 255]
    screen.fill('orange')

    # ELEMENTS
    text_font = pygame.font.Font(None, 50)  # Delete after merge if duplicate
    page_header = text_font.render(
        'Spillvert, gi poeng til spiller med best svar', False, white)
    text_p1 = text_font.render('Spiller 1', False, white)
    text_p2 = text_font.render('Spiller 2', False, white)
    text_answer_p1 = text_font.render(answer_p1, False, white)
    text_answer_p2 = text_font.render(answer_p2, False, white)

    # Draw text elements
    screen.blit(page_header, (2300//4, 50))  # Draw page_header
    screen.blit(text_p1, (1840//6, 300))  # Draw text_p1
    screen.blit(text_p2, ((1840//6*4), 300))  # Draw text_p2
    screen.blit(text_answer_p1, (1840//6, 500))  # Answer_p1
    screen.blit(text_answer_p2, (1840//6*4, 500))  # Answer_p2

    # Center Line
    startX = 1840//2
    startY = 110
    endX = 1840//2
    endY = 1000
    width = 20
    pygame.draw.line(screen, white, (startX, startY), (endX, endY), width)

    # Cross Line
    startX2 = 0
    startY2 = 110
    endX2 = 1920
    endY2 = startY2
    pygame.draw.line(screen, white,
                     (startX2, startY2), (endX2, endY2), width)

    # Wait function:
    s_p1 = False
    pre_p1 = False

    s_p2 = False
    pre_p2 = False

    running = True
    pygame.display.update()  # Må kanskje flyttes ned

    while running:
        stringer = ""

        pre_p1 = s_p1
        s_p1 = GPIO.input(3)

        pre_p2 = s_p2
        s_p2 = GPIO.input(4)

        if pre_p1 and not s_p1:
            running = False
            stringer = "P1"

        if pre_p2 and not s_p2:
            running = False
            stringer = "P2"

    return stringer


if __name__ == "__main__":
    # call the main function
    main()
    pygame.quit()
