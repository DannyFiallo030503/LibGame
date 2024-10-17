from Character import Character

import pygame
import random

class NPC(Character):
    def __init__(self, x, y, w, h, image, hp, mp, sp, speed=5, move_delay=20, move_tick=3000, area_move=100, area_lock=300):
        super().__init__(x, y, w, h, image, hp, mp, sp, speed, move_delay)
        self.move_tick = move_tick
        self.area_move = area_move
        self.direction = None
        self.area_lock = area_lock
        self.m = 0
        
    def move(self):
        curren_time = pygame.time.get_ticks()
        if curren_time - self.last_move > self.move_delay:
            self.last_move = curren_time
            new_x, new_y = self.rect.x, self.rect.y
            if self.direction == 'L':
                new_x -= self.speed
            elif self.direction == 'R':
                new_x += self.speed
            elif self.direction == 'U':
                new_y -= self.speed
            elif self.direction == 'D':
                new_y += self.speed
                
            if ((new_x - self.x) ** 2 + (new_y - self.y) ** 2) ** 0.5 <= self.area_lock:
                self.rect.x = new_x
                self.rect.y = new_y
                self.m -= self.speed

    
    def update(self):
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