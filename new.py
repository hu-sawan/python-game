import pygame
import random

# set to keep track of used coordinates for boxes
boxes_coordinates = set()

# Initialize the game
pygame.init()

# Get user screen info
width, height = pygame.display.Info().current_w, pygame.display.Info().current_h

# Set the dimensions of the screen
screen = pygame.display.set_mode((width, height))

# Set the title of the game
pygame.display.set_caption("New Game")

# Set the background color of the screen
background = (0, 0, 0)

# Set the game loop
running = True
x, y, w, h = 50, 50, 50, 50
DIRECTION = 'RIGHT'

# generate a random number between 0 and height
gap = random.randint(0, width - w)

# checking if object is colliding:
def check_collision(obj1_x, obj1_y, obj1_w, obj1_h, obj2_x, obj2_y, obj2_w, obj2_h):
    # to check if bottom right corner of obj 1 cuts obj 2
    if(
        (obj1_y + obj1_h) > obj2_y 
        and 
        (obj1_y + obj1_h) < (obj2_y + obj2_h) 
        and 
        (obj1_x + obj1_w) > obj2_x
        and
        (obj1_x + obj1_w) < (obj2_x + obj2_w)
    ):
        return True    
    
    # to check if top right corner of obj 1 cuts obj 2
    if(
        obj1_y > obj2_y 
        and 
        obj1_y < (obj2_y + obj2_h)
        and 
        (obj1_x + obj1_w) > obj2_x
        and
        (obj1_x + obj1_w) < (obj2_x + obj2_w)
    ):
        return True
    
    # to check if bottom left corner of obj 1 cuts obj 2
    if(
        (obj1_y + obj1_h) > obj2_y 
        and 
        (obj1_y + obj1_h) < (obj2_y + obj2_h) 
        and 
        obj1_x > obj2_x
        and
        obj1_x < (obj2_x + obj2_w)
    ):
        return True
    
    # to check if top left corner of obj 1 cuts obj 2
    if(
        obj1_y > obj2_y 
        and 
        obj1_y  < (obj2_y + obj2_h) 
        and 
        obj1_x > obj2_x
        and
        obj1_x < (obj2_x + obj2_w)
    ):
        return True
    
    # CHECK IF OBJ2 CUTS OBJ1
    # to check if bottom right corner of obj 2 cuts obj 1
    if(
        (obj2_y + obj2_h) > obj1_y 
        and 
        (obj2_y + obj2_h) < (obj1_y + obj1_h) 
        and 
        (obj2_x + obj2_w) > obj1_x
        and
        (obj2_x + obj2_w) < (obj1_x + obj1_w)
    ):
        return True

    # to check if top right corner of obj 2 cuts obj 1
    if(
        obj2_y > obj1_y 
        and 
        obj2_y < (obj1_y + obj1_h)
        and 
        (obj2_x + obj2_w) > obj1_x
        and
        (obj2_x + obj2_w) < (obj1_x + obj1_w)
    ):
        return True
    
    # to check if bottom left corner of obj 2 cuts obj 1
    if(
        (obj2_y + obj2_h) > obj1_y 
        and 
        (obj2_y + obj2_h) < (obj1_y + obj1_h) 
        and 
        obj2_x > obj1_x
        and
        obj2_x < (obj1_x + obj1_w)
    ):
        return True
    
    # to check if top left corner of obj 1 cuts obj 2
    if(
        obj2_y > obj1_y 
        and 
        obj2_y  < (obj1_y + obj1_h) 
        and 
        obj2_x > obj1_x
        and
        obj2_x < (obj1_x + obj1_w)
    ):
        return True

# random coordinates generator
def get_random_coordinates(x = -1, y = -1):
    if x == -1:
        x = random.randint(50, width - 50)

    if y == -1:
        y = random.randint(50, height - 50)

    while True:
        if y < ((height // 2) - 30) or y > ((height // 2) + 30):
            break
        y = random.randint(50, height - 50)

    return (x, y)

# display game over screen
def game_over():
    font = pygame.font.Font(None, 36)
    text = font.render("GAME OVER", True, (255, 255, 255))
    text_rect = text.get_rect(center=(width // 2, height // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()

# keep track of current boxes
current_boxes_count = 0
BOX_x, BOX_y = None, None

# keep track of score
score = 0

def display_score():
    font = pygame.font.Font(None, 36)
    text = font.render("Score " + str(score), True, (0, 0, 255), (0, 0, 0))
    text_rect = text.get_rect(center=(45, 15))
    screen.blit(text, text_rect)
    pygame.display.flip()

def display_speed(speed):
    font = pygame.font.Font(None, 36)
    text = font.render("Speed " + str(speed), True, (0, 0, 255))
    text_rect = text.get_rect(center=(55, 45))
    screen.blit(text, text_rect)
    pygame.display.flip()

def calc_slope(ax, ay, bx, by):
    return (by - ay) / (bx - ax)

def calc_center_of_gravity(x, y):
    return (x, y)

targetX, targetY = -1, -1

current_flying_boxes_count = 0

flying_ball_X, flying_ball_Y = -1, -1
flying_line_X, flying_line_Y = -1, -1
flying_line_slope = None

GAP_MOVING_DIRECTION = 'RIGHT'

# Game loop
while running:
    LINE_HEIGHT, MAIN_OFFSET = 2, 200

    # when score increase the gap will shrink to make it harder
    MAIN_OFFSET = MAIN_OFFSET - score if (MAIN_OFFSET - score) >= 30 else 30

    # move the gap back and forth
    if GAP_MOVING_DIRECTION == 'RIGHT':
        gap += .5
    else:
        gap -= .5

    # change the direction when it reach bounderies
    if gap + (2 * MAIN_OFFSET) >= width:
        GAP_MOVING_DIRECTION = 'LEFT'

    if gap - MAIN_OFFSET <= 0:
        GAP_MOVING_DIRECTION = 'RIGHT'

    # Set the background color
    screen.fill(background)

    # draw a rectangle
    pygame.draw.rect(screen, (255, 255, 255), (x, y, w, h))

    # draw a circle
    pygame.draw.line(screen, (0, 0, 255), (0, height // 2), (gap - MAIN_OFFSET, height // 2), LINE_HEIGHT)
    pygame.draw.line(screen, (0, 0, 255), (gap + w + MAIN_OFFSET, height // 2), (width, height // 2), LINE_HEIGHT)

    if(
        check_collision(x, y, w, h, 0, height // 2, gap - MAIN_OFFSET, LINE_HEIGHT)
        or
        check_collision(x, y, w, h, gap + w + MAIN_OFFSET, height // 2, width - (gap + w + MAIN_OFFSET), LINE_HEIGHT)
    ):
        game_over()
        pygame.time.delay(1000)
        break
    
    # increase speed based on current score
    inc_speed = score * 0.05 if (score % 10) == 0 else inc_speed # increase speed by 5% of the cureent score

    # move the rectangle horizontally
    if DIRECTION == 'RIGHT':
        x += (1 + inc_speed)
    elif DIRECTION == 'LEFT':
        x -= (1 + inc_speed)

    if x >= (width - w):
        DIRECTION = 'LEFT'
    elif x <= 0:
        DIRECTION = 'RIGHT'

    # move the rectangle vertically
    if DIRECTION == 'DOWN':
        y += (1 + inc_speed)
    elif DIRECTION == 'UP':
        y -= (1 + inc_speed)

    if y >= (height - h):
        DIRECTION = 'UP'
    elif y <= 0:
        DIRECTION = 'DOWN'

    # generate box in random coordinates
    BOX_WIDTH, BOX_HEIGHT = 5, 5
    BOXES_COUNT = 50

    if current_boxes_count < BOXES_COUNT:
        while current_boxes_count < BOXES_COUNT:
            BOX_x, BOX_y = get_random_coordinates()
            if (BOX_x, BOX_y) not in boxes_coordinates:
                boxes_coordinates.add((BOX_x, BOX_y))
                current_boxes_count += 1

    if current_flying_boxes_count == 0:
        # getting a rand coordinates to shoot the flying box from
        flying_line_X, flying_line_Y = get_random_coordinates(width)
        flying_ball_X, flying_ball_Y = flying_line_X, flying_line_Y

        flying_line_slope = calc_slope(flying_ball_X, flying_ball_Y, x, y)
        current_flying_boxes_count += 1

    FLYING_BALL_SIZE = 20

    pygame.draw.rect(screen, (255, 0, 0), (flying_ball_X, flying_ball_Y, FLYING_BALL_SIZE, FLYING_BALL_SIZE), border_radius=50)

    if check_collision(x, y, w, h, flying_ball_X,  flying_ball_Y, FLYING_BALL_SIZE, FLYING_BALL_SIZE):
        game_over()
        break

    flying_ball_X -= 4
    flying_ball_Y = (flying_line_slope * (flying_ball_X - flying_line_X)) + flying_line_Y

    if flying_ball_X <= 0 or flying_ball_Y <= 0 or flying_ball_Y >= height:
        current_flying_boxes_count = 0

    for (BOX_x, BOX_y) in boxes_coordinates.copy():
        pygame.draw.rect(screen, (255, 255, 255), (BOX_x, BOX_y, BOX_WIDTH, BOX_HEIGHT))
        if check_collision(x, y, w, h, BOX_x, BOX_y, BOX_WIDTH, BOX_HEIGHT):
            boxes_coordinates.remove((BOX_x, BOX_y))
            current_boxes_count -= 1
            score += 1

    display_score()
    display_speed(1 + inc_speed)

    # decrease the speed of the game
    pygame.time.delay(3)

    # Set the game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                DIRECTION = "LEFT"
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                DIRECTION = "RIGHT"
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                DIRECTION = "UP"
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                DIRECTION = "DOWN"

    # Update the display
    pygame.display.flip()


# Quit the game
pygame.quit()