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
    current_axis = 0
    font = pygame.font.SysFont(None,55)
    # stoping from exiting
    def plot():
        for v_x,v_y in snk_l:
            pygame.draw.rect(game, bl, [v_x, v_y, h, h])
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
            if f_x != x:
                if f_x - x > 0 :
                    velocity_x = 10
                    velocity_y = 0
                else:
                    velocity_x = -10
                    velocity_y = 0
            else:
                if f_y - y > 0:
                    velocity_y = 10
                    velocity_x = 0
                else:
                    velocity_y = -10
                    velocity_x = 0

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
