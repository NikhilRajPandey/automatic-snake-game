import pygame
import random
import math

screen_width = 1200
screen_height = 800

def wall_collid(direction,snk_l):
    head = snk_l[-1]
    if direction == 1: # East
        if (screen_width - head[0])  <= 20: # Means it will collide with wall
            return True
    if direction == 2: # West
        if head[0]  <= 20:
            return True
    if direction == 3: # North
        if head[1] <= 20: # Pygame cartesian plane start upside down
            return True
    if direction == 4: # South
        if (screen_height - head[1])  <= 20:
            return True
    return False
def part_collid(direction,snk_l,food):
    head = snk_l[-1]
    snk_l = snk_l[:-1]
    can_collid_parts = []
    if direction == 1: # East
        for index,part in enumerate(snk_l):
            if part[1] == head[1] and part[0] > head[0]: # Adding those parts that can collid
                can_collid_parts.append([index,part])
        if can_collid_parts == []:
            return False # Means not any part will collid
        else:
            collid_parts_x = []
            collid_parts_x_index = []
            for item in can_collid_parts: # Sometimes a many parts lies in head path
                collid_parts_x.append(item[1][0])
                collid_parts_x_index.append(item[0])
            nearest_part = min(collid_parts_x)
            nearest_part_index = collid_parts_x_index[collid_parts_x.index(nearest_part)]
            if food[0] < nearest_part and food[1] == snk_l[nearest_part_index][1]: # Means I will eat the food before collidation
                return False
            return (((nearest_part - head[0]) / 10 ) - (nearest_part_index))
    elif direction == 2: # West
        for index,part in enumerate(snk_l):
            if part[1] == head[1] and part[0] < head[0]:
                can_collid_parts.append([index,part])
        if can_collid_parts == []:
            return False
        else:
            collid_parts_x = []
            collid_parts_x_index = [] # From Snk_l
            for item in can_collid_parts:
                collid_parts_x.append(item[1][0])
                collid_parts_x_index.append(item[0])
            nearest_part = max(collid_parts_x)
            nearest_part_index = collid_parts_x_index[collid_parts_x.index(nearest_part)]
            if food[0] > nearest_part and food[1] == snk_l[nearest_part_index][1]:
                return False
            return (((head[0] - nearest_part) / 10 ) - (nearest_part_index))
    elif direction == 3: # North
        for index,part in enumerate(snk_l):
            if part[0] == head[0] and part[1] < head[1]:
                can_collid_parts.append([index,part])
        if can_collid_parts == []:
            return False
        else:
            collid_parts_y = []
            collid_parts_y_index = []
            for item in can_collid_parts:
                collid_parts_y.append(item[1][1])
                collid_parts_y_index.append(item[0])
            nearest_part = max(collid_parts_y)
            nearest_part_index = collid_parts_y_index[collid_parts_y.index(nearest_part)]
            if food[1] > nearest_part and food[0] == snk_l[nearest_part_index][0]:
                return False
            return (((head[1] - nearest_part) / 10 ) - (nearest_part_index))
    elif direction == 4: # South
        for index,part in enumerate(snk_l):
            if part[0] == head[0] and part[1] > head[1]:
                can_collid_parts.append([index,part])
        if can_collid_parts == []:
            return False
        else:
            collid_parts_y = []
            collid_parts_y_index = []
            for item in can_collid_parts:
                collid_parts_y.append(item[1][1])
                collid_parts_y_index.append(item[0])
            nearest_part = min(collid_parts_y)
            nearest_part_index = collid_parts_y_index[collid_parts_y.index(nearest_part)]
            if food[1] < nearest_part and food[0] == snk_l[nearest_part_index][0]:
                return False
            return (((nearest_part - head[1]) / 10 ) - (nearest_part_index))
            # This will return at which moment it will collide because the part is also moving

def will_it_collid(direction,snk_l,food):
    part_coll = part_collid(direction,snk_l,food)
    wall_coll = wall_collid(direction,snk_l)
    if part_coll is not False:
        part_coll = int(part_coll)
        if part_coll < 2: # Here i write two it means i have to maintain at least 10 pixel distance
            part_coll = True
        else:
            part_coll = False
    if not part_coll and not wall_coll:
        return False
    else:
        return True
    

# main game
def loop():
    def plot():
        for v_x,v_y in snk_l:
            pygame.draw.rect(game, bl, [v_x, v_y, h, h])
    pygame.init()
    game =  pygame.display.set_mode((screen_width,screen_height))
    ex = False
    gameover = False
    # colors
    white = (255,255,255)
    bl = (25,50,100)
    red = (255,0,0)
    blue = (51, 51, 255)
    # specific variables
    x = 40
    y = 50
    h = 30
    f_x = math.ceil(random.randint(20,1100) / 10) * 10
    f_y = math.ceil(random.randint(20,700) / 10) * 10
    velocity_x = 10
    velocity_y = 0
    snk_l = []
    fps = 45
    clock = pygame.time.Clock()
    snk_le = 1
    current_direction = 1
    font = pygame.font.SysFont(None,55)
    bg = pygame.image.load("back.jpg")
    bg2 = pygame.image.load("over.jpg")
    # stoping from exiting
    while not ex:
        if gameover == True:
            game.blit(bg2,(0,0))
            fontover = pygame.font.SysFont(None,105)
            fontover2 = pygame.font.SysFont(None,80)
            text = fontover2.render("Game over Enter to play this game", True, bl)
            game.blit(text, [120, 110])
            score = len(snk_l) * 5
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
            food = [f_x,f_y]
            game.blit(bg,(0,0))
            pygame.draw.rect(game, red, [f_x, f_y, h, h])
            txt = font.render("Score:"+str(score), True, bl)
            game.blit(txt, [5, 5])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            head = []
            head.append(x)
            head.append(y)
            snk_l.append(head)
            plot()
            # Automation Code Start Here
            def work_when_collid(current_direction,snk_l,food):
                checking_collidation = will_it_collid(current_direction,snk_l,food)
                direction = current_direction
                if checking_collidation:
                    if current_direction == 1 or current_direction == 2: # West and East
                        if not will_it_collid(3,snk_l,food): # These lines are for taking turns if something come in snake way
                            direction = 3
                            velocity_y = -10
                            velocity_x = 0
                        else:
                            direction = 4
                            velocity_y = 10
                            velocity_x = 0

                    if current_direction == 3 or current_direction == 4: # North
                        if not will_it_collid(1,snk_l,food):
                            direction = 1 # East
                            velocity_x = 10
                            velocity_y = 0
                        else:
                            direction = 2 # West
                            velocity_x = -10
                            velocity_y = 0
                    return [direction,velocity_x,velocity_y]
                else:
                    return False # Means I have to do nothing

            # Basic Work for eating food
            focus_on_y_axis = False
            if f_x != x or f_y == y:
                # Think if this is not writen then it will collid in himself
                if f_x - x > 0 and current_direction == 2: 
                    focus_on_y_axis = True
                elif f_x - x < 0 and current_direction == 1:
                    focus_on_y_axis = True
                elif f_x == x:
                    focus_on_y_axis = True
                if not focus_on_y_axis:
                    if f_x - x > 0 :
                        direction_check = will_it_collid(1,snk_l,food)
                        if current_direction != 1 and not direction_check:
                            current_direction = 1 # East
                            velocity_x = 10
                            velocity_y = 0
                        else:
                            motion_vars = work_when_collid(current_direction,snk_l,food)
                            if motion_vars != False:
                                current_direction = motion_vars[0]
                                velocity_x = motion_vars[1]
                                velocity_y = motion_vars[2]
                    else:
                        direction_check = will_it_collid(2,snk_l,food)
                        if current_direction != 2 and not direction_check:
                            current_direction = 2 # West
                            velocity_x = -10
                            velocity_y = 0
                        else:
                            motion_vars = work_when_collid(current_direction,snk_l,food)
                            # If False Then i have to do nothing
                            if motion_vars != False:
                                current_direction = motion_vars[0]
                                velocity_x = motion_vars[1]
                                velocity_y = motion_vars[2]
            if focus_on_y_axis or f_x == x:
                if f_y - y > 0:
                    direction_check = will_it_collid(4,snk_l,food)
                    if current_direction != 4 and not direction_check:
                        current_direction = 4 # South
                        velocity_y = 10
                        velocity_x = 0
                    else:
                        motion_vars = work_when_collid(current_direction,snk_l,food)
                        if motion_vars != False:
                            current_direction = motion_vars[0]
                            velocity_x = motion_vars[1]
                            velocity_y = motion_vars[2]
                else:
                    direction_check = will_it_collid(3,snk_l,food)
                    if current_direction != 3 and not direction_check:
                        current_direction = 3 # North
                        velocity_y = -10
                        velocity_x = 0
                    else:
                        motion_vars = work_when_collid(current_direction,snk_l,food)
                        if motion_vars != False:
                            current_direction = motion_vars[0]
                            velocity_x = motion_vars[1]
                            velocity_y = motion_vars[2]
            if len(snk_l)>snk_le:
                del snk_l[0]
                
            if abs(x - f_x)<15 and abs(y - f_y)<15:
                snk_le = snk_le + 5
                # mouse_button_clicked = False
                f_x = math.ceil(random.randint(20,1100) / 10) * 10
                f_y = math.ceil(random.randint(20,700) / 10) * 10
                # For Debuging Purpose
                # while not mouse_button_clicked:
                #     for event in pygame.event.get():
                #         if event.type == pygame.MOUSEBUTTONDOWN:
                #             posx,posy = pygame.mouse.get_pos()
                #             f_x = math.ceil(posx / 10) * 10
                #             f_y = math.ceil(posy / 10) * 10
                #             mouse_button_clicked = True
            if x<0 or y<0 or x>screen_width or y>screen_height:
                gameover = True
            if head in snk_l[:-2]:
                print("Due to head collidation")
                gameover = True
            x = x + velocity_x
            y = y + velocity_y
            clock.tick(fps)
            pygame.display.update()
loop()
pygame.quit()
quit()
