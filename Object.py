import pygame

class Object:
    def __init__(self, x, y, w, h, image) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = image
        self.rect = pygame.Rect(x, y, w, h)

class Object_Move(Object):
    def __init__(self, x, y, w, h, image) -> None:
        super().__init__(x, y, w, h, image)
        self.pick_up = False
        
    def draw(self, screen):
        pygame.draw.rect(screen, (200,200,200), self.rect)
        
    def move(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.pick_up = not self.pick_up
                
        if self.pick_up and event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
            self.rect.x = event.pos[0]
            self.rect.y = event.pos[1]        
        
    