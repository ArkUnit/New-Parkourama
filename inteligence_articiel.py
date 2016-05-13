import pygame
from pygame.locals import *
import sys

pygame.init()

window = pygame.display.set_mode((800,500))
Map = pygame.Surface((800,500))
clock = pygame.time.Clock()

fond_color = pygame.Color(95,205,228)

obstacle_1 = pygame.image.load("C:\\Users\\michael\\Pictures\\obstacle1.png")
obstacle_2 = pygame.image.load("C:\\Users\\michael\\Pictures\\obstacle2.png")

personnage_droite_arret = pygame.image.load("C:\\Users\\michael\\Pictures\\perso_pnj_droite_arret.png")
personnage_droite1 = pygame.image.load("C:\\Users\\michael\\Pictures\\perso_pnj_droite1.png")
personnage_droite2 = pygame.image.load("C:\\Users\\michael\\Pictures\\perso_pnj_droite2.png")
personnage_droite3 = pygame.image.load("C:\\Users\\michael\\Pictures\\perso_pnj_droite3.png")

personnage_gauche_arret = pygame.image.load("C:\\Users\\michael\\Pictures\\perso_pnj_gauche_arret.png")
personnage_gauche1 = pygame.image.load("C:\\Users\\michael\\Pictures\\perso_pnj_gauche1.png")
personnage_gauche2 = pygame.image.load("C:\\Users\\michael\\Pictures\\perso_pnj_gauche2.png")
personnage_gauche3 = pygame.image.load("C:\\Users\\michael\\Pictures\\perso_pnj_gauche3.png")

niveau_test = pygame.image.load("C:\\Users\\michael\\Pictures\\niveau_de_test(test).png")

continuer = True

def sol_deco():
	tente = pygame.image.load("C:\\Users\\michael\\Pictures\\tente.png")
	fleur1 = pygame.image.load("C:\\Users\\michael\\Pictures\\fleur1.png")
	fleur2 = pygame.image.load("C:\\Users\\michael\\Pictures\\fleur2.png")
	fleur3 = pygame.image.load("C:\\Users\\michael\\Pictures\\fleur3.png")
	pont = pygame.image.load("C:\\Users\\michael\\Pictures\\pont_en_bois.png")
	
	
	window.blit(tente,(385,375))
	window.blit(fleur1,(710,425))
	window.blit(fleur2,(600,430))
	window.blit(fleur3,(640,420))
	window.blit(fleur3,(540,420))
	window.blit(pont,(180,400))

class Obstacle1 (pygame.sprite.Sprite):
	
	def __init__ (self,group):
		pygame.sprite.Sprite.__init__(self,group)
		
	def update(self):
		self.image = obstacle_1

bounce_obstacle1 = Obstacle1([])
grp_ob1 = pygame.sprite.Group([bounce_obstacle1])
bounce_obstacle1.image = obstacle_1
bounce_obstacle1.rect = pygame.Rect(100,350,bounce_obstacle1.image.get_width(),bounce_obstacle1.image.get_height())
pygame.sprite.Group([bounce_obstacle1])

class Obstacle2 (pygame.sprite.Sprite):
	
	def __init__ (self, group):
		pygame.sprite.Sprite.__init__(self,group)
	
	def update(self):
		self.image = obstacle_2

bounce_obstacle2 = Obstacle2([])
grp_ob2 = pygame.sprite.Group([bounce_obstacle2])
bounce_obstacle2.image = obstacle_2
bounce_obstacle2.rect = pygame.Rect(300,350,bounce_obstacle2.image.get_width(),bounce_obstacle2.image.get_height())


pygame.sprite.Group([bounce_obstacle2])

class Joueur (pygame.sprite.Sprite):
	
	direction_droite = True
	direction_gauche = False
	continuer_animation = False
	sauv_animation = False
	
	cpt = 0
	
	def __init__ (self, group):
		pygame.sprite.Sprite.__init__(self, group)
	
	def update(self):
		
		if self.continuer_animation:
			if self.direction_droite:
				self.cpt += 1
				if self.cpt == 5:
					self.image = personnage_droite1
				if self.cpt == 10:
					self.image = personnage_droite2
				if self.cpt == 15:
					self.image = personnage_droite3
					self.cpt = 0
			if self.direction_gauche:
				self.cpt += 1
				if self.cpt == 5:
					self.image = personnage_gauche1
				if self.cpt == 10:
					self.image = personnage_gauche2
				if self.cpt == 15:
					self.image = personnage_gauche3
					self.cpt = 0
		

joueur = Joueur([])
grp_j = pygame.sprite.Group([joueur])
joueur.image = personnage_droite_arret
joueur.rect = pygame.Rect(400,320,joueur.image.get_width(),joueur.image.get_height())
joueur.rect.x = 500
joueur.rect.y = 100

x_change = 0
y_change = 0
pygame.sprite.Group([joueur])

x_pied_j = joueur.rect.x
y_pied_j = joueur.rect.y

tire = False
continuer_tire = True


jaune = pygame.Color(255,255,0)
bleu = pygame.Color(0,0,255)


x_balle = joueur.rect.x
y_balle = joueur.rect.y
direction_balle = "droite"

cpt_phy = 0
continuer_phy = True
sauv_cpt_phy = 0

saut = False
cpt_saut = 0
bloc_saut = False

while continuer:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		
		if event.type == KEYDOWN:
			if event.key == K_RIGHT:
				direction_balle = "droite"
				if Map.get_at((joueur.rect.x+16,joueur.rect.y+33)) != jaune or Map.get_at((joueur.rect.x+11,joueur.rect.y+33)) != jaune:
					if direction_balle == "droite":
						joueur.image = personnage_droite1
				joueur.sauv_animation = True
				joueur.continuer_animation = True
				joueur.direction_droite = True
				joueur.direction_gauche = False
				if direction_balle == "gauche":
					continuer_tire = False
					tire = False
					x_balle = joueur.rect.x
				x_change = 2
			
			
			if event.key == K_LEFT:
				direction_balle = "gauche"
				if Map.get_at((joueur.rect.x+16,joueur.rect.y+33)) != jaune or Map.get_at((joueur.rect.x+11,joueur.rect.y+33)) != jaune:
					if direction_balle == "gauche":
						joueur.image = personnage_gauche1
				joueur.sauv_animation = True
				joueur.continuer_animation = True
				joueur.direction_gauche = True
				joueur.direction_droite = False
				if direction_balle == "droite":
					continuer_tire = False
					tire = False
					x_balle = joueur.rect.x
				x_change = -2
			
			
			if event.key == K_n:
				if continuer_tire == False:
					tire = True
					continuer_tire = True
					x_balle = joueur.rect.x
					y_balle = joueur.rect.y
			
			if event.key == K_UP:
				if Map.get_at((joueur.rect.x+16,joueur.rect.y+36)) == jaune or Map.get_at((joueur.rect.x+11,joueur.rect.y+33)) == jaune:
					saut = True
					cpt_saut = 0
					if joueur.continuer_animation:
						joueur.sauv_animation = True
					joueur.continuer_animation = False
					joueur.direction_droite = False
					joueur.direction_gauche = False
					if direction_balle == "gauche":
						joueur.image = personnage_gauche1
					if direction_balle == "droite":
						joueur.image = personnage_droite1
			
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
					
		
		if event.type == KEYUP:
			if event.key == K_RIGHT:
				joueur.sauv_animation = False
				if Map.get_at((joueur.rect.x+16,joueur.rect.y+33)) == jaune or Map.get_at((joueur.rect.x+11,joueur.rect.y+33)) == jaune:
					joueur.image = personnage_droite_arret
				if Map.get_at((joueur.rect.x+16,joueur.rect.y+33)) != jaune or Map.get_at((joueur.rect.x+11,joueur.rect.y+33)) != jaune:
					if direction_balle == "droite":
						joueur.image = personnage_droite1
				joueur.continuer_animation = False
				joueur.cpt = 0
				x_change = 0
			if event.key == K_LEFT:
				joueur.sauv_animation = False
				if Map.get_at((joueur.rect.x+16,joueur.rect.y+33)) == jaune or Map.get_at((joueur.rect.x+11,joueur.rect.y+33)) == jaune:
					joueur.image = personnage_gauche_arret
				if Map.get_at((joueur.rect.x+16,joueur.rect.y+33)) != jaune or Map.get_at((joueur.rect.x+11,joueur.rect.y+33)) != jaune:
					if direction_balle == "gauche":
						joueur.image = personnage_gauche1
				joueur.continuer_animation = False
				joueur.cpt = 0
				x_change = 0
				
	
	
	
	if saut == False:
		if Map.get_at((joueur.rect.x+16,joueur.rect.y+35)) != jaune or Map.get_at((joueur.rect.x+11,joueur.rect.y+35)) != jaune:
			cpt_phy += 1
			if cpt_phy > 7 and cpt_phy < 11:
				y_change += 1
			if cpt_phy > 10:
				y_change += 1
	
	if saut:
		cpt_saut += 1
		cpt_phy = 0
		joueur.continuer_animation = False
		joueur.direction_droite = False
		joueur.direction_gauche = False
		if cpt_saut > 0 and cpt_saut < 2:
			y_change = -5
		if cpt_saut > 2 and cpt_saut < 4:
			y_change = -3
		if cpt_saut > 4 and cpt_saut < 6:
			saut = False
			cpt_saut = 0
			if direction_balle == "gauche":
				joueur.direction_gauche = True
				joueur.direction_droite = False
			if direction_balle == "droite":
				joueur.direction_droite = True
				joueur.direction_gauche = False


	
	
	
	if saut == False:
		if Map.get_at((joueur.rect.x+16,joueur.rect.y+33)) == jaune or Map.get_at((joueur.rect.x+11,joueur.rect.y+33)) == jaune:
			if joueur.sauv_animation:
				joueur.continuer_animation = True
				joueur.sauv_animation = False
			else:
				if joueur.continuer_animation == False:
					if direction_balle == "gauche":
						joueur.direction_gauche = True
						joueur.direction_droite = False
						joueur.image = personnage_gauche_arret
					if direction_balle == "droite":
						joueur.direction_droite = True
						joueur.direction_gauche = False
						joueur.image = personnage_droite_arret
			
		
	if saut == False:
		if Map.get_at((joueur.rect.x+16,joueur.rect.y+33)) == jaune or Map.get_at((joueur.rect.x+11,joueur.rect.y+33)) == jaune:
			y_change = 0
			joueur.rect.y -= 2
			cpt_phy = 0
	
	joueur.rect.x += x_change
	joueur.rect.y += y_change
	
	x_pied_j = joueur.rect.x
	y_pied_j = joueur.rect.y
	
	if continuer_tire:
		if direction_balle == "droite":
			x_balle += 10
		if direction_balle == "gauche":
			x_balle -= 10
	
	
	#~ if pygame.sprite.groupcollide(grp_j,grp_ob1,False,False):
		#~ print("sa marche ")
	
	if Map.get_at((x_pied_j+4,y_pied_j+5)) == jaune or Map.get_at((x_pied_j+4,y_pied_j+10)) == jaune or Map.get_at((x_pied_j+8,y_pied_j+20)) == jaune:
		x_change = 0
		joueur.rect.x += 3
		
	if Map.get_at((x_pied_j+28,y_pied_j+5)) == jaune or Map.get_at((x_pied_j+28,y_pied_j+10)) == jaune or Map.get_at((x_pied_j+22,y_pied_j+20)) == jaune:
		x_change = 0
		joueur.rect.x -= 3
		
	if joueur.rect.y > 470:
		y_change = 0
		joueur.rect.y -= 3
	
	if joueur.rect.x < 38:
		x_change = 0
		joueur.rect.x += 3
	
	if joueur.rect.x > 750:
		x_change = 0
		joueur.rect.x -= 3
	
	window.fill(fond_color)
	window.blit(niveau_test,(0,0))
	pygame.draw.rect(Map, jaune,(0,443,210,63))
	pygame.draw.rect(Map, jaune,(340,443,590,63))
	pygame.draw.rect(Map, jaune,(210,450,130,20))
	#~ pygame.draw.rect(window, bleu,(538,150,60,290))
	#~ pygame.draw.rect(Map, jaune,(150,425,10,100))
	grp_j.draw(window)
	sol_deco()
	
	if tire:
		pygame.draw.rect(window, jaune,( x_balle, y_balle , 10 ,5))
	
	bounce_obstacle1.update()
	bounce_obstacle2.update()
	joueur.update()
	pygame.display.update()
	clock.tick(40)
	

