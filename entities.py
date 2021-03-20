###### ENTITY FILE ######

#### Imports ####
import pygame, sys, random
from assets.Images import p_bullet
from pygame.locals import *
from random import randint

#### Entity Class ####
class Entity:
	def __init__(self, img, speed, sx, sy):
		self.img = img
		self.speed = speed
		self.sx = sx
		self.sy = sy
		self.rect = pygame.Rect(sx, sy, self.img.get_width(), self.img.get_height())


class Player(Entity):
	def __init__(self, img, speed, sx, sy, max_bullets, health):
		super().__init__(img, speed, sx, sy)
		self.movement = [0, 0]
		self.bullet_list = []
		self.enemy_list = []
		self.boss_list = []
		self.max_bullets = max_bullets
		self.health = health

	def move(self):
		self.rect[0] += self.movement[0]
		self.rect[1] += self.movement[1]

	def check_boundaries(self, surf):
		if self.rect[0] < 1:
			self.rect[0] = 1
		if self.rect[0] > surf.get_width() - self.img.get_width() - 1:
			self.rect[0]  = surf.get_width() - self.img.get_width() - 1
		if self.rect[1] < 25:
			self.rect[1] = 25
		if self.rect[1] > surf.get_height() - self.img.get_height() - 1:
			self.rect[1] = surf.get_height() - self.img.get_height() - 1


class Bullet(Entity):
	def __init__(self, img, speed, sx, sy):
		super().__init__(img, speed, sx, sy)

	def move(self, entity, surf):
		self.rect[0] += self.speed
		if self.rect[0] > surf.get_width():
			entity.bullet_list.remove(self)

class Enemy(Entity):
	def __init__(self, img, speed, sx, sy, spawn_rate):
		super().__init__(img, speed, sx, sy)
		self.bullet_list = []
		self.spawn_rate = spawn_rate
		
	def move(self, entity):
		self.rect[0] -= self.speed
		if self.rect[0] < 0:
			entity.enemy_list.remove(self)
	
	def spawn(self, entity):
		s = randint(1, self.spawn_rate)
		if s == self.spawn_rate:
			entity.enemy_list.append(self)
	
	def shoot(self):
		s = randint(1, 125)
		if s == 125:
			self.bullet_list.append(EnemyBullet(p_bullet, 3, self.rect[0], self.rect[1]))


class EnemyBullet(Entity):
	def __init__(self, img, speed, sx, sy):
		super().__init__(img, speed, sx, sy)

	def move(self, entity):
		self.rect[0] -= self.speed
		if self.rect[0] == 0:
			entity.bullet_list.remove(self)