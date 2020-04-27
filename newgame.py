from config import *
from enemyconfig import *

pygame.init()
runmain = True
runpro = True

while True:  # loop to keep the window running
    victory1 = 0  # initialising the scores and number of rounds won to 0
    victory2 = 0
    score1 = 0
    score2 = 0
    flag = 0
    k = 0
    subtr = 0
    draw = 0
    num_of_enemies = 30
    num_of_fixedenemies = 30

    for k in range(6):
        # This loop is for conducting each match for player 1 and 2
        draw = 0
        cross = 0
        t = 500
        gameover = 0
        runmain = True

        while runmain:  # Loop for conducting the round
            # Setting up the display
            screen = pygame.display.set_mode(screen_size)
            halt = False
            # halt is to stop the game in case of crossing the river
            # or dying from obstacle
            pygame.display.set_caption(GAMENAME)  # setting game name and icon
            pygame.display.set_icon(ICON)

            if k % 2 == 1:
                # checking if player 1 is playing, or player 2
                # and initialising their icon and initial positions
                playerImg = PLAYER2
                playerX = 720
                playerY = 0
            else:
                playerImg = PLAYER1
                playerX = 720
                playerY = 836

            # initialising the necessary variables for fixed obstacles
            fixedenemyImg = []
            fixedenemyX = []
            fixedenemyY = []
            fixedenemyX_change = []
            fixedenemyY_change = []

            # initialising the necessary variables for moving obstacles
            enemyImg = []
            enemyX = []
            enemyY = []
            enemyX_change = []
            enemyY_change = []

            playerY_change = 0  # initialising the moving of player to 0
            playerX_change = 0

            score = 0
            num_of_enemies = 30 + 10 * (k // 2)
            # increasing number of enemies based upon the current round
            visited = [0] * num_of_enemies
            # array to check if score has been given for the ith obstacle
            num_of_fixedenemies = 30 + 10 * (k // 2)
            visitedfixed = [0] * num_of_fixedenemies

            # loop to place all the enemies in the game
            for i in range(num_of_enemies):
                num = random.randint(0, 5)
                enemyImg.append(pygame.image.load(ENEMY[num]))  # selecting
                # random enemy from array of enemies
                enemyY.append(POSITION[random.randint(0, 4)])
                enemyX.append(random.randint(0, 1300))
                if k % 2 == 0:
                    enemyX_change.append(SPEED[num] + 1.5 * victory1)
                    # choosing the speed of the enemy
                else:
                    enemyX_change.append(SPEED[num] + 1.5 * victory2)
            for i in range(num_of_fixedenemies):
                fixedenemyImg.append(pygame.image.load(
                    FIXEDENEMIES[random.randint(0, 7)]))
                fixedenemyY.append(FIXEDPOSITION[random.randint(0, 5)])
                fixedenemyX.append(random.randint(0, 1300))
                while fixedenemyY[i] == 19 and fixedenemyX[
                        i] >= 656 and fixedenemyX[i] <= 848:
                    # loop to remove the enemy from the initial position
                    # of the player(if randomly alloted)
                    fixedenemyX[i] = random.randint(0, 1300)
                while fixedenemyY[i] == 819 and fixedenemyX[
                        i] >= 656 and fixedenemyX[i] <= 848:
                    fixedenemyX[i] = random.randint(0, 1300)

            stop = False

            def player(x, y):
                # function to load the player at x and y co-ordinate
                screen.blit(playerImg, (x, y))

            def enemyfun(x, y, j):
                # function to display ith moving enemy at (x, y)
                screen.blit(enemyImg[j], (x, y))

            def fixedenemyfun(x, y, j):
                # function to display ith fixed enemy at (x, y)
                screen.blit(fixedenemyImg[j], (x, y))

            def iscollision(enemyx, enemyy, playerx, playery):
                # function to check for collision in the game
                distance = math.sqrt(math.pow(enemyx - playerx, 2) +
                                     (math.pow(enemyy - playery, 2)))
                # finding distance between obstacle and player
                if distance < 45:
                    # if distance <45px, collision has happened
                    return True
                else:
                    return False

            running = True
            while running:
                while t > 0:
                    # loop to do an intro to the new round
                    # with the round and player no.
                    screen.fill(BLACK)
                    text = ARCADE_FONT.render(
                        "ROUND " + str(k // 2 + 1) + " BEGINS", True,
                        RED)
                    screen.blit(text, (500, 250))
                    text = FONT.render(READY + str(k % 2 + 1), True,
                                       RED)
                    screen.blit(text, (450, 300))
                    t -= 1
                    pygame.display.update()

                subtr += 0.1 * (
                        k // 2 + 1)
                # subtr is being used to keep decreasing thescore
                # based on the time elapsed,proprtional to the round number
                if subtr >= 1:  # decreasing the score after subtr becomes 1
                    score -= 1
                    subtr = 0

                screen.fill(BLUE)  # creating the blue river background

                # creating the green rectangles for the land
                pygame.draw.rect(screen, GREEN, (0, 830, 1400, 70))
                pygame.draw.rect(screen, GREEN, (0, 670, 1400, 70))
                pygame.draw.rect(screen, GREEN, (0, 510, 1400, 70))
                pygame.draw.rect(screen, GREEN, (0, 350, 1400, 70))
                pygame.draw.rect(screen, GREEN, (0, 190, 1400, 70))
                pygame.draw.rect(screen, GREEN, (0, 30, 1400, 70))
                pygame.draw.rect(screen, GREEN, (0, 0, 1400, 50))

                for event in pygame.event.get():
                    # loop to keep getting input from the user
                    if event.type == pygame.QUIT:
                        # if the player presses quit, exit
                        sys.exit()
                    if k % 2 == 0:  # movement keys for player 1
                        if event.type == pygame.KEYDOWN:
                            # keep changing x and y of player when the
                            # keys are kept pressed
                            if event.key == pygame.K_LEFT:
                                playerX_change = -2.8
                                # co-ordinate is being changed by 2.8
                                # (speed of player)
                            if event.key == pygame.K_RIGHT:
                                playerX_change = 2.8
                            if event.key == pygame.K_UP:
                                playerY_change = -2.8
                            if event.key == pygame.K_DOWN:
                                playerY_change = 2.8
                        if event.type == pygame.KEYUP:
                            # when the keys are lifted, stop moving the player
                            if event.key == pygame.K_LEFT or \
                                    event.key == pygame.K_RIGHT:
                                playerX_change = 0
                            if event.key == pygame.K_DOWN or \
                                    event.key == pygame.K_UP:
                                playerY_change = 0
                    else:  # movement keys for player 2
                        if event.type == pygame.KEYDOWN:
                            # keep changing x and y of player when the
                            # keys are kept pressed
                            if event.key == pygame.K_a:
                                # co-ordinate is being changed by 2.8(
                                # speed of player)
                                playerX_change = -2.8
                            if event.key == pygame.K_d:
                                playerX_change = 2.8
                            if event.key == pygame.K_w:
                                playerY_change = -2.8
                            if event.key == pygame.K_s:
                                playerY_change = 2.8
                        if event.type == pygame.KEYUP:
                            # when the keys are lifted, stop moving the player
                            if event.key == pygame.K_d or \
                                    event.key == pygame.K_a:
                                playerX_change = 0
                            if event.key == pygame.K_w or \
                                    event.key == pygame.K_s:
                                playerY_change = 0

                playerX += playerX_change
                # changing the co-ordinate of player
                # dependant upon the key press
                playerY += playerY_change

                # if statements to keep the player within the screen window
                if playerY <= 0:
                    playerY = 0
                if playerX <= 0:
                    playerX = 0
                if playerY >= 836:
                    playerY = 836
                if playerX > 1336:
                    playerX = 1336

                for i in range(num_of_fixedenemies):
                    # loop to display all the fixed obstacles on the screen
                    fixedenemyfun(fixedenemyX[i], fixedenemyY[i], i)

                for i in range(num_of_enemies):
                    # loop to increase score after crossing obstacles
                    if playerY < enemyY[i] and visited[i] == 0 and k % 2 == 0:
                        score += 10
                        # condition for player 1 to cross obstacle
                        visited[i] = 1
                        # marking ith obstacle as already crossed
                    if playerY > enemyY[i] and visited[i] == 0 and k % 2 == 1:
                        score += 10
                        # condition for player 2 to cross an obstacle
                        visited[i] = 1
                    if k % 2 == 0 and playerY <= 0 and visitedfixed[i] == 0:
                        score += 5
                        visitedfixed[i] = 1
                    if k % 2 == 1 and playerY >= 836 and visitedfixed[i] == 0:
                        score += 5
                        visitedfixed[i] = 1
                    enemyX[i] += enemyX_change[i]
                    if playerY < fixedenemyY[i] and \
                            visitedfixed[i] == 0 and k % 2 == 0:
                        score += 5
                        visitedfixed[i] = 1
                    if playerY > enemyY[i] and \
                            visitedfixed[i] == 0 and k % 2 == 1:
                        score += 5
                        visitedfixed[i] = 1
                    if enemyX[i] >= 1400:
                        enemyX[i] = -64

                    collision = iscollision(enemyX[i], enemyY[i], playerX,
                                            playerY)
                    # checking if collision occured between obstacle and player
                    if collision:
                        halt = True
                    collision = iscollision(
                        fixedenemyX[i], fixedenemyY[i], playerX, playerY)
                    if collision:
                        halt = True

                    enemyfun(enemyX[i], enemyY[i], i)
                    # updating the position of the obstacles

                if k % 2 == 0:  # keeping score for player 1
                    score1 = score
                else:
                    score2 = score  # keeping score for player 2

                player(playerX, playerY)  # updating player position

                if playerY == 0 and k % 2 == 0:
                    # condition for player 1 to cross the river
                    stop = True  # round over
                    cross = 1  # river crossed
                    score += 100  # bonus for crossing the river
                if playerY >= 836 and k % 2 == 1:
                    # condition for player 2 to cross the river
                    stop = True  # round over
                    cross = 1  # river crossed
                    score += 100  # bonus for crossing the river

                if k % 2 == 0:  # keeping score for player 1
                    score1 = score
                else:
                    score2 = score  # keeping score for player 2

                scoredisp = ARCADE_FONT.render(
                    "SCORE Player 1: " + str(score1), True, RED)
                # displaying scores
                screen.blit(scoredisp, (0, 0))
                scoredisp = ARCADE_FONT.render(
                    "SCORE Player 2: " + str(score2), True, (0, 0, 255))
                screen.blit(scoredisp, (0, 40))

                scoredisp = ARCADE_FONT.render(
                    str(victory1) + "-" + str(victory2), True,
                    RED)  # displaying rounds won by each
                screen.blit(scoredisp, (700, 0))

                scoredisp1 = ARCADE_FONT.render(
                    "ROUND " + str(k // 2 + 1), True, RED)
                # displaying round number
                screen.blit(scoredisp1, (650, 45))

                if k % 2 == 1 and (
                        stop is True or halt is True):
                    # checking who is the winner of each
                    # round(after the loop executes 2 times)
                    if score1 >= score2:
                        victory1 += 1
                        # storing number of games won by player 1
                        winner = 1
                        # storing winner of current round
                    if score2 >= score1:
                        victory2 += 1
                        winner = 2
                    if score1 == score2:
                        draw = 1  # to check if round is a tie
                    score1 = 0
                    score2 = 0
                while stop or halt:
                    # loop to show final score and stop the play
                    if cross == 1:
                        # condition to show success message
                        res = OVER_FONT.render(CONGO,
                                               True,
                                               BLACK)
                        screen.blit(res, (10, 100))
                    else:
                        # condition to show hit by obstacle message
                        res = OVER_FONT.render(COLLI,
                                               True,
                                               RED)
                        screen.blit(res, (20, 100))
                    res = OVER_FONT.render(FINSCOR + str(
                        k % 2 + 1) + " IS " + str(score), True, BLACK)
                    # message to show final score
                    screen.blit(res, (200, 250))
                    res = OVER_FONT.render(ENTER, True,
                                           BLACK)  # message to continue
                    screen.blit(res, (250, 340))
                    if k % 2 == 1:
                        gameover = 300
                        # loop control variable to show winner of each round
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                # if enter is pressed, get out of
                                # all loops to start next match
                                stop = False
                                running = False
                                halt = False
                                runmain = False
                    pygame.display.update()

                while gameover > 0 and k % 2 == 1:
                    # loop to display winner of each round
                    screen.fill(BLACK)
                    if draw != 1:  # if not a tie, we have a winner
                        text = FONT.render("ROUND " + str(k // 2 + 1) +
                                           " WON BY PLAYER " + str(winner),
                                           True, RED)
                        # displaying round winner
                    else:
                        text = FONT.render(
                            ROUND_TIE, True,
                            RED)  # tie message
                    screen.blit(text, (500, 250))
                    gameover -= 1
                    pygame.display.update()
                pygame.display.update()
    ab = 800  # control variable for game winner loop
    while ab > 0:
        screen.fill(BLACK)

        if victory1 > victory2:
            # checking which player won more rounds, and is a winner
            winner1 = 1
        elif victory2 > victory1:
            winner1 = 2

        if victory1 == victory2:
            text = FONT.render(
                TIE, True,
                RED)  # message if game is tied
        else:
            text = FONT.render(
                "PLAYER " + str(winner1) + WIN, True,
                RED)  # printing the winner of the game
        screen.blit(text, (500, 250))

        text = FONT.render(
            NEWGAME, True,
            RED)
        screen.blit(text, (450, 290))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # waiting for enter key response to start a new game
                    ab = -1

        pygame.display.update()
