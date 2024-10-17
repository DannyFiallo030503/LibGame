import pygame
import random
import math

from NPC import NPC
from Object import Object

class Enemy(NPC):
    def __init__(self, x, y, w, h, image, hp, mp, sp, speed=5, move_delay=20, move_tick=3000, area_move=100, area_lock=300):
        super().__init__(x, y, w, h, image, hp, mp, sp, speed, move_delay, move_tick, area_move, area_lock)
        self.out_range = False
        
    def update(self, players: list[Object]):
        for p in players:
            if self.is_in_range(p) == 1:
                self.move_to_point(p.rect.x, p.rect.y)
            elif self.is_in_range(p) == 2:
                ...
        
        if self.m <= 0:
            self.walk = False
        
        if not self.walk:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_move > self.move_tick:
                self.last_move = current_time
                self.m = random.randint(0, self.area_move)
                self.direction = random.choice(['L', 'R', 'U', 'D'])
                self.walk = True
        else:
            self.move()
            
    def move_to_point(self, x, y):
        curren_time = pygame.time.get_ticks()
        if curren_time - self.last_move > self.move_delay:
            self.last_move = curren_time
            if self.rect.x - x > 0:
                self.rect.x -= self.speed
            elif self.rect.x - x < 0:
                self.rect.x += self.speed
            if self.rect.y - y > 0:
                self.rect.y -= self.speed
            elif self.rect.y - y < 0:
                self.rect.y += self.speed
        
    def is_in_range(self, object: Object):
        distancia = math.sqrt((object.rect.x - self.x) ** 2 + (object.rect.y - self.y) ** 2)
        if distancia <= self.area_lock:
            if self.hp >= self.hp_total * 10 / 100:
                return 1  
            else:
                return 2  
        return 0