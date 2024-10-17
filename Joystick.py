import pygame
import math

from Line import Line

class Joystick:
    def __init__(self, screen, mode_dark, x, y, r=100, width=5):
        self.screen = screen
        self.set_mode(mode_dark)
        self.x = x
        self.y = y
        self.pos_joy = (x, y)
        self.r = r
        self.radio = 2*r
        self.width = width
        self.rect = pygame.Rect(self.x - self.r * 1.2, self.y - self.r * 1.2, self.r * 2.4, self.r * 2.4)
        self.pick_up = False

    def draw(self):
        pygame.draw.circle(self.screen, self.mode, self.pos_joy, self.r, self.width)
        pygame.draw.circle(self.screen, self.mode, (self.x, self.y), self.r * 2/3, 0)

    def set_mode(self, mode_dark):
        if mode_dark:
            self.mode = (24, 23, 28)
        else:
            self.mode = (233, 233, 233)
            
    def collition(self, point: tuple) -> bool:
        x, y = point  
        dist = math.sqrt((self.pos_joy[0] - x) ** 2 + (self.pos_joy[1] - y) ** 2)
        return dist <= self.radio

    def handle_event(self, event: pygame.event.Event):
        if event.type in (pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN, pygame.MOUSEMOTION):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.collition(event.pos):
                    self.pick_up = not self.pick_up
                    self.x = event.pos[0]
                    self.y = event.pos[1]
                    return Line((self.pos_joy[0], self.pos_joy[1]), (self.x, self.y))
                else:
                    self.x = self.pos_joy[0]
                    self.y = self.pos_joy[1]
                    self.pick_up = not self.pick_up
                    return None
            elif event.type == pygame.MOUSEMOTION and self.pick_up:
                if self.collition(event.pos):
                    self.x = event.pos[0]
                    self.y = event.pos[1]
                    return Line((self.pos_joy[0], self.pos_joy[1]), (self.x, self.y))
                else:
                    l = Line((self.pos_joy[0], self.pos_joy[1]), event.pos)
                    new_l = l.point_in_radio(self.radio)
                    self.x = new_l.point2[0]
                    self.y = new_l.point2[1]
                    return new_l
                
        return Line((self.pos_joy[0], self.pos_joy[1]), (self.x, self.y))