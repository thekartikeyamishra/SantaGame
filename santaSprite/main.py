import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Santa's Gift Run")

# Loading assests
background = pygame.image.load("assets/background.jpg")
santa_img = pygame.image.load("assets/santa.png")
gift_img = pygame.image.load("assets/gift.png")
snowball_img = pygame.image.load("assets/snowball.png")

# Scaling image
santa_img = pygame.transform.scale(santa_img, (80, 80))
gift_img = pygame.transform.scale(gift_img, (40, 40))
snowball_img = pygame.transform.scale(snowball_img, (50, 50))

# Background music
pygame.mixer.music.load("assets/music.mp3")
pygame.mixer.music.play(-1)  # LOOPING

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# FONT
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

# Santa's properties
santa = pygame.Rect(100, HEIGHT // 2, 80, 80)
santa_speed = 5

gifts = []
snowballs = []
gift_speed = 5
snowball_speed = 7

# Game Variable
score = 0
high_score = 0
game_over = False


# Helper Function
def draw_text(text, font, color, x, y):
    surface = font.render(text, True, color)
    screen.blit(surface, (x, y))


def reset_game():
    global gifts, snowballs, score, game_over
    gifts.clear()
    snowball.clear()
    score = 0
    game_over = False


# Game Loop

running = True
while running:
    screen.fill(WHITE)
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_UP] and santa.top > 0:
            santa.y -= santa_speed
        if keys[pygame.K_DOWN] and santa.bottom < HEIGHT:
            santa.y += santa_speed

        if random.randint(1, 50) == 1:
            gifts.append(pygame.Rect(WIDTH, random.randint(0, HEIGHT - 40), 40, 40))

        if random.randint(1, 70) == 1:
            snowballs.append(pygame.Rect(WIDTH, random.randint(0, HEIGHT - 50), 50, 50))

        for gift in list(gifts):
            gift.x -= gift_speed
            if santa.colliderect(gift):
                gifts.remove(gift)
            elif gift.x < 0:
                gifts.remove(gift)

        for snowball in list(snowballs):
            snowball.x -= snowball_speed
            if santa.colliderect(snowball):
                game_over = True
            elif snowball.x < 0:
                snowballs.remove(snowball)

        for gift in gifts:
            screen.blit(gift_img, (gift.x, gift.y))
        for snowball in snowballs:
            screen.blit(snowball_img, (snowball.x, snowball.y))

        screen.blit(santa_img, (santa.x, santa.y))
        draw_text(f"Score: {score}", font, WHITE, 10, 10)

    else:
        draw_text("GAME OVER", font, RED, WIDTH//2 - 80, HEIGHT // 2 - 40)
        draw_text(f"Your Score: {score}", font, WHITE, WIDTH//2 - 80, HEIGHT // 2)
        draw_text(f"High Score: {high_score}", font, WHITE, WIDTH//2 - 80, HEIGHT // 2 + 40)
        draw_text("Press R to Restart", font, WHITE, WIDTH//2 - 100, HEIGHT // 2 + 80)

        if keys[pygame.K_r]:
            high_score = max(high_score, score)
            reset_game()
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()