import pygame 
import sys

from Button import Button
from Joystick import Joystick
from Character import Character
from NPC import NPC
from Enemy import Enemy
from Object import (
    				Object, 
    				Object_Move
    			)

def prueba(SCREEN: pygame.surface.Surface, clock):
	
	character = Character(100, 100, 100, 100, None, 5, 5, 5, 5)
	npc = NPC(400, 100, 100, 100, None, 5, 5, 5, 5)
	enemy = Enemy(100, 400, 100, 100, None, 5, 5, 5, 5)
	obj_mov = Object_Move(200, 450, 100, 100, None)
	
	joystick = Joystick(SCREEN, True, 500, 250)
	
	x = 100
	y = 100
	line = None
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			
			line = joystick.handle_event(event)
			character.move_line(line)
			obj_mov.move(event)
						
		SCREEN.fill((130,130,130))
		
		joystick.draw()
		character.draw(SCREEN)
		npc.draw(SCREEN)
		enemy.draw(SCREEN)
		obj_mov.draw(SCREEN)

		character.update()
		npc.update()
		enemy.update([character])
		
		pygame.display.flip()
		clock.tick(20)
	
pygame.init()

# screen of the game
SCREEN = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

#color of screen
screen_color = (250, 200, 250)

# buttons
new_game_btn = Button(SCREEN, clock, 20, 50, 100, 50, (200,30,200), "New Game", (255,255,255), pygame.font.Font(None, 25), prueba)

run = True
while run:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			
		new_game_btn.handle_event(event)
			
	SCREEN.fill(screen_color)
	
	new_game_btn.draw()
	
	pygame.display.flip()
	
	clock.tick(60)

pygame.quit()
