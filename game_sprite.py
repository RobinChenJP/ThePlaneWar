import pygame
import random

SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FRAME_PER_SECOND = 60


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, img_path, speed=1):
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
        self.speed = speed


class PlaneSprite(GameSprite):

    def __init__(self, img_path):
        super().__init__(img_path, 0)
        self.is_survive = True
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 60

    def update(self, *args):
        pass

    def control_direction(self, pressed_key):
        if pressed_key[pygame.K_LEFT] and self.rect.x > -20:
            self.rect.x -= 2
        elif pressed_key[pygame.K_RIGHT] and self.rect.right < SCREEN_RECT.width + 20:
            self.rect.x += 2
        if pressed_key[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= 2
        elif pressed_key[pygame.K_DOWN] and self.rect.bottom < SCREEN_RECT.height:
            self.rect.y += 2

    def kill(self):
        super().kill()
        self.is_survive = False



class EnemySprite(GameSprite):
    def __init__(self, img_path):
        super().__init__(img_path, 1)
        max_x = SCREEN_RECT.width - self.rect.width
        self.random_show(max_x)

    def update(self, *args):
        self.rect.y += self.speed
        if self.rect.y > SCREEN_RECT.height:
            self.kill()

    def random_show(self, max_x):
        self.rect.x = random.randint(0, max_x)
        self.rect.bottom = 0
        self.speed = random.randint(1, 3)


class BulletSprite(GameSprite):
    def __init__(self, img_path, plane_sprite, ):
        super().__init__(img_path, 2)
        self.rect.centerx = plane_sprite.rect.centerx
        self.rect.bottom = plane_sprite.rect.y

    def update(self, *args):
        super().update()
        self.rect.y -= self.speed
        if self.rect.bottom <= 0:
            self.kill()


class BackgroundSprite(GameSprite):
    def __init__(self, img_path, speed=1, is_alt=False):
        super().__init__(img_path, speed)
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self, *args):
        self.rect.y += self.speed
        if self.rect.y > self.rect.height:
            self.rect.y = -self.rect.height
