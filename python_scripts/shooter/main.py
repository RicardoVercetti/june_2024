# main.py
import pygame
from os.path import join
from random import randint
# from datetime import datetime
import time


# general setup
pygame.init()
WIDTH, HEIGHT = 1280, 720 

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space shooter")
running = True
clock = pygame.time.Clock()


# plain surface
surf = pygame.Surface((100, 200))
surf.fill("orange")
x = 50

star_pos = [(randint(0, WIDTH), randint(0, HEIGHT)) for i in range(20)]

# image surface
# python_scripts/shooter/res/images/player.png
player_surf = pygame.image.load(join("res","images","player.png")).convert_alpha()
player_rect = player_surf.get_frect(center=(50,HEIGHT-50))

star_surf = pygame.image.load(join("res","images","star.png")).convert_alpha()  # C:\Users\HP\Documents\Repos\june_2024\python_scripts\shooter\res\images\star.png

meteor_surf = pygame.image.load(join("res","images","meteor.png")).convert_alpha()    # C:\Users\HP\Documents\Repos\june_2024\python_scripts\shooter\res\images\meteor.png
meteor_rect = meteor_surf.get_frect(center=(WIDTH/2,HEIGHT/2))

laser_surf = pygame.image.load(join("res","images","laser.png")).convert_alpha()
laser_rect = laser_surf.get_frect(center=(20, HEIGHT-20))


print("player rect :", player_rect)
print("Meteor rect :", meteor_rect)

direction = "right"

n = 0

# to calculate my current fps
duration = 1 # second
frames = 0
previous_time = time.time()
residual_time = 0

while running:
	clock.tick(60)
	# event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	# print("Looping", n)
	n += 1

	# draw the game
	# x += 0.1

	# frames
	frames += 1
	current_time = time.time()
	if current_time - previous_time >= duration:
		residual_time += current_time - previous_time - duration
		print("Frames : ", frames)
		print("residual_time: ", residual_time)
		frames = 0
		previous_time = time.time() 



	display_surface.fill("darkgrey")


	# 20 random star placements
	for poss in star_pos:
		display_surface.blit(star_surf, poss)

	if direction == "right":
		player_rect.right += 0.9
		if player_rect.right >= WIDTH:
			direction = "left"
	if direction == "left":
		player_rect.left -= 0.9
		if player_rect.left < 0:
			direction = "right"

	laser_rect.left = 20
	laser_rect.bottom = HEIGHT - 20



	display_surface.blit(meteor_surf, meteor_rect)   # params -> surface, position(tuple)
	display_surface.blit(laser_surf, laser_rect)
	display_surface.blit(player_surf, player_rect)      # block image transfer

	pygame.display.update()     # .flip() can also be used, only updates specific portion


print("Exited out of the pygame loop.")






# print(pygame.display.get_desktop_sizes())
pygame.quit()




# excercise

# import a meteore and place it at the center
# import a laser, place it at the bottom left with 20px padding to left and bottom
# make the player bounce from left to right