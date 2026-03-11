import pygame
import random
# import sys
import asyncio

pygame.init()

def draw_glow_text(text, font, base_color, glow_color, x, y):
    for i in range(1,3):
        glow_text = font.render(text, True, glow_color)
        screen.blit(glow_text, (x-i, y-i))
        screen.blit(glow_text, (x+i, y+i))
    
    main_text = font.render(text, True, base_color)
    screen.blit(main_text, (x, y))

WIDTH = 1000
HEIGHT = 600

mid_width = WIDTH//2
mid_height = HEIGHT//2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Racing Game")

clock = pygame.time.Clock()
 
class Cantrols() :
    start_button = pygame.Rect(WIDTH//2 - 100, 250, 200, 60)
    quit_button = pygame.Rect(WIDTH//2 - 100, 330, 200, 60)
    easy_button = pygame.Rect(WIDTH//2 - 100, 220, 200, 60)
    medium_button = pygame.Rect(WIDTH//2 - 100, 300, 200, 60)
    hard_button = pygame.Rect(WIDTH//2 - 100, 380, 200, 60)
    back_button = pygame.Rect(WIDTH - 250, HEIGHT - 100, 200, 60)
    pause_button = pygame.Rect(WIDTH - 150, 50, 100, 30)
    resume_button = pygame.Rect(mid_width - 90, mid_height - 60, 180, 52)
    restart_button = pygame.Rect(mid_width - 90, mid_height ,180, 52)
    back2_button = pygame.Rect(mid_width - 90, mid_height + 60, 180, 52)
    restart2_button = pygame.Rect(mid_width - 210 , mid_height - 60,190, 52)
    back3_button = pygame.Rect(mid_width + 20, mid_height - 60 , 190, 52)
    left_button  = pygame.Rect(mid_width + 310, mid_height + 141, 60, 40)
    right_button = pygame.Rect(mid_width + 412, mid_height + 141, 60, 40)
    up_button    = pygame.Rect(mid_width + 371, mid_height + 80, 40, 60)
    down_button  = pygame.Rect(mid_width + 371, mid_height + 182, 40, 60)
    nitro_button  = pygame.Rect(mid_width - 430, mid_height + 140, 80, 80)
btt = Cantrols()
 
class Load_files():

    enemy_cars = [
        pygame.image.load("assets/enemy_car3.png").convert_alpha(),
        pygame.image.load("assets/enemy_car.png").convert_alpha(),
        pygame.image.load("assets/enemy_car4.png").convert_alpha(),
        pygame.image.load("assets/enemy_car6.png").convert_alpha(),
        pygame.image.load("assets/enemy_car7.png").convert_alpha()  
    ]
    
    player_car_image = pygame.image.load("assets/player_car.png").convert_alpha() 

    play_back = pygame.image.load("assets/play_back.png")
    up_side = pygame.image.load("assets/up_side.png")
    lr_side = pygame.image.load("assets/lr_side.png")
    tital = pygame.image.load("assets/start_alt.png") 
    scl_img = pygame.image.load("assets/scl_back.png")
    button_img = pygame.image.load("assets/start_quite.png") 
    button0_img = pygame.image.load("assets/pause.png")
    button1_img = pygame.image.load("assets/_re_re_back.png")
    button2_img = pygame.image.load("assets/_re_back.png")
    up = pygame.image.load("assets/up.png")
    down = pygame.image.load("assets/down.png")
    left = pygame.image.load("assets/left.png")
    right = pygame.image.load("assets/right.png")
    nitro_btt= pygame.image.load("assets/nitro.png")
    coin_img = pygame.image.load("assets/coin.png")
    green_flame = pygame.image.load("assets/green_flame.png")
    score_back = pygame.image.load("assets/score_back.png")
UI = Load_files()

class data_base():
    running = True
    game_state = "start"
    # basic data
    base = (160, 82, 45)
    grain = (120, 60, 30)
    paused = False
    countdown_time = 3
    countdown_active = False
    # for initilization
    level = 1
    high_level = 1
    score = 0
    high_score = 0
    coin = 0
    total_coins = 0
    tilt_angle = 0
    line_y = 0
    side_Line_width = 5
    left_side_space = 220
    right_side_space = 780
    explosion_timer = 0
    lanes = [240,335,435,535,635,720]
    # speeds 
    normal_speed = 5
    medium_speed = 7
    hard_speed = 9
    enemy_speed= normal_speed
    coin_speed = normal_speed
    powerup_speed = normal_speed
    nitro_speed = 12
    # nitro
    nitro = 100
    max_nitro = 100 
    nitro_active = False
    # coins 
    coins = []
    no_coin_drop = 6
    # powerup shield
    powerup_respawn_timer = 0
    shield_timer = 0 
    shield_active = False
    powerup_active = True
    powerup_y_range = (-600,-200)
    powerup_x = random.choice(lanes)
    powerup_y = random.randint( powerup_y_range[0],powerup_y_range[1] )
    # Player car details
    player_width = 50
    player_height = 90
    player_speed = 5
    player_x = WIDTH // 2
    player_y = HEIGHT - 100
    # image\\enemy car details
    MIN_DISTANCE = 200
    enemy_width = 50
    enemy_height = 90
    enemies = []
    no_enemy_car = 6

    for i in range(no_coin_drop):
        coins.append([ random.choice(lanes), random.randint(-1200, -300) ])

    for i in range(no_enemy_car):
        lane = lanes[i % len(lanes)]
        y = -i * MIN_DISTANCE
        image = random.choice(UI.enemy_cars)   
        enemies.append([lane, y ,image])    
data = data_base()

# all fonts
font1 = pygame.font.SysFont(None, 80) 
font2 = pygame.font.SysFont(None, 40)
font3 = pygame.font.SysFont(None, 200)
font4 = pygame.font.SysFont(None, 25)
font5 = pygame.font.SysFont(None, 36)
font6 = pygame.font.SysFont(None, 60)
font7 = pygame.font.SysFont(None, 70)
font8 = pygame.font.SysFont(None, 120)
font9 = pygame.font.SysFont(None, 50)

# function for reset data
def data_reset():   
     
    data.score = 0
    data.level = 1
    data.explosion_timer = 600
    data.nitro = 100
    data.player_x = WIDTH // 2
    data.player_y = HEIGHT - 100
    # Reset enemies start location
    data.enemies = []
    for i in range(data.no_enemy_car):
        lane = data.lanes[i % len(data.lanes)]
        y = -i * data.MIN_DISTANCE
        image = random.choice(UI.enemy_cars)   
        data.enemies.append([lane, y ,image])
    # reset powerup & shield
    data.shield_timer = 0 
    data.shield_active = False  
    data.powerup_active = True
    data.powerup_x = random.choice(data.lanes)
    data.powerup_y = random.randint(data.powerup_y_range[0],data.powerup_y_range[1])
    # reset coins location
    data.coin = 0
    data.coins = []
    for i in range(data.no_coin_drop):
        data.coins.append([ random.choice(data.lanes), random.randint(-1200, -300) ])
 
async def main():

    while data.running:
        dt = clock.tick(60) / 1000   # 60 FPS
        # print(clock.get_fps())
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                data.running = False
            # key for start
            if event.type == pygame.MOUSEBUTTONDOWN:
                if data.game_state == "start":
                    if btt.start_button.collidepoint(event.pos):
                        data.game_state = "menu"
                    elif btt.quit_button.collidepoint(event.pos):
                        data.running = False

                elif data.game_state == "menu" :
                    if btt.easy_button.collidepoint(event.pos) :
                        data.enemy_speed = data.normal_speed
                        data.game_state = "countdown"
                        data.countdown_time = 3
                    if btt.medium_button.collidepoint(event.pos) :
                        data.enemy_speed = data.medium_speed
                        data.game_state = "countdown"
                        data.countdown_time = 3
                    if btt.hard_button.collidepoint(event.pos) :
                        data.enemy_speed = data.hard_speed
                        data.game_state = "countdown"
                        data.countdown_time = 3
                    if btt.back_button.collidepoint(event.pos) :
                        data.game_state = "start"
                                            
                elif data.game_state == "play" :
                    if btt.left_button.collidepoint(event.pos):
                        data.player_x -= data.player_speed
                        data.tilt_angle = 8
                    if btt.right_button.collidepoint(event.pos):
                        data.player_x += data.player_speed
                        data.tilt_angle = -8
                    if btt.up_button.collidepoint(event.pos):
                        data.player_y -= data.player_speed
                    if btt.down_button.collidepoint(event.pos):
                        data.player_y += data.player_speed
                    if btt.nitro_button.collidepoint(event.pos) and data.nitro > 0:
                        data.nitro_active = True

                    if not data.paused:
                        if btt.pause_button.collidepoint(event.pos):
                            data.paused = True

                    else :
                        if btt.resume_button.collidepoint(event.pos):
                            data.paused = False
                        elif btt.restart_button.collidepoint(event.pos):
                            data_reset()
                            data.paused = False
                            data.game_state = "play"
                        elif btt.back2_button.collidepoint(event.pos):
                            data_reset()
                            data.paused = False
                            data.game_state = "menu"

                elif data.game_state == "explode" :
                    if btt.restart2_button.collidepoint(event.pos):
                        data_reset()
                        data.game_state = "play"
                    elif btt.back3_button.collidepoint(event.pos):
                        data_reset()
                        data.game_state = "menu"
        
        if data.game_state == "playing":
            # normal game movement
            data.player_y += data.player_speed
            enemy_y += data.enemy_speed

        elif data.game_state == "start":

            screen.fill(data.base)
            for y in range(0, HEIGHT, 40):
                pygame.draw.rect(screen, data.grain, (0, y, WIDTH, 20))
            
            screen.blit(UI.lr_side,(0,0))
            screen.blit(UI.lr_side,(980,0))
            screen.blit(UI.up_side,(0,0))
            screen.blit(UI.up_side,(0,580))

            screen.blit(UI.tital, (160,130)) 
            draw_glow_text("ULTIMATE RACER", font1, (255,0,0), (255,100,100), 240, 150)

            screen.blit(UI.button_img, btt.start_button)
            screen.blit(font2.render("START", True, (255,0,0)), (btt.start_button.x + 55, btt.start_button.y + 15))
            screen.blit(UI.button_img, btt.quit_button)
            screen.blit(font2.render("QUIT", True, (255,0,0)), (btt.quit_button.x + 65, btt.quit_button.y + 15))

        elif data.game_state == "menu":
            
            screen.fill(data.base)
            for y in range(0, HEIGHT, 40):
                pygame.draw.rect(screen, data.grain, (0, y, WIDTH, 20))

            screen.blit(UI.lr_side,(0,0))
            screen.blit(UI.lr_side,(980,0))
            screen.blit(UI.up_side,(0,0))
            screen.blit(UI.up_side,(0,580))

            screen.blit(UI.button_img, btt.easy_button)
            screen.blit(font2.render("EASY", True, (255,0,0)), (btt.easy_button.x + 60, btt.easy_button.y + 15))
            screen.blit(UI.button_img, btt.medium_button)
            screen.blit(font2.render("MEDIUM", True, (255,0,0)), (btt.medium_button.x + 45, btt.medium_button.y + 15))
            screen.blit(UI.button_img, btt.hard_button)
            screen.blit(font2.render("HARD", True, (255,0,0)), (btt.hard_button.x + 65, btt.hard_button.y + 15))
            screen.blit(UI.button_img, btt.back_button)
            screen.blit(font2.render("BACK", True, (255,0,0)), (btt.back_button.x + 65, btt.back_button.y + 15))

            screen.blit(UI.scl_img,(50,50))

            if data.high_score == "" :
                high_score_text = font2.render(f"High Score : 0", True, (255,0,0))
            else :
                high_score_text = font2.render(f"High Score : {int(data.high_score)}", True, (255,0,0))
            screen.blit(high_score_text, (90,105))
    
            if data.high_level == "" :
                high_level_text = font2.render(f"High level : 1", True, (255, 0,0))
            else :
                high_level_text = font2.render(f"High level : {data.high_level}", True, (255,0,0))
            screen.blit(high_level_text, (90,140))
    
            if data.total_coins == "" :
                total_coin_text = font2.render(f"Total Coins : 0", True, (255,0,0))
            else :
                total_coin_text = font2.render(f"Total Coins : {data.total_coins}", True, (255,0,0))
            screen.blit(total_coin_text, (90,70))
            
        elif data.game_state == "countdown":

            screen.fill(data.base)

            for y in range(0, HEIGHT, 40):
                pygame.draw.rect(screen, data.grain, (0, y, WIDTH, 20))

            screen.blit(UI.lr_side,(0,0))
            screen.blit(UI.lr_side,(980,0))
            screen.blit(UI.up_side,(0,0))
            screen.blit(UI.up_side,(0,580))

            data.countdown_time -= dt
            if data.countdown_time > 2:
                text = "3"
            elif data.countdown_time > 1:
                text = "2"
            elif data.countdown_time > 0:
                text = "1"
            else:
                text = "GO!"
            countdown_text = font3.render(text, True, (255,255,0))
            countdown_rect = countdown_text.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(countdown_text, countdown_rect) 

            if data.countdown_time <= -0.5:
                data.game_state = "play"

        elif data.game_state == "play":
            
            keys = pygame.key.get_pressed()

            # ------------------ UPDATE OR PAUSE SECTION ------------------
            if not data.paused: 
                # press to hold button
                mouse_pressed = pygame.mouse.get_pressed()
                mouse_pos = pygame.mouse.get_pos()
                
                nitro_button_pressed = (mouse_pressed[0] and btt.nitro_button.collidepoint(mouse_pos))
                nitro_key_pressed = keys[pygame.K_LSHIFT]

                if mouse_pressed[0]:   # finger held down
                    if btt.left_button.collidepoint(mouse_pos):
                        data.player_x -= data.player_speed
                        data.tilt_angle = 8
                    if btt.right_button.collidepoint(mouse_pos):
                        data.player_x += data.player_speed
                        data.tilt_angle = -8
                    if btt.up_button.collidepoint(mouse_pos):
                        data.player_y -= data.player_speed
                    if btt.down_button.collidepoint(mouse_pos):
                        data.player_y += data.player_speed
                # ---------- NITRO ----------
                if (nitro_button_pressed or nitro_key_pressed) and data.nitro > 0:
                    data.nitro_active = True
                    data.player_speed = data.nitro_speed
                    data.nitro -= 1 * dt
                else:
                    data.nitro_active = False
                    data.player_speed = 5
                    if data.nitro < data.max_nitro:
                        data.nitro += 0.5 * dt
                # ---------- PLAYER MOVEMENT ----------
                data.tilt_angle = 0   # reset every frame

                if keys[pygame.K_LEFT] :
                    data.player_x -= data.player_speed
                    data.tilt_angle = 8                   # tilt right visually

                if keys[pygame.K_RIGHT]: 
                    data.player_x += data.player_speed
                    data.tilt_angle = -8                 # tilt left visually
                    
                if keys[pygame.K_UP] :
                    data.player_y -= data.player_speed

                if keys[pygame.K_DOWN] :
                    data.player_y += data.player_speed
                # Boundaries       
                data.player_x = max(data.left_side_space, data.player_x)
                data.player_x = min(data.right_side_space - data.player_width - data.side_Line_width, data.player_x)
                
                data.player_y = max(20, data.player_y)
                data.player_y = min(500, data.player_y)          
                # ---------- image\\ENEMY MOVEMENT ----------
                for enemy in data.enemies:
                    enemy[1] += data.enemy_speed + (data.level * 0.5)

                    if enemy[1] > HEIGHT:
                        new_lane = random.choice(data.lanes)
                        # Check other enemies already in that lane
                        lane_enemies = [e for e in data.enemies if e[0] == new_lane and e != enemy]
                        if lane_enemies:
                            highest = min(e[1] for e in lane_enemies)
                            spawn_y = min(highest - data.MIN_DISTANCE, -data.MIN_DISTANCE)
                        else:
                            spawn_y = -data.MIN_DISTANCE
                        enemy[0] = new_lane
                        enemy[1] = spawn_y
                
                
                # ---------- COIN MOVEMENT ----------
                data.coin_speed = data.enemy_speed + (data.level * 0.3)
                for coin_axis in data.coins:
                    coin_axis[1] += data.coin_speed

                    if coin_axis[1] > HEIGHT:
                        coin_axis[0] =  random.choice(data.lanes)       # x axis
                        coin_axis[1] = random.randint(-1200, -300)  # y axis
                # ---------- POWERUP MOVEMENT ----------
                if data.powerup_active:
                    data.powerup_speed = data.enemy_speed + (data.level * 0.3)
                    data.powerup_y += data.powerup_speed

                    if data.powerup_y > HEIGHT:
                        data.powerup_x = random.choice(data.lanes)
                        data.powerup_y = random.randint( data.powerup_y_range[0],data.powerup_y_range[1])
                # ---------- SHIELD TIMER ----------
                if data.shield_active:
                    data.shield_timer -= dt       
                    if data.shield_timer <= 0:
                        data.shield_active = False
                # ---------- SCORE SYSTEM ----------
                if data.nitro_active:
                    data.score += 20 * dt
                else:
                    data.score += 10 * dt

                data.level = int(data.score // 300) + 1
                # ---------- COLLISION ----------
                player_rect = pygame.Rect(data.player_x,data.player_y,data.player_width - 10,data.player_height - 20)
                # Enemy collision
                for enemy in data.enemies:
                    enemy_rect = pygame.Rect(enemy[0], enemy[1],data.enemy_width - 10,data.enemy_height - 20)
                    if player_rect.colliderect(enemy_rect):
                        if not data.shield_active:
                            data.game_state = "explode"
                            data.explosion_timer = 600
                # Coin collision
                for coin_axis in data.coins:
                    coin_rect = pygame.Rect(coin_axis[0], coin_axis[1], 45, 45)

                    if player_rect.colliderect(coin_rect):
                        data.coin += 5   # fixed reward
                        data.total_coins += 5

                        coin_axis[0] = random.choice(data.lanes) 
                        coin_axis[1] = random.randint(-1200, -300)
                # Powerup collision
                if data.powerup_active:
                    powerup_rect = pygame.Rect(data.powerup_x-10, data.powerup_y-10, 40, 40)
                    if player_rect.colliderect(powerup_rect) :
                        data.shield_active = True
                        data.shield_timer = 5   # 5 seconds at 60 FPS
                        data.powerup_active = False
                        data.powerup_respawn_timer = random.randint(10,20)   # wait 10 seconds before respawn     
                # Powerup respawn
                if not data.powerup_active:
                    data.powerup_respawn_timer -= dt
                    if data.powerup_respawn_timer <= 0:
                        data.powerup_active = True
                        data.powerup_x = random.choice(data.lanes)
                        data.powerup_y = random.randint(data.powerup_y_range[0],data.powerup_y_range[1])

                # Middle line
                data.line_y += data.enemy_speed
                if data.line_y > HEIGHT:
                    data.line_y = 0
                
            # ------------------ DRAW SECTION ------------------
            screen.blit(UI.play_back,(0,0))    # green grass
            # # pause button
            screen.blit(UI.button0_img,btt.pause_button)
            screen.blit(font4.render("PAUSE", True, (255,255,255)), (btt.pause_button.x + 13, btt.pause_button.y + 6))
            # Road
            pygame.draw.rect(screen, (50,50,50), (data.left_side_space , 0 ,  WIDTH-440 , HEIGHT)) 


            # Middle line
            for i in range(-600,HEIGHT,200):
                pygame.draw.rect(screen, (255,255,255), (WIDTH//2 - 5, i + data.line_y, 10,50))

            # Side White line
            pygame.draw.line(screen, (255, 255, 255), (data.left_side_space, 0), (data.left_side_space, HEIGHT), data.side_Line_width)
            pygame.draw.line(screen, (255, 255, 255), (data.right_side_space, 0), (data.right_side_space, HEIGHT), data.side_Line_width)

            # Nitro bar 
            pygame.draw.rect(screen, (255,255,255), (30,200,20,200), 2)                                                        
            bar_height = int((data.nitro / data.max_nitro) * 200)         
            
            if data.nitro < data.max_nitro * 0.2:
                nitro_color = (255, 140, 0)    
            else:
                nitro_color = (0,255,255)    # Cyan
            pygame.draw.rect(screen,nitro_color,(30, 200 + (200 - bar_height), 20, bar_height))

            # Draw coins
            for coin_axis in data.coins:
                screen.blit(UI.coin_img, (coin_axis[0] + 25 , coin_axis[1] + 45))

            # Daraw powerup
            if data.powerup_active:
                screen.blit(UI.green_flame,(data.powerup_x + 15, data.powerup_y + 45))

            # Draw Enemies
            for enemy in data.enemies:
                screen.blit(enemy[2], (enemy[0] ,enemy[1] ))  

            # Draw Player
            rotated_car = pygame.transform.rotate(UI.player_car_image, data.tilt_angle)
            new_rect = rotated_car.get_rect(center=(data.player_x + data.player_width//2, data.player_y + data.player_height//2))
            screen.blit(rotated_car, new_rect.topleft)
                
            # Shield glow
            if data.shield_active:
                pygame.draw.circle(screen,(0, 255, 255),(data.player_x + data.player_width//2 - 5, data.player_y + data.player_height//2),46,3)

            # Score & Level & coin
            screen.blit(font5.render("Level: " + str(int(data.level)), True, (255, 255, 255)), (20,46))
            screen.blit(font5.render("Coins: " + str(int(data.coin)), True, (255, 255, 255)), (20,69))
            screen.blit(font5.render("Score: " + str(int(data.score)), True, (255, 255, 255)), (20,23))

            # Draw control buttons
            screen.blit(UI.up,btt.up_button)
            screen.blit(UI.down,btt.down_button)
            screen.blit(UI.left,btt.left_button)
            screen.blit(UI.right,btt.right_button)
            screen.blit(UI.nitro_btt,btt.nitro_button)

            # ------------------ PAUSE OVERLAY ------------------
            if data.paused:
               
                pygame.draw.rect(screen,(160, 82, 45),(mid_width - 104,mid_height - 126,214,250))
                pygame.draw.rect(screen,(255,255,255),(mid_width - 108,mid_height - 130,222,258),4)

                screen.blit(font6.render("PAUSED", True, (255,255,255)), ( mid_width - 85,mid_height - 115))

                # button
                screen.blit(UI.button1_img, btt.resume_button)
                screen.blit(UI.button1_img, btt.restart_button)
                screen.blit(UI.button1_img, btt.back2_button)
                screen.blit(font2.render("RESUME", True, (255,255,255)), (btt.resume_button.x + 30, btt.resume_button.y + 13))
                screen.blit(font2.render("RESTART", True, (255,255,255)), (btt.restart_button.x + 25, btt.restart_button.y + 13))
                screen.blit(font2.render("EXIT", True, (255,255,255)), (btt.back2_button.x + 50, btt.back2_button.y + 13))
                
        elif data.game_state == "explode":
            # ------------------ Explode OVERLAY ------------------
            data.explosion_timer -= 1
 

            # # Grow rectangl
            overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
            overlay.fill((150,150,150, 5))
            screen.blit(overlay, (0, 0))

            pygame.draw.rect(screen,(255,255,255),(mid_width - 250,mid_height - 150,500,300),5)
            pygame.draw.rect(screen,(160, 82, 45),(mid_width - 245,mid_height - 145,490,290))

            screen.blit(font7.render("     GAME OVER    ", True, (255,255,255)), ( mid_width - 220,mid_height - 130))
        
            screen.blit(UI.button2_img,btt.restart2_button)
            screen.blit(UI.button2_img,btt.back3_button)
            screen.blit(font2.render("RESTART", True, (255,255,255)), (btt.restart2_button.x + 25, btt.restart2_button.y + 12))

            screen.blit(font9.render("EXIT", True, (255,255,255)), (btt.back3_button.x + 50, btt.back3_button.y + 12))
            # score
            screen.blit(UI.score_back,(mid_width - 200,mid_height + 10))
            screen.blit(font2.render(f"Score : {int(data.score)}", True, (255,255,255)), (mid_width - 60 , mid_height + 15))
            # # Countdown
            seconds_left = max(0, data.explosion_timer // 60) 
            screen.blit(font8.render(f"{seconds_left}", True, (255,0,0)), (mid_width - 15 , mid_height + 55 ))

            if data.explosion_timer <= 1:
                data_reset()  
                data.game_state = "menu"
            
        pygame.display.update()
        await asyncio.sleep(0)
    pygame.quit()

asyncio.run(main())
