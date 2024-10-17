import pygame

from Object import Object
from Line import Line

class Character(Object):
	def __init__(self, x, y, w, h, image, hp, mp, sp, speed=5, move_delay=20):
		super().__init__(x, y, w, h, image)
		self.hp = hp
		self.hp_total = hp
		self.mp = mp
		self.sp = sp
		self.speed = speed
		self.line = None
		self.walk = False
		self.move_delay= move_delay
		self.last_move = pygame.time.get_ticks()
		
	def draw(self, screen):
		pygame.draw.rect(screen, (200,200,200), self.rect)
		
	def move(self, x, y):
		self.rect.x += x
		self.rect.y += y
		
	def move_line(self, line: Line):
		curren_time = pygame.time.get_ticks()
		if line is not None and curren_time - self.last_move > self.move_delay:
			point = line.dist(self.rect.x, self.rect.y, line.m, line.n, self.speed, (line.point1, line.point2))
			if point is not None:
				self.last_move = curren_time
				self.rect.x = point[0]
				self.rect.y = point[1]
				self.line = line
				self.walk = True
		if line is None:
			self.walk = False
			self.line = None
			
	def update(self):
		if self.walk:
			if self.line is not None:
				self.move_line(self.line)
				
			
			