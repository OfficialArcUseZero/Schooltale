import pygame
from sys import exit
import random

pygame.init()

screen_width = 800
screen_height = 400
spawn_delay = 2000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Schooltale')
clock = pygame.time.Clock()

background_surf = pygame.image.load('images/background.png')
background_rect = background_surf.get_rect()

gaming_surf = pygame.Surface((700, 300), pygame.SRCALPHA)
gaming_surf.fill((106, 103, 103, 128))

character_surf = pygame.image.load('images/character.png')
character_rect = character_surf.get_rect(topleft=(350,150))

backpack_surf = pygame.image.load('images/backpack.png')
backpack_rect = backpack_surf.get_rect(topleft=(675, 250))

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit() 
            exit() 

    screen.blit(background_surf, background_rect)
    screen.blit(gaming_surf, (50, 50))
    screen.blit(character_surf, character_rect)

    if pygame.time.get_ticks() > spawn_delay:
        screen.blit(backpack_surf, backpack_rect)

        right_speed = random.randint(5, 8)
        backpack_rect.right -= right_speed
        if backpack_rect.left < 50:
            backpack_rect.x = 675
            backpack_rect.y = random.randint(100, 250)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        character_rect.y -= 5
    if keys[pygame.K_a]:
        character_rect.x -= 5
    if keys[pygame.K_s]:
        character_rect.y += 5
    if keys[pygame.K_d]:
        character_rect.x += 5

    if character_rect.top < 35:
        character_rect.top = 35

    if character_rect.left < 35:
        character_rect.left = 35

    if character_rect.bottom > 365:
        character_rect.bottom = 365

    if character_rect.right > 765:
        character_rect.right = 765
    
    if character_rect.colliderect(backpack_rect):
        print("Collision")
    pygame.display.update()
    clock.tick(60)