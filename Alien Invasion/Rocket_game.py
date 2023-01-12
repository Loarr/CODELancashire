import sys
import pygame

class Rocket():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.moving_right = False
        self.moving_down = False
        self.moving_left = False
        self.moving_up = False

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Rocket Game")

    rocket = Rocket(screen)


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    rocket.moving_right = True
                elif event.key == pygame.K_LEFT:
                    rocket.moving_left = True
                elif event.key == pygame.K_UP:
                    rocket.moving_up = True
                elif event.key == pygame.K_DOWN:
                    rocket.moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    rocket.moving_right = False
                elif event.key == pygame.K_LEFT:
                    rocket.moving_left = False
                elif event.key == pygame.K_UP:
                    rocket.moving_up = False
                elif event.key == pygame.K_DOWN:
                    rocket.moving_down = False

        if rocket.moving_left and rocket.rect.left > 0:
            rocket.rect.centerx -= 1
        if rocket.moving_right and rocket.rect.right< rocket.screen_rect.right:
            rocket.rect.centerx += 1
        if rocket.moving_up and rocket.rect.top > rocket.screen_rect.top:
            rocket.rect.centery -= 1
        if rocket.moving_down and rocket.rect.bottom < rocket.screen_rect.bottom:
            rocket.rect.centery += 1
        screen.fill((250,225,0))

        rocket.screen.blit(rocket.image, rocket.rect)
        pygame.display.flip()


run_game()
