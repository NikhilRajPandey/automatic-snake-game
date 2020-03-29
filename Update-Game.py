import pygame
import random
import math
# main game
def loop():
    pygame.init()
    screen_width = 1200
    screen_height = 800
    game =  pygame.display.set_mode((screen_width,screen_height))
    ex = False
    gameover = False
    # colors
    white = (255,255,255)
    bl = (25,50,100)
    red = (255,0,0)
    blue = (51, 51, 255)
    # Spesfic variables
    x = 40
    y = 50
    h = 30
    f_x = math.ceil(random.randint(20,1100) / 10) * 10
    f_y = math.ceil(random.randint(20,700) / 10) * 10
    velocity_x = 0
    velocity_y = 0
    fps = 45
    clock = pygame.time.Clock()
    snk_l = []
    snk_le = 1
    current_direction = 0
    font = pygame.font.SysFont(None,55)
    # stoping from exiting
    def plot():
        for v_x,v_y in snk_l:
            pygame.draw.rect(game, bl, [v_x, v_y, h, h])
    def search(axis,snk_l):
        returning_value = []
        if axis == 0: # Means x-axis
            for x,y in snk_l[:-2]:
                if snk_l[0][0] == x:
                    returning_value.append([x,y])
        else: # Means y-axis
            for x,y in snk_l[:-2]:
                if snk_l[0][1] == y:
                    returning_value.append([x,y])
        return returning_value
    
    def will_it_collid(direction,snk_l):
        collid_part = []
        collid_part_len = None
        if direction == 1:
            # Finding those part that can collide from head of snake
            for index,cordinates in enumerate(snk_l[::-2]):
                if snk_l[0][0] == cordinates[1] and cordinates[0] > snk_l[0][0]:
                    collid_part.append(cordinates)
                    collid_part_len = len(snk_l) - index
                    break
            if (collid_part[0][0] - snk_l[0][0] - collid_part_len) < 1:
                return False
            else:
                return True
        elif direction == 2:
            for index,cordinates in enumerate(snk_l[::-2]):
                if snk_l[0][0] == cordinates[1] and cordinates[0] < snk_l[0][0]:
                    collid_part.append(cordinates)
                    collid_part_len = len(snk_l) - index
                    break
            if (snk_l[0][0] - collid_part[0][0] - collid_part_len) < 1:
                return False
            else:
                return True
        elif direction == 3:
            for index,cordinates in enumerate(snk_l[::-2]):
                if snk_l[0][1] == cordinates[0] and cordinates[1] > snk_l[0][0]:
                    collid_part.append(cordinates)
                    collid_part_len = len(snk_l) - index
                    break
            if (collid_part[0][1] - snk_l[0][1] - collid_part_len) < 1:
                return False
            else:
                return True
        elif direction == 4:
            for index,cordinates in enumerate(snk_l[::-2]):
                if snk_l[0][1] == cordinates[0] and cordinates[1] < snk_l[0][0]:
                    collid_part.append(cordinates)
                    collid_part_len = len(snk_l) - index
                    break
            if (snk_l[0][1] - collid_part[0][1] - collid_part_len) < 1:
                return False
            else:
                return True

    bg = pygame.image.load("back.jpg")
    bg2 = pygame.image.load("over.jpg")
    while not ex:
        if gameover == True:
            game.blit(bg2,(0,0))
            fontover = pygame.font.SysFont(None,105)
            fontover2 = pygame.font.SysFont(None,80)
            text = fontover2.render("Game over Enter to play this game", True, bl)
            game.blit(text, [120, 110])
            note = fontover.render("Score:"+str(score),True, blue)
            game.blit(note,[370,180])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        loop()
        else:
            score = len(snk_l) * 5
            game.blit(bg,(0,0))
            txt = font.render("Score:"+str(score), True, bl)
            game.blit(txt, [5, 5])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = 10
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -10
                        velocity_y = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = 10
                        velocity_x = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -10
                        velocity_x = 0
                    if event.key == pygame.K_RCTRL:
                        snk_le = snk_le + 5
                    if event.key == pygame.K_b:
                        h = 10
                        fps = 25
                    if event.key == pygame.K_LCTRL:
                        h = 30
                        fps = 30

            # Automation Code is here
            # Preventing game over
            eat_food_or_not = True
            if current_direction == 1:
                if (screen_width - x) < 20:
                    eat_food_or_not = False
                    # Searching that how many parts of the snake lie on that axis
                    search_result = search(1,snk_l)
                    maximum_turn = y > (screen_height / 2) # if true means down and if false means up
                    if len(search_result) == 0:
                        if maximum_turn:
                            velocity_x = 0
                            velocity_y = -10
                        else:
                            velocity_x = 0
                            velocity_y = 10
                    else:
                        # This var will decide which turn we have to choose
                        if maximum_turn and :
                            
                                       


            # Basic Work for eating food
            if eat_food_or_not:
                if f_x != x:
                    if f_x - x > 0 :
                        current_direction = 1 # East
                        velocity_x = 10
                        velocity_y = 0
                    else:
                        current_direction = 2 # West
                        velocity_x = -10
                        velocity_y = 0
                else:
                    if f_y - y > 0:
                        current_direction = 3 # North
                        velocity_y = 10
                        velocity_x = 0
                    else:
                        current_direction = 4 # South
                        velocity_y = -10
                        velocity_x = 0
                # Special Cases for eating food

            # Automation Code end here
            if abs(x - f_x)<15 and abs(y - f_y)<15:
                snk_le = snk_le + 5
                f_x = math.ceil(random.randint(20,1100) / 10) * 10
                f_y = math.ceil(random.randint(20,700) / 10) * 10
            if x<0 or y<0 or x>screen_width or y>screen_height:
                gameover = True
            head = []
            head.append(x)
            head.append(y)
            snk_l.append(head)
            if head in snk_l[:-2]:
                gameover = True
            plot()
            food = pygame.draw.rect(game, red, [f_x, f_y, h, h])
            x = x + velocity_x
            y = y + velocity_y
            if len(snk_l)>snk_le:
                del snk_l[0]
            clock.tick(fps)
            pygame.display.update()
loop()
pygame.quit()
quit()
