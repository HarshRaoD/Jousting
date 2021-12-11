""" This file contains the code to run the 1 player game of Jousting """
import random
from time import sleep
import pygame


def botEasy(x, y):
    """Returns a list: [x_change, y_change] for computer to move (easy difficulty)
        :param y: y position of bot
        :param x: x position of bot"""
    list_change = [0, 0]
    while True:
        val = random.randint(0, 10)
        # To make sure knight shouldn't get stuck in the corner
        if x == 15:
            if y == 15:
                if val == 1 or val == 4 or val == 8:
                    break
            elif y == 585:
                if val == 1 or val == 2 or val == 5:
                    break
            elif val != 3:
                break
        elif x == 785:
            if y == 0:
                if val == 3 or val == 4 or val == 7:
                    break
            elif y == 585:
                if val == 3 or val == 2 or val == 6:
                    break
            elif val != 1:
                break
        elif y == 15 and val != 2:
            break
        elif y == 585 and val != 4:
            break
        else:
            break

    if val == 1:
        # Move Right
        list_change[0] = 1
        list_change[1] = 0
    elif val == 2:
        # Move Up
        list_change[0] = 0
        list_change[1] = -1
    elif val == 3:
        # Move Left
        list_change[0] = -1
        list_change[1] = 0
    elif val == 4:
        # Move Down
        list_change[0] = 0
        list_change[1] = 1
    elif val == 5:
        # Move Up & Right
        list_change[0] = 1
        list_change[1] = -1
    elif val == 6:
        # Move Up & Left
        list_change[0] = -1
        list_change[1] = -1
    elif val == 7:
        # Move Down & Left
        list_change[0] = -1
        list_change[1] = 1
    elif val == 8:
        # Move Down & Right
        list_change[0] = 1
        list_change[1] = 1

    return list_change


def botMedium(x, y):
    """Returns a list: [x_change, y_change] for computer to move (easy difficulty)
        :param y: y position of bot
        :param x: x position of bot"""
    list_change = [0, 0]
    while True:
        val = random.randint(0, 10)
        # To make sure knight shouldn't get stuck in the corner
        if x == 15:
            if y == 15:
                if val == 1 or val == 4 or val == 8:
                    break
            elif y == 585:
                if val == 1 or val == 2 or val == 5:
                    break
            elif val != 3 and val != 6 and val != 7 and val != 2 and val != 4:
                break
        elif x == 785:
            if y == 0:
                if val == 3 or val == 4 or val == 7:
                    break
            elif y == 585:
                if val == 3 or val == 2 or val == 6:
                    break
            elif val != 1 and val != 5 and val != 8 and val != 2 and val != 4:
                break
        elif y == 15 and val != 2 and val != 5 and val != 6 and val != 1 and val != 3:
            break
        elif y == 585 and val != 4 and val != 7 and val != 8 and val != 1 and val != 3:
            break
        else:
            break

    if val == 1:
        # Move Right
        list_change[0] = 1.5
        list_change[1] = 0
    elif val == 2:
        # Move Up
        list_change[0] = 0
        list_change[1] = 1.5
    elif val == 3:
        # Move Left
        list_change[0] = -1.5
        list_change[1] = 0
    elif val == 4:
        # Move Down
        list_change[0] = 0
        list_change[1] = 1.5
    elif val == 5:
        # Move Up & Right
        list_change[0] = 1.5
        list_change[1] = -1.5
    elif val == 6:
        # Move Up & Left
        list_change[0] = -1.5
        list_change[1] = -1.5
    elif val == 7:
        # Move Down & Left
        list_change[0] = -1.5
        list_change[1] = 1.5
    elif val == 8:
        # Move Down & Right
        list_change[0] = 1.5
        list_change[1] = 1.5

    return list_change


def botHard(x, y, x1, y1, my_spear, opponent_spear):
    """ Returns a list: [x_change, y_change] for computer to move (hard difficulty)
        :param y1: y position of opponent
        :param y: y position of bot
        :param x: x position of bot
        :param x1: x position of opponent
        :param my_spear: Positions of Bot's spear tip
        :param opponent_spear: Positions of Opponent's spear tip"""
    # TODO Debug this function
    threat_me = False  # True if there is a threat to bot

    CHECK_DIST = 30

    # Check for threat_me
    # TODO Change values of threat distance
    for spearTip in opponent_spear:
        if ((spearTip[0] > x - CHECK_DIST and spearTip[0] < x + CHECK_DIST) and (
                spearTip[1] > y - CHECK_DIST and spearTip[1] < y + CHECK_DIST)):
            threat_me = True
            threat_spear = spearTip
            break

    threat_you = False  # True if there is a threat to opponent
    # Check for threat_you
    for spearTip in my_spear:
        if ((spearTip[0] > x1 - CHECK_DIST and spearTip[0] < x1 + CHECK_DIST) and (
                spearTip[1] > y1 - CHECK_DIST and spearTip[1] < y1 + CHECK_DIST)):
            threat_you = True
            threat_spear = spearTip
            break

    print("me:", threat_me, " you: ", threat_you)
    i = 0
    while True:
        val = random.randint(0, 9)
        if i > 15:  # To make sure we don't stuck in an infinite loop
            break
        i += 1
        '''# To make sure knight shouldn't get stuck in the corner
        if (x == 15):
            if (y == 15):
                if not (val == 1 or val == 4 or val == 8):
                    continue
            elif (y == 585):
                if not (val == 1 or val == 2 or val == 5):
                    continue
            elif not (val != 3):
                continue
        elif (x == 785):
            if (y == 0):
                if not (val == 3 or val == 4 or val == 7):
                    continue
            elif (y == 585):
                if not (val == 3 or val == 2 or val == 6):
                    continue
            elif not (val != 1):
                continue
        elif not (y == 15 and val != 2):
            continue
        elif not (y == 585 and val != 4):
            continue'''

        if threat_me:
            if (threat_spear[0] <= x and threat_spear[1] <= y):
                # Threat at Top Left
                val = 8
                break
            elif (threat_spear[0] > x and threat_spear[1] <= y):
                # Threat at Top Right
                val = 7
                break
            elif (threat_spear[0] > x and threat_spear[1] > y):
                # Threat at Down Right
                val = 6
                break
            elif (threat_spear[0] <= x and threat_spear[1] > y):
                # Threat at Down Left
                val = 5
                break

        if threat_you:
            if (threat_spear[0] <= x and threat_spear[1] <= y):
                # Threat at Top Left
                val = 6
                break
            elif (threat_spear[0] > x and threat_spear[1] <= y):
                # Threat at Top Right
                val = 5
                break
            elif (threat_spear[0] > x and threat_spear[1] > y):
                # Threat at Down Right
                val = 8
                break
            elif (threat_spear[0] <= x and threat_spear[1] > y):
                # Threat at Down Left
                val = 7
                break

        break

    list_change = [0, 0]
    # print(val)
    if (val == 1):
        print("# Move Right")
        list_change[0] = 1
        list_change[1] = 0
    elif (val == 2):
        print("# Move Up")
        list_change[0] = 0
        list_change[1] = -1
    elif (val == 3):
        print("# Move Left")
        list_change[0] = -1
        list_change[1] = 0
    elif (val == 4):
        print("# Move Down")
        list_change[0] = 0
        list_change[1] = 1
    elif (val == 5):
        print("# Move Up & Right")
        list_change[0] = 1
        list_change[1] = -1
    elif (val == 6):
        print("# Move Up & Left")
        list_change[0] = -1
        list_change[1] = -1
    elif (val == 7):
        print("# Move Down & Left")
        list_change[0] = -1
        list_change[1] = 1
    elif (val == 8):
        print("# Move Down & Right")
        list_change[0] = 1
        list_change[1] = 1

    return list_change


def oneRedPlayerGame():
    """Plays the game with player being red colour (easy difficulty)"""
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

            # If the key is released
            if event.type == pygame.KEYUP:  # KEYUP means key has been released
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_red_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_red_change = 0

            # Update control of green
            list_green = botEasy(x_green, y_green)
            x_green_change = list_green[0]
            y_green_change = list_green[1]

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


def oneRedPlayerGameMed():
    """Plays the game with player being red colour (medium difficulty)"""
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
    while (running):
        # Iterate through all possible events
        for event in pygame.event.get():
            # To Quit the game if X has been pressed
            if (event.type == pygame.QUIT):
                running = False
            # If a key is pressed
            if (event.type == pygame.KEYDOWN):  # KEYDOWN means key is pressed
                # Check Controls for Red
                if (event.key == pygame.K_LEFT):
                    # print("R Left")
                    x_red_change = -1
                if (event.key == pygame.K_RIGHT):
                    # print("R Right")
                    x_red_change = 1
                if (event.key == pygame.K_UP):
                    # print("R Up")
                    y_red_change = -1
                if (event.key == pygame.K_DOWN):
                    # print("R Down")
                    y_red_change = 1

            # If the key is released
            if event.type == pygame.KEYUP:  # KEYUP means key has been released
                if (event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT):
                    x_red_change = 0
                if (event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                    y_red_change = 0

            # Update control of green
            list_green = botMedium(x=x_green, y=y_green)
            x_green_change = list_green[0]
            y_green_change = list_green[1]

        # To fill the screen with the colour blue
        screen.fill(blue)

        # Updating Position of Red Player
        if (x_red + x_red_change > 15 and x_red + x_red_change < 785):
            x_red += x_red_change
        if (y_red + y_red_change > 15 and y_red + y_red_change < 585):
            y_red += y_red_change

        # Updating Position of Green Player
        if (x_green + x_green_change > 15 and x_green + x_green_change < 785):
            x_green += x_green_change
        if (y_green + y_green_change > 15 and y_green + y_green_change < 585):
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
            if ((spearTip[0] > x_green - 15 and spearTip[0] < x_green + 15) and (
                    spearTip[1] > y_green - 15 and spearTip[1] < y_green + 15)):
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
            if ((spearTip[0] > x_red - 15 and spearTip[0] < x_red + 15) and (
                    spearTip[1] > y_red - 15 and spearTip[1] < y_red + 15)):
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
        if (running == False and game_end):
            sleep(5)

    pygame.quit()
    return


def oneGreenPlayerGame():
    """Plays the game with player being green colour (easy difficulty)"""
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
    while (running):
        # Iterate through all possible events
        for event in pygame.event.get():
            # To Quit the game if X has been pressed
            if (event.type == pygame.QUIT):
                running = False
            # If a key is pressed
            if (event.type == pygame.KEYDOWN):  # KEYDOWN means key is pressed
                # Check Controls for Green
                if (event.key == pygame.K_a):
                    print("G Left")
                    x_green_change = -1
                if (event.key == pygame.K_d):
                    print("G Right")
                    x_green_change = 1
                if (event.key == pygame.K_w):
                    print("G Up")
                    y_green_change = -1
                if (event.key == pygame.K_s):
                    print("G Down")
                    y_green_change = 1

            # If the key is released
            if event.type == pygame.KEYUP:  # KEYUP means key has been released
                if (event.key == pygame.K_a or event.key == pygame.K_d):
                    x_green_change = 0
                if (event.key == pygame.K_w or event.key == pygame.K_s):
                    y_green_change = 0

            # Update control of red
            list_red = botEasy(x_red, y_red)
            x_red_change = list_red[0]
            y_red_change = list_red[1]

        # To fill the screen with the colour blue
        screen.fill(blue)

        # Updating Position of Red Player
        if (x_red + x_red_change > 15 and x_red + x_red_change < 785):
            x_red += x_red_change
        if (y_red + y_red_change > 15 and y_red + y_red_change < 585):
            y_red += y_red_change

        # Updating Position of Green Player
        if (x_green + x_green_change > 15 and x_green + x_green_change < 785):
            x_green += x_green_change
        if (y_green + y_green_change > 15 and y_green + y_green_change < 585):
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
            if ((spearTip[0] > x_green - 15 and spearTip[0] < x_green + 15) and (
                    spearTip[1] > y_green - 15 and spearTip[1] < y_green + 15)):
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
            if ((spearTip[0] > x_red - 15 and spearTip[0] < x_red + 15) and (
                    spearTip[1] > y_red - 15 and spearTip[1] < y_red + 15)):
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
        if (running == False and game_end):
            sleep(5)

    pygame.quit()
    return


def oneGreenPlayerGameMed():
    """Plays the game with player being green colour (medium difficulty)"""
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
    while (running):
        # Iterate through all possible events
        for event in pygame.event.get():
            # To Quit the game if X has been pressed
            if (event.type == pygame.QUIT):
                running = False
            # If a key is pressed
            if (event.type == pygame.KEYDOWN):  # KEYDOWN means key is pressed
                # Check Controls for Green
                if (event.key == pygame.K_a):
                    print("G Left")
                    x_green_change = -1
                if (event.key == pygame.K_d):
                    print("G Right")
                    x_green_change = 1
                if (event.key == pygame.K_w):
                    print("G Up")
                    y_green_change = -1
                if (event.key == pygame.K_s):
                    print("G Down")
                    y_green_change = 1

            # If the key is released
            if event.type == pygame.KEYUP:  # KEYUP means key has been released
                if (event.key == pygame.K_a or event.key == pygame.K_d):
                    x_green_change = 0
                if (event.key == pygame.K_w or event.key == pygame.K_s):
                    y_green_change = 0

            # Update control of red
            list_red = botMedium(x_red, y_red)
            x_red_change = list_red[0]
            y_red_change = list_red[1]

        # To fill the screen with the colour blue
        screen.fill(blue)

        # Updating Position of Red Player
        if (x_red + x_red_change > 15 and x_red + x_red_change < 785):
            x_red += x_red_change
        if (y_red + y_red_change > 15 and y_red + y_red_change < 585):
            y_red += y_red_change

        # Updating Position of Green Player
        if (x_green + x_green_change > 15 and x_green + x_green_change < 785):
            x_green += x_green_change
        if (y_green + y_green_change > 15 and y_green + y_green_change < 585):
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
            if ((spearTip[0] > x_green - 15 and spearTip[0] < x_green + 15) and (
                    spearTip[1] > y_green - 15 and spearTip[1] < y_green + 15)):
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
            if ((spearTip[0] > x_red - 15 and spearTip[0] < x_red + 15) and (
                    spearTip[1] > y_red - 15 and spearTip[1] < y_red + 15)):
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
        if (running == False and game_end):
            sleep(5)

    pygame.quit()
    return
