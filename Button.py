import pygame

class Button:
	def __init__(self, screen, clock,  x, y, w, h, color, text, text_color, font, action):
		self.rect = pygame.Rect(x, y, w, h)
		self.color = color
		self.clock = clock
		self.screen = screen
		self.text = text
		self.font = font
		self.text_btn = self.font.render(text, True, text_color)
		self.text_rect = self.text_btn.get_rect(center=self.rect.center)
		self.action = action
	
	# draw in the screen
	def draw(self):
		pygame.draw.rect(self.screen, self.color, self.rect)
		self.screen.blit(self.text_btn, self.text_rect)
	
	# handle events in tehe screen
	def handle_event(self, event):
		if event.type == pygame.MOUSEBUTTONDOWN:
			if self.rect.collidepoint(event.pos):
				self.action(self.screen, self.clock)
			