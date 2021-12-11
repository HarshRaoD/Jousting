""" This file contains the code to run the 2 player game of Jousting """

from time import sleep
import pygame


def twoPlayerGame():
    """This function runs the 2 player game of jousting"""
    # Initialise pygame
    pygame.init()

    game_end = False  # False by default, set to true when one player wins

    # Create the window
    screen = pygame.display.set_mode((800, 600))  # width 800 and height 600 pixels
    pygame.display.set_caption("Jousting")  # Set the title
    ''' Icons made by "https://www.freepik.com"  
    from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>'''
    pygame.display.set_icon(pygame.image.load("knight.png"))

    # Initialing Color
    red = (255, 0, 0)  # (r,g,b)
    green = (0, 255, 0)
    blue = (0, 0, 150)

    # Starting Position
    x_green = 80
    y_green = 80
    x_red = 720
    y_red = 520

    # Other initialisations
    x_red_change = 0
    y_red_change = 0
    x_green_change = 0
    y_green_change = 0
    red_spear = [[x_red - 60, y_red], [x_red + 60, y_red]]  # Positions of Red's spear tip
    green_spear = [[x_green, y_green - 60], [x_green, y_green + 60]]  # Positions of Green's spear tip

    # Game Loop
    running = True
    while running:
        # Iterate through all possible events
        for event in pygame.event.get():
            # To Quit the game if X has been pressed
            if event.type == pygame.QUIT:
                running = False
            # If a key is pressed
            if event.type == pygame.KEYDOWN:  # KEYDOWN means key is pressed
                # Check Controls for Red
                if event.key == pygame.K_LEFT:
                    print("R Left")
                    x_red_change = -1
                if event.key == pygame.K_RIGHT:
                    print("R Right")
                    x_red_change = 1
                if event.key == pygame.K_UP:
                    print("R Up")
                    y_red_change = -1
                if event.key == pygame.K_DOWN:
                    print("R Down")
                    y_red_change = 1

                # Check Controls for Green
                if event.key == pygame.K_a:
                    print("G Left")
                    x_green_change = -1
                if event.key == pygame.K_d:
                    print("G Right")
                    x_green_change = 1
                if event.key == pygame.K_w:
                    print("G Up")
                    y_green_change = -1
                if event.key == pygame.K_s:
                    print("G Down")
                    y_green_change = 1

            # If the key is released
            if event.type == pygame.KEYUP:  # KEYUP means key has been released
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_red_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_red_change = 0
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_green_change = 0
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    y_green_change = 0

        # To fill the screen with the colour blue
        screen.fill(blue)

        # Updating Position of Red Player
        if 15 < x_red + x_red_change < 785:
            x_red += x_red_change
        if 15 < y_red + y_red_change < 585:
            y_red += y_red_change

        # Updating Position of Green Player
        if 15 < x_green + x_green_change < 785:
            x_green += x_green_change
        if 15 < y_green + y_green_change < 585:
            y_green += y_green_change
        red_spear = [[x_red - 60, y_red], [x_red + 60, y_red]]  # Positions of Red's spear tip
        green_spear = [[x_green, y_green - 60], [x_green, y_green + 60]]  # Positions of Green's spear tip

        # Drawing Red Player
        pygame.draw.rect(screen, red,
                         pygame.Rect(x_red - 15, y_red - 15, 30, 30))  # pygame.Rect(left, top, width, height)
        pygame.draw.line(screen, red, (x_red - 60, y_red - 1), (x_red + 60, y_red - 1), 3)
        pygame.draw.circle(screen, red, tuple(red_spear[0]), 3)
        pygame.draw.circle(screen, red, tuple(red_spear[1]), 3)

        # Drawing Green Player
        pygame.draw.rect(screen, green,
                         pygame.Rect(x_green - 15, y_green - 15, 30, 30))  # pygame.Rect(left, top, width, height)
        pygame.draw.line(screen, green, (x_green - 1, y_green - 60), (x_green - 1, y_green + 60), 3)
        pygame.draw.circle(screen, green, tuple(green_spear[0]), 3)
        pygame.draw.circle(screen, green, tuple(green_spear[1]), 3)
        pygame.display.flip()

        # Check if Red Wins
        for spearTip in red_spear:
            if (x_green - 15 < spearTip[0] < x_green + 15) and (y_green - 15 < spearTip[1] < y_green + 15):
                print("Red Wins")
                pygame.draw.rect(screen, blue, pygame.Rect(x_green - 10, y_green - 10, 20, 20))  # To show green is dead
                running = False
                game_end = True
                # Display Red wins on the screen
                font = pygame.font.Font('freesansbold.ttf', 32)  # Creating a font object
                text = font.render('Red Wins', True, red, blue)
                text.get_rect().center = (800, 600)
                screen.blit(text, text.get_rect())
                break

        # Check if Green Wins
        for spearTip in green_spear:
            if (x_red - 15 < spearTip[0] < x_red + 15) and (y_red - 15 < spearTip[1] < y_red + 15):
                print("Green Wins")
                pygame.draw.rect(screen, blue, pygame.Rect(x_red - 10, y_red - 10, 20, 20))
                running = False
                game_end = True
                # Display Green wins on the screen
                font = pygame.font.Font('freesansbold.ttf', 32)  # Creating a font object
                text = font.render('Green Wins', True, green, blue)
                text.get_rect().center = (400, 300)
                screen.blit(text, text.get_rect())
                break

        pygame.display.update()
        if running == False and game_end:
            sleep(5)

    pygame.quit()
    return
