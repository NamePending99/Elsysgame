# import the pygame module, so you can use it
import pygame
from pygame import surface
from pygame.display import update

# define a main function


def SCORE(answer_p1, answer_p2):
    #Clock (OPTIONAL)
    clock = pygame.time.Clock()

    # initialize the pygame module
    pygame.init()

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # define a variable to control the main loop
    running = True

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
    text_p2 = text_font.render('Spiller 1', False, white)
    text_answer_p1 = text_font.render(answer_p1, False, white)
    text_answer_p2 = text_font.render(answer_p2, False, white)

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    print("Spiller 1 får poeng")
                    return 1, 0
                if event.key == pygame.K_2:
                    print("Spiller 2 får poeng")
                    return 0, 1

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
        clock.tick(60)


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    print(SCORE("PLACEHOLDER 1", "PLACEHOLDER 2"))
    # PLACEHOLDER ARGUMENT FOR ANSWERS^
