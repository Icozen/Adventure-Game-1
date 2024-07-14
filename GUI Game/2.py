import pygame
import sys
import random as r
import time

pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 36)
# # Game variables
# player_hp = 150
# enemy_hp = 70
# player_dmg = r.randint(20, 30)
# enemy_dmg = r.randint(1, 15)
# crit_hit_chance = 10
# kills = 0
# # Initialize turn_counter outside of any function to ensure it's globally accessible
# turn_counter = 0  # Counter to manage turns

def draw_text(text, color, x, y, font=font):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

def game_loop():
    # Game variables
    player_hp = 150
    enemy_hp = 70
    player_dmg = r.randint(20, 30)
    enemy_dmg = r.randint(1, 15)
    crit_hit_chance = 10
    kills = 0
    # Initialize turn_counter outside of any function to ensure it's globally accessible
    turn_counter = 0  # Counter to manage turns
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(WHITE)
        draw_text(f"Player HP: {player_hp}", BLACK, 10, 10)
        draw_text(f"Enemy HP: {enemy_hp}", BLACK, 10, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and turn_counter % 2 == 0:  # Player can act on even turns
            if r.randint(1, 100) <= crit_hit_chance:
                print("Critical hit!")
                enemy_hp -= player_dmg * 2
                print(f"Dealt {player_dmg * 2} damage!")
            else:
                enemy_hp -= player_dmg
                print(f"Dealt {player_dmg} damage!")

            if enemy_hp <= 0:
                kills += 1
                print("Enemy defeated!")
                enemy_hp = 70  # Reset enemy HP for next encounter

        if turn_counter % 2!= 0:  # Enemy acts on odd turns
            if player_hp > 0:
                player_hp -= enemy_dmg
                print(f"Received {enemy_dmg} damage!")
                if player_hp <= 0:
                    print("Game Over!")
                    running = False

        turn_counter += 1  # Increment turn counter
        pygame.time.delay(500)  # Delay between turns, adjust as needed

        pygame.display.flip()

    pygame.quit()
    sys.exit()

game_loop()
