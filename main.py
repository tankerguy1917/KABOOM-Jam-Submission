###### MAIN FILE ######

#### Imports ####
import pygame, sys, random
from pygame.locals import *
from assets.Images import *
from random import randint
from entities import Player, Bullet, Enemy, EnemyBullet
pygame.init()

#### Clock/FPS ####
clock = pygame.time.Clock()
FPS = 60

#### Window Stuff ####
WIN = (500, 300)
screen = pygame.display.set_mode(WIN, 0, 32)
display = pygame.Surface((WIN[0] / 2, WIN[1] / 2))

#### Class Instances
player = Player(player_img1, 2, 0, 0, 100, 5)

#### Main Menu Func ####
def main_menu():
	global text_alpha
	text_alpha = 255

	## Loop
	while True:
		## Gets mouse position/Sets mouse rect size
		mx, my = pygame.mouse.get_pos()
		mouse_rect = pygame.Rect(mx / 2, my / 2, 1, 1)

		##Fills/Clears screen
		display.fill((0, 29, 42))

		## Displays buttons/Sets buttons' rect
		display.blit(bg, (-30, 0))
		display.blit(name, (78, 20))
		name_rect = pygame.Rect(78, 20, name.get_width(), name.get_height())
		display.blit(play_img, (100, 70))
		play_rect = pygame.Rect(100, 70, play_img.get_width(), play_img.get_height())
		display.blit(credits_img, (100, 95))
		credits_rect = pygame.Rect(100, 95, credits_img.get_width(), credits_img.get_height())
		display.blit(tutorial_img, (100, 120))
		tut_rect = pygame.Rect(100, 120, tutorial_img.get_width(), tutorial_img.get_height())

		## Checks for input
		for e in pygame.event.get():
			if e.type == QUIT:
				pygame.quit()
				sys.exit()
			if e.type == KEYDOWN:
				if e.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if e.type == MOUSEBUTTONDOWN:
				if e.button == 1:
					if name_rect.colliderect(mouse_rect):
						player.health += 1
					if play_rect.colliderect(mouse_rect):
						survival_mode()
					if credits_rect.colliderect(mouse_rect):
						credits()
					if tut_rect.colliderect(mouse_rect):
						tutorial()

		## Updates screen
		screen.blit(pygame.transform.scale(display, WIN), (0, 0))
		pygame.display.update()
		clock.tick(FPS)

#### Credits Func ####
def credits():
	## Sets font
	font = pygame.font.Font("DotGothic16-Regular.ttf", 10)

	## Credit "titles"
	t1 = "Lead Game Design:"
	t2 = "Lead Graphics Design:"
	t3 = "Lead Programer:"
	t4 = "Play Testers:"
	t5 = "Special Thanks To:"

	## People to fill the credit "titles"
	c1 = "tankerguy1917"
	c2 = "tankerguy1917"
	c3 = "tankerguy1917"
	c4_1 = "tankerguy1917"
	c5_1 = "Benjamin Brewer"
	c5_2 = "Replit Community"
	c5_3 = "Replit.com"

	## Gets the text to a state to where it can be rendered
	text1 = font.render(t1, True, (0, 190, 145))
	text1_1 = font.render(c1, True, (0, 190, 145))
	text2 = font.render(t2, True, (0, 190, 145))
	text2_1 = font.render(c2, True, (0, 190, 145))
	text3 = font.render(t3, True, (0, 190, 145))
	text3_1 = font.render(c3, True, (0, 190, 145))
	text4 = font.render(t4, True, (0, 190, 145))
	text4_1 = font.render(c4_1, True, (0, 190, 145))
	text5 = font.render(t5, True, (0, 190, 145))
	text5_1 = font.render(c5_1, True, (0, 190, 145))
	text5_2 = font.render(c5_2, True, (0, 190, 145))
	text5_3 = font.render(c5_3, True, (0, 190, 145))

	## Misc
	cred_timer = 450
	cred_num = 1

	## Loop
	while True:
		## Fills/Clears screen
		display.fill((0, 29, 42))

		## Displays background image
		display.blit(bg, (-30, 0))

		## Renders credits
		if cred_num == 1:
			display.blit(text1, (10, 10))
			display.blit(text1_1, (120, 20))
			display.blit(text2, (10, 40))
			display.blit(text2_1, (120, 50))
			display.blit(text3, (10, 70))
			display.blit(text3_1, (120, 80))
		if cred_num == 2:
			display.blit(text4, (10, 10))
			display.blit(text4_1, (120, 20))
		if cred_num == 3:
			display.blit(text5, (10, 10))
			display.blit(text5_3, (120, 20))
			display.blit(text5_2, (120, 35))
			display.blit(text5_1, (120, 50))
		if cred_timer == 4:
			main_menu()

		## Countdown for player to read credits
		if cred_timer < 300 and cred_timer > 150:
			cred_num = 2
		elif cred_timer > 300:
			cred_num = 1
		elif cred_timer < 150:
			cred_num = 3
		elif cred_timer <= 0:
			cred_num = 4
		cred_timer -= 1

		## Checks for input
		for e in pygame.event.get():
			if e.type == QUIT:
				pygame.quit()
				sys.exit()
			if e.type == KEYDOWN:
				if e.key == K_ESCAPE:
					main_menu()

		## Updates screen
		screen.blit(pygame.transform.scale(display, WIN), (0, 0))
		pygame.display.update()
		clock.tick(FPS)

#### Tutorial Func ####
def tutorial():
	## Sets the font
	font = pygame.font.Font("DotGothic16-Regular.ttf", 10)

	## Tutorial messages
	t1 = "Use the arrow keys to move around!"
	t2 = "Use space to shoot!"
	t3 = "Kill enemies to get points!"

	## Makes the text able to be rendered
	text1 = font.render(t1, True, (0, 190, 145))
	text2 = font.render(t2, True, (0, 190, 145))
	text3 = font.render(t3, True, (0, 190, 145))

	## Sets sone player values for tutorial only
	player.rect[0] = 10
	player.rect[1] = 73
	player.max_bullets = 1
	player.enemy_list.append(Enemy(enemy1_img1, 1, display.get_width(), randint(20, display.get_height() - enemy1_img1.get_height()), 600))

	## Checks how far player is in tutorial
	milestones = 0
	wait_timer = 250

	## Loop
	while True:
		## Fills/Clears screen
		display.fill((0, 29, 42))

		## Displays background image
		display.blit(bg, (-30, 0))

		## Sees how far the player is in the tutorial/Displays tutorial messages
		if milestones == 0:
			display.blit(text1, (35, 0))
		if milestones == 1:
			display.blit(text2, (75, 0))
		if milestones == 2:
			display.blit(text3, (35, 0))
		if milestones == 3:
			wait_timer -= 1
		if wait_timer <= 0:
			main_menu()

		## Render sprites
		# Renders player
		display.blit(player.img, (player.rect[0], player.rect[1]))
		# Renders ammo images
		for i in range(player.max_bullets):
			display.blit(bullet_counter_img, (i * bullet_counter_img.get_width() * 1.25, 0))
		# Renders player health
		for  i in range(player.health):
			display.blit(heart_img, (i * heart_img.get_width() * 1.25, 15))
		# Renders player bullet images
		for bul in player.bullet_list:
			display.blit(bul.img, (bul.rect[0], bul.rect[1]))
			# Moves the bullets
			bul.move(player, display)
			for enemy in player.enemy_list:
				if bul.rect.colliderect(enemy.rect):
					player.enemy_list.remove(enemy)
					if milestones == 2:
						milestones += 1
		# Moves the player/Checks to make sure the player isn't out of bounds
		player.move()
		player.check_boundaries(display)
		# Renders enemy
		if milestones >= 2:
			for enemy in player.enemy_list:
				display.blit(enemy.img, (enemy.rect[0], enemy.rect[1]))
				# Moves enemy
				enemy.move(player)

		## Checks for input
		for e in pygame.event.get():
			if e.type == QUIT:
				pygame.quit()
				sys.exit()
			if e.type == KEYDOWN:
				if e.key == K_ESCAPE:
					main_menu()
				if e.key == K_RIGHT:
					player.movement[0] += player.speed
					if milestones == 0:
						milestones += 1
				if e.key == K_LEFT:
					player.movement[0] -= player.speed
					if milestones == 0:
						milestones += 1
				if e.key == K_UP:
					player.movement[1] -= player.speed
					if milestones == 0:
						milestones += 1
				if e.key == K_DOWN:
					player.movement[1] += player.speed
					if milestones == 0:
						milestones += 1
				if e.key == K_SPACE:
					player.bullet_list.append(Bullet(p_bullet, 10, player.rect[0] + player.img.get_width() + 1, player.rect[1] + player.img.get_height() / 2 - 4))
					if milestones == 1:
						milestones += 1
			if e.type == KEYUP:
				if e.key == K_RIGHT:
					player.movement[0] = 0
				if e.key == K_LEFT:
					player.movement[0] = 0
				if e.key == K_UP:
					player.movement[1] = 0
				if e.key == K_DOWN:
					player.movement[1] = 0
		
		## Updates the screen
		screen.blit(pygame.transform.scale(display, WIN), (0, 0))
		pygame.display.update()
		clock.tick(FPS)

#### Pick Game Mode Func ####
def play_type():
	
	## Loop
	while True:
		## Gets mouse position/Sets mouse rect
		mx, my = pygame.mouse.get_pos()
		mouse_rect = pygame.Rect(mx / 2, my / 2, 1, 1)

		## Fills/Clears screen
		display.fill((0, 29, 42))

		## Displays buttons/Sets buttons' rect
		display.blit(bg, (-30, 0))
		display.blit(classic_img, (75,30))
		classic_rect = pygame.Rect(75, 30, 100, 40)
		display.blit(survival_img, (75, 85))
		surv_rect = pygame.Rect(75, 85, 100, 40)

		## Checks for events
		for e in pygame.event.get():
			if e.type == QUIT:
				pygame.quit()
				sys.exit()
			if e.type == KEYDOWN:
				if e.key == K_ESCAPE:
					main_menu()
			if e.type == MOUSEBUTTONDOWN:
				if e.button == 1:
					if classic_rect.colliderect(mouse_rect):
						classic_mode()
					if surv_rect.colliderect(mouse_rect):
						survival_mode()

		## Updates screen
		screen.blit(pygame.transform.scale(display, WIN), (0, 0))
		pygame.display.update()
		clock.tick(FPS)

text_alpha = 255
def death_screen():
	global text_alpha
	font = pygame.font.Font("DotGothic16-Regular.ttf", 25)

	t = "YOU DIED"

	text = font.render(t, True, (0, 190, 145))


	while True:
		display.fill((0, 29, 42))

		display.blit(bg, (-30, 0))
		display.blit(text, (70, 30))
		text.set_alpha(text_alpha)
		text_alpha -= 2
		if text_alpha <= 0:
			main_menu()

		screen.blit(pygame.transform.scale(display, WIN), (0, 0))
		pygame.display.update()
		clock.tick(FPS)

#### Survival/Endless Waves Func ####
def survival_mode():
	if player.health < 5:
		player.health = 5
	player.enemy_list = []
	player.bullet_list = []

	kills = 0

	player.rect[1] = 73
	player.rect[0] = 10

	font = pygame.font.Font("DotGothic16-Regular.ttf", 10)
	
	while True:
		p_kills = str(kills)
		t = "KILLS: " + p_kills

		text = font.render(t, True, (0, 190, 145))

		if player.health > 0:
			display.fill((0, 29, 42))

			display.blit(bg, (-30, 0))
			display.blit(text, (200, 0))

			display.blit(player.img, (player.rect[0], player.rect[1]))
			player.move()
			player.check_boundaries(display)
			for i in range(player.health):
				display.blit(heart_img, (i * heart_img.get_width() * 1.25, 15))

			for bul in player.bullet_list:
				display.blit(bul.img, (bul.rect[0], bul.rect[1]))
				bul.move(player, display)
				for enemy in player.enemy_list:
					if bul.rect.colliderect(enemy.rect):
						player.enemy_list.remove(enemy)
						kills += 1

			if len(player.enemy_list) <= 9:
				player.enemy_list.append(Enemy(enemy1_img1, 1, display.get_width(), randint(20, display.get_height() - enemy1_img1.get_height()), 1200))
			else:
				player.enemy_list.remove(player.enemy_list[-1])

			for enemy in player.enemy_list:
				display.blit(enemy.img, (enemy.rect[0], enemy.rect[1]))
				enemy.move(player)
				enemy.shoot()
				for bul in enemy.bullet_list:
					display.blit(bul.img, (bul.rect[0], bul.rect[1]))
					bul.move(enemy)
					if bul.rect.colliderect(player.rect):
							player.health -= 1
							if len(enemy.bullet_list) > 0:
								enemy.bullet_list.remove(bul)

			## Checks for input
			for e in pygame.event.get():
				if e.type == QUIT:
					pygame.quit()
					sys.exit()
				if e.type == KEYDOWN:
					if e.key == K_ESCAPE:
						main_menu()
					if e.key == K_RIGHT:
						player.movement[0] += player.speed
					if e.key == K_LEFT:
						player.movement[0] -= player.speed
					if e.key == K_UP:
						player.movement[1] -= player.speed
					if e.key == K_DOWN:
						player.movement[1] += player.speed
					if e.key == K_SPACE:
						player.bullet_list.append(Bullet(p_bullet, 10, player.rect[0] + player.img.get_width() + 1, player.rect[1] + player.img.get_height() / 2 - 4))
				if e.type == KEYUP:
					if e.key == K_RIGHT:
						player.movement[0] = 0
					if e.key == K_LEFT:
						player.movement[0] = 0
					if e.key == K_UP:
						player.movement[1] = 0
					if e.key == K_DOWN:
						player.movement[1] = 0

			screen.blit(pygame.transform.scale(display, WIN), (0, 0))
			pygame.display.update()
			clock.tick(FPS)

		else:
			death_screen()

#### Level-up Func ####
def level_up(game_mode):
	pass

main_menu()