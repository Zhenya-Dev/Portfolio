import pygame
import sys
import random

SIZE_BLOKS = 20
FRAME_COLOR = [0, 255, 204]
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
RED = (224, 0, 0)
HEADER_COLOR = (0, 204, 153)
SNAKE_COLOR = (0, 102, 0)
COUNT_BLOCKS = 20
HEADER_MARGIN = 70
MARGIN = 1

size = [SIZE_BLOKS * COUNT_BLOCKS + 2 * SIZE_BLOKS + MARGIN * COUNT_BLOCKS,
        SIZE_BLOKS * COUNT_BLOCKS + 2 * SIZE_BLOKS + MARGIN * COUNT_BLOCKS + HEADER_MARGIN]

print(size)
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Snake_Game')
timer = pygame.time.Clock()

apple_eat = pygame.mixer.Sound('sound/poedanie-ukus-yabloka.wav')
game_over_sound = pygame.mixer.Sound('sound/zvuk-game-over-4158.wav')

font = pygame.font.SysFont(None, 48)

apple_img = pygame.image.load('img/apple.png')
apple_img = pygame.transform.scale(apple_img,(SIZE_BLOKS*2, SIZE_BLOKS*2))

def snake_block(x,y):
    return [x,y]

def is_inside(head):
    return 0 <= head[0] < SIZE_BLOKS and 0 <= head[1] < SIZE_BLOKS

def get_random_block():
    x = random.randint(0, COUNT_BLOCKS - 1)
    y = random.randint(0, COUNT_BLOCKS - 1)
    empty_block = snake_block(x, y)
    while empty_block in snake_blocks:
        empty_block[0] = random.randint(0, COUNT_BLOCKS - 1)
        empty_block[1] = random.randint(0, COUNT_BLOCKS - 1)
    return empty_block

def draw_block(color, row, column, what):
    if what == 'block':
        pygame.draw.rect(screen, color, [SIZE_BLOKS + column * SIZE_BLOKS + MARGIN * (column + 1),
                                     HEADER_MARGIN + SIZE_BLOKS + row * SIZE_BLOKS + MARGIN * (row + 1),
                                     SIZE_BLOKS, SIZE_BLOKS])
    else:
        screen.blit(apple_img, [SIZE_BLOKS + column * SIZE_BLOKS + MARGIN * (column + 1) - SIZE_BLOKS * 0.5,
                            HEADER_MARGIN + SIZE_BLOKS + row * SIZE_BLOKS + MARGIN * (row + 1) - SIZE_BLOKS * 0.5])


snake_blocks = [snake_block(9, 8),snake_block(9, 9), snake_block(9, 10)]
apple = get_random_block()

d_row = 0
d_col = 1
total = 0
speed = 1

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('exit')
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and d_col != 0:
                d_row = -1
                d_col = 0
            elif event.key == pygame.K_DOWN and d_col != 0:
                d_row = 1
                d_col = 0
            elif event.key == pygame.K_LEFT and d_row != 0:
                d_row = 0
                d_col = -1
            elif event.key == pygame.K_RIGHT and d_row != 0:
                d_row = 0
                d_col = 1


    screen.fill(FRAME_COLOR)
    pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

    text_t = "Total: " + str(total)
    text_s = "Speed: " + str(speed)
    text_total = font.render(text_t, True, WHITE)
    text_speed = font.render(text_s, True, WHITE)
    screen.blit(text_total, (SIZE_BLOKS, SIZE_BLOKS))
    screen.blit(text_speed, (SIZE_BLOKS + 230, SIZE_BLOKS))

    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column) % 2 == 0:
                color = BLUE
            else:
                color = WHITE
            draw_block(color, row, column,'block')

    head = snake_blocks[-1]

    if head in snake_blocks[:-1]:
        #print("YYYPPS")
        pygame.quit()
        sys.exit()

    if not is_inside(head):
        game_over_sound.play()
        pygame.time.wait(3000)
        #print('crash')
        pygame.quit()
        sys.exit()


    draw_block(RED, apple[0], apple[1],'apple')

    for block in snake_blocks:
        draw_block(SNAKE_COLOR, block[0], block[1],'block')

    if apple == head:
        apple_eat.play()
        total += 1
        speed = total // 5 + 1
        snake_blocks.insert(0,apple)
        apple = get_random_block()

    new_head = snake_block(head[0] + d_row, head[1] + d_col)
    snake_blocks.append(new_head)
    snake_blocks.pop(0)

    pygame.display.flip()
    timer.tick(3 + speed)