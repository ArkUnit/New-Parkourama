import pygame
from pygame.locals import *
import sys
import random
from random import randrange

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

personnage_haut_arret = pygame.image.load("C:\\Users\\michael\\Pictures\\perso_haut_arret.png")
personnage_haut1 = pygame.image.load("C:\\Users\\michael\\Pictures\\perso_haut1.png")
personnage_haut2 = pygame.image.load("C:\\Users\\michael\\Pictures\\perso_haut2.png")
personnage_haut3 = pygame.image.load("C:\\Users\\michael\\Pictures\\perso_haut3.png")

monstre_droite1 = pygame.image.load("C:\\Users\\michael\\Pictures\\slime_droite1.png")
monstre_droite2 = pygame.image.load("C:\\Users\\michael\\Pictures\\slime_droite2.png")
monstre_droite3 = pygame.image.load("C:\\Users\\michael\\Pictures\\slime_droite3.png")
monstre_droite4 = pygame.image.load("C:\\Users\\michael\\Pictures\\slime_droite4.png")

monstre_gauche1 = pygame.image.load("C:\\Users\\michael\\Pictures\\slime_gauche1.png")
monstre_gauche2 = pygame.image.load("C:\\Users\\michael\\Pictures\\slime_gauche2.png")
monstre_gauche3 = pygame.image.load("C:\\Users\\michael\\Pictures\\slime_gauche3.png")
monstre_gauche4 = pygame.image.load("C:\\Users\\michael\\Pictures\\slime_gauche4.png")

personnage_cookie_gauche1 = pygame.image.load("C:\\Users\\michael\\Pictures\\cookie_gauche_perso1.png")
personnage_cookie_gauche2 = pygame.image.load("C:\\Users\\michael\\Pictures\\cookie_gauche_perso2.png")
personnage_cookie_gauche3 = pygame.image.load("C:\\Users\\michael\\Pictures\\cookie_gauche_perso3.png")

personnage_cookie_droite1 = pygame.image.load("C:\\Users\\michael\\Pictures\\cookie_droite_perso1.png")
personnage_cookie_droite2 = pygame.image.load("C:\\Users\\michael\\Pictures\\cookie_droite_perso2.png")
personnage_cookie_droite3 = pygame.image.load("C:\\Users\\michael\\Pictures\\cookie_droite_perso3.png")

niveau_test = pygame.image.load("C:\\Users\\michael\\Pictures\\niveau_de_test(test).png")

cookie = pygame.image.load("C:\\Users\\michael\\Pictures\\cookies.png")

coeur = pygame.image.load("C:\\Users\\michael\\Pictures\\coeur.png")

continuer = True
continuer_interface = True

def interface():
	global continuer_interface
	global window
	fond_interface = pygame.image.load("C:\\Users\\michael\\Pictures\\interface_de_niveau_test.png")
	boutton_quitter = pygame.image.load("C:\\Users\\michael\\Pictures\\boutton_quitter.png")
	boutton_quitter2 = pygame.image.load("C:\\Users\\michael\\Pictures\\boutton_quitter.png")
	boutton_quitter_select = pygame.image.load("C:\\Users\\michael\\Pictures\\boutton_quitter_select.png")
	boutton_quitter_apuyer = pygame.image.load("C:\\Users\\michael\\Pictures\\boutton_quitter_apuyer.png")
	
	boutton_play = pygame.image.load("C:\\Users\\michael\\Pictures\\boutton_play.png")
	boutton_play2 = pygame.image.load("C:\\Users\\michael\\Pictures\\boutton_play.png")
	boutton_play_apuyer = pygame.image.load("C:\\Users\\michael\\Pictures\\boutton_play_apuyer.png")
	boutton_play_select = pygame.image.load("C:\\Users\\michael\\Pictures\\boutton_play_select.png")
	
	bloc_select_play = False
	bloc_select_quitter = False
	
	def button_play(x,y):
		if x < 433 and x > 295:
			if y < 300 and y > 248:
				return True
		return False
	
	def button_play_select(x,y):
		if x < 433 and x > 295:
			if y < 300 and y > 248:
				return True
		return False
	
	def button_quitter(x,y):
		if x < 433 and x > 295:
			if y < 400 and y > 348:
				return True
		return False
	
	def button_quitter_select(x,y):
		if x < 433 and x > 295:
			if y < 400 and y > 348:
				return True
		return False
	
	while continuer_interface:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					x,y = pygame.mouse.get_pos()
					
					if button_play(x,y):
						continuer_interface = False
					
					if button_quitter(x,y):
						pygame.quit()
						sys.exit()
			
			elif event.type == MOUSEMOTION:
				
				x,y = pygame.mouse.get_pos()
				
				if button_play_select(x,y):
					if bloc_select_play == False:
						boutton_play = boutton_play_select
				else:
					if bloc_select_play == False:
						boutton_play = boutton_play2
						
				if button_quitter_select(x,y):
					if bloc_select_quitter == False:
						boutton_quitter = boutton_quitter_select
				else:
					if bloc_select_quitter == False:
						boutton_quitter = boutton_quitter2
				
		
		window.blit(fond_interface,(0,0))
		window.blit(boutton_play,(300,250))
		window.blit(boutton_quitter,(300,350))
		pygame.display.update()
			

interface()
	

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
	direction_monter = False
	block_mouv_cookie = False
	
	cpt = 0
	
	def __init__ (self, group):
		pygame.sprite.Sprite.__init__(self, group)
	
	def update(self):
		
		if self.continuer_animation:
			if self.block_mouv_cookie == False:
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
				if self.direction_monter:
					self.cpt += 1
					if self.cpt == 5:
						self.image = personnage_haut1
					if self.cpt == 10:
						self.image = personnage_haut2
					if self.cpt == 15:
						self.image = personnage_haut3
						self.cpt = 0
			
			elif self.block_mouv_cookie:
				
				if self.direction_droite:
					self.cpt += 1
					if self.cpt == 3:
						self.image = personnage_cookie_droite1
					if self.cpt == 6:
						self.image = personnage_cookie_droite2
					if self.cpt == 9:
						self.image = personnage_cookie_droite3
					if self.cpt == 12:
						self.image = personnage_cookie_droite2
					if self.cpt == 15:
						self.image = personnage_cookie_droite1
						self.cpt = 0
				if self.direction_gauche:
					self.cpt += 1
					if self.cpt == 3:
						self.image = personnage_cookie_gauche1
					if self.cpt == 6:
						self.image = personnage_cookie_gauche2
					if self.cpt == 9:
						self.image = personnage_cookie_gauche3
					if self.cpt == 12:
						self.image = personnage_cookie_gauche2
					if self.cpt == 15:
						self.image = personnage_cookie_gauche1
						self.cpt = 0
		

joueur = Joueur([])
grp_j = pygame.sprite.Group([joueur])
joueur.image = personnage_droite_arret
joueur.rect = pygame.Rect(400,320,14,21)
joueur.rect.x = 500
joueur.rect.y = 350

x_change = 0
y_change = 0

cpt_block_mouv_cookie = 0

nb_vie_j = 4
cpt_degat = 0
continuer_regeneration = False
cpt_regeneration = 100
continuer_degat = False

pygame.sprite.Group([joueur])



class Bot(pygame.sprite.Sprite):
	
	cpt = 0
	continuer_animation_bot = False
	direct_bot_droite = False
	direct_bot_gauche = False
	
	def __init__(self, group):
		pygame.sprite.Sprite.__init__(self, group)
		
	def update(self):
		if self.continuer_animation_bot:
			if self.direct_bot_droite:
				self.cpt += 1
				if self.cpt == 5:
					self.image = monstre_droite1
				if self.cpt == 10:
					self.image = monstre_droite2
				if self.cpt == 15:
					self.image = monstre_droite3
					self.cpt = 0
			if self.direct_bot_gauche:
				self.cpt += 1
				if self.cpt == 5:
					self.image = monstre_gauche1
				if self.cpt == 10:
					self.image = monstre_gauche2
				if self.cpt == 15:
					self.image = monstre_gauche3
					self.cpt = 0


bot = Bot([])
grp_b = pygame.sprite.Group([bot])
bot.image = monstre_droite2
bot.rect = pygame.Rect(400,320,15,10)
bot.rect.x = 100
bot.rect.y = 419

x_change_bot = 0
y_change_bot = 0

adopter = False

block_marche_bot = 0
block_tourner_gauche = False
block_tourner_droit = False

sauv_derniere_direct_bot = "droite"

action_bot_choix = randrange(0,20)

pygame.sprite.Group([bot])


nb_cookie = 99999

x_pied_j = joueur.rect.x
y_pied_j = joueur.rect.y

tire = False
continuer_tire = True



jaune = pygame.Color(255,255,0)
black = pygame.Color(0,0,0)
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

continuer_grimper = False
grimpe = False
block_phy = False


particule_coeur = False

def paricule():
	global particule_coeur
	
	cpt_particule = 0
	
	if particule_coeur:
		cpt_particule += 1
		if cpt_particule == 50:
			particule_coeur = False
			cpt_particule = 0



while continuer:
	if Map.get_at((joueur.rect.x+28,joueur.rect.y+10)) == bleu or Map.get_at((joueur.rect.x+4,joueur.rect.y+10)) == bleu:
		grimpe = True
		saut = False
		
	else:
		grimpe = False
		block_phy == False
	
	action_bot_choix = randrange(0,50)
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		
		if event.type == KEYDOWN:
			
			if event.key == K_SPACE:
				if Map.get_at((joueur.rect.x+16,joueur.rect.y+35)) == jaune or Map.get_at((joueur.rect.x+11,joueur.rect.y+35)) == jaune:
					joueur.block_mouv_cookie = True
					joueur.continuer_animation = True
					x_change = 0
			
			if event.key == K_RIGHT:
				if joueur.block_mouv_cookie == False:
					direction_balle = "droite"
					if Map.get_at((joueur.rect.x+16,joueur.rect.y+35)) != jaune or Map.get_at((joueur.rect.x+11,joueur.rect.y+35)) != jaune:
						if direction_balle == "droite":
							if grimpe == False:
								joueur.image = personnage_droite1
					joueur.sauv_animation = True
					joueur.continuer_animation = True
					if Map.get_at((joueur.rect.x+16,joueur.rect.y+35)) == jaune or Map.get_at((joueur.rect.x+11,joueur.rect.y+35)) == jaune:
						joueur.direction_droite = True
					joueur.direction_gauche = False
					if direction_balle == "gauche":
						continuer_tire = False
						tire = False
						x_balle = joueur.rect.x
					x_change = 2
			
			
			if event.key == K_LEFT:
				if joueur.block_mouv_cookie == False:
					direction_balle = "gauche"
					if Map.get_at((joueur.rect.x+16,joueur.rect.y+35)) != jaune or Map.get_at((joueur.rect.x+11,joueur.rect.y+35)) != jaune:
						if direction_balle == "gauche":
							if grimpe == False:
								joueur.image = personnage_gauche1
					joueur.sauv_animation = True
					joueur.continuer_animation = True
					if Map.get_at((joueur.rect.x+16,joueur.rect.y+35)) == jaune or Map.get_at((joueur.rect.x+11,joueur.rect.y+35)) == jaune:
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
				if joueur.block_mouv_cookie == False:
					if grimpe == False:
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
					
					if grimpe:
						joueur.continuer_animation = True
						joueur.direction_droite = False
						joueur.direction_gauche = False
						joueur.direction_monter = True
						joueur.image = personnage_haut1
						y_change = -2
						block_phy = True
					
			
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
					
		
		if event.type == KEYUP:
			if event.key == K_RIGHT:
				if joueur.block_mouv_cookie == False:
					joueur.sauv_animation = False
					if Map.get_at((joueur.rect.x+16,joueur.rect.y+33)) == jaune or Map.get_at((joueur.rect.x+11,joueur.rect.y+33)) == jaune:
						joueur.image = personnage_droite_arret
					if Map.get_at((joueur.rect.x+16,joueur.rect.y+35)) != jaune or Map.get_at((joueur.rect.x+11,joueur.rect.y+35)) != jaune:
						if direction_balle == "droite":
							if grimpe == False:
								joueur.image = personnage_droite1
					
					joueur.continuer_animation = False
					joueur.cpt = 0
					x_change = 0
			
			if event.key == K_LEFT:
				if joueur.block_mouv_cookie == False:
					joueur.sauv_animation = False
					if Map.get_at((joueur.rect.x+16,joueur.rect.y+33)) == jaune or Map.get_at((joueur.rect.x+11,joueur.rect.y+33)) == jaune:
						joueur.image = personnage_gauche_arret
					if Map.get_at((joueur.rect.x+16,joueur.rect.y+35)) != jaune or Map.get_at((joueur.rect.x+11,joueur.rect.y+35)) != jaune:
						if direction_balle == "gauche":
							if grimpe == False:
								joueur.image = personnage_gauche1
					
					joueur.continuer_animation = False
					joueur.cpt = 0
					x_change = 0
			
			if event.key == K_UP:
				if joueur.block_mouv_cookie == False:
					if grimpe:
						joueur.continuer_animation = False
						joueur.direction_monter = False
						y_change = 0
						block_phy = False
						joueur.cpt = 0
					
	
	if joueur.rect.x < bot.rect.x and joueur.rect.x > bot.rect.x - 100:
		if joueur.rect.y < bot.rect.y and joueur.rect.y > bot.rect.y -200:
			if adopter == False:
				x_change_bot = -1
				action_bot_choix = 9999999
				bot.direct_bot_gauche = True
				bot.direct_bot_droite = False
				bot.continuer_animation_bot = True
				
					
	
	if joueur.rect.x > bot.rect.x and joueur.rect.x < bot.rect.x + 100:
		if joueur.rect.y < bot.rect.y and joueur.rect.y > bot.rect.y -200:
			if adopter == False:
				x_change_bot = 1
				action_bot_choix = 9999999
				bot.direct_bot_gauche = False
				bot.direct_bot_droite = True
				bot.continuer_animation_bot = True
				
	
	if joueur.rect.x > bot.rect.x - 20 and joueur.rect.x < bot.rect.x + 10:
		if joueur.rect.y < bot.rect.y and joueur.rect.y > bot.rect.y -200:
			x_change_bot = 0
			bot.continuer_animation_bot = False
			action_bot_choix = 9999999
			if joueur.block_mouv_cookie == True:
				if adopter == False:
					nb_cookie -= 1
				adopter = True
	
	
	
	if pygame.sprite.groupcollide(grp_j,grp_b,False,False):
		if joueur.block_mouv_cookie == False:
			if adopter == False:
				if cpt_degat > 0:
					cpt_degat -= 1
				if cpt_degat == 0:
					if nb_vie_j > 0:
						nb_vie_j -= 1
					cpt_degat = 50
					continuer_regeneration = False
	else:
		cpt_degat = 0
		if nb_vie_j < 4:
			continuer_regeneration = True
	
	
	if continuer_regeneration:
		if cpt_regeneration == 100 or cpt_regeneration < 100:
			cpt_regeneration -= 1
		if cpt_regeneration == 0:
			cpt_regeneration = 100
			if nb_vie_j < 4:
				nb_vie_j += 1
	else:
		cpt_regeneration = 100
	
	
	if adopter:
		if joueur.rect.x > bot.rect.x and joueur.rect.x < bot.rect.x + 1000:
			if joueur.rect.y < bot.rect.y and joueur.rect.y > bot.rect.y -200:
				x_change_bot = 1
				bot.continuer_animation_bot = True
				action_bot_choix = 999999
				bot.direct_bot_droite = True
				bot.direct_bot_gauche = False
	
	
	if adopter:
		if joueur.rect.x < bot.rect.x and joueur.rect.x > bot.rect.x - 1000:
			if joueur.rect.y < bot.rect.y and joueur.rect.y > bot.rect.y -200:
				x_change_bot = -1
				action_bot_choix = 9999999
				bot.direct_bot_gauche = True
				bot.direct_bot_droite = False
				bot.continuer_animation_bot = True
		
		
	if adopter:
		if joueur.rect.x > bot.rect.x - 20 and joueur.rect.x < bot.rect.x + 10:
			if joueur.rect.y < bot.rect.y and joueur.rect.y > bot.rect.y -200:
				x_change_bot = 0
				bot.continuer_animation_bot = False
				action_bot_choix = 9999999
	
	
	if action_bot_choix == 2:
		if block_tourner_droit == False:
			if block_marche_bot == 0:
				bot.direct_bot_droite = True
				bot.direct_bot_gauche = False
				block_tourner_gauche = True
				bot.continuer_animation_bot = True
				x_change_bot = 1
				sauv_derniere_direct_bot = "droite"
	
	elif action_bot_choix == 1 or action_bot_choix == 5 or action_bot_choix == 38 or action_bot_choix == 29:
		if block_tourner_gauche == False:
			if block_marche_bot == 0:
				bot.direct_bot_gauche = True
				block_tourner_droite = True
				bot.direct_bot_droite = False
				bot.continuer_animation_bot = True
				sauv_derniere_direct_bot = "gauche"
				x_change_bot = -1
	
	elif action_bot_choix == 10:
		if block_marche_bot == 0:
			x_change_bot = 0
			bot.continuer_animation_bot = False
			
			
			if sauv_derniere_direct_bot == "gauche":
				block_tourner_droite = False
			
			if sauv_derniere_direct_bot == "droite":
				block_tourner_gauche = False
			
			block_marche_bot = 0
			block_marche_bot = randrange(20,200)
	
	
	if block_marche_bot > 0 :
		block_marche_bot -= 1
	
	
	if bot.rect.y > 470:
		y_change_bot = 0
		bot.continuer_animation_bot = False
		bot.rect.y -= 3
	
	if bot.rect.x < 38:
		x_change_bot = 0
		bot.continuer_animation_bot = False
		bot.rect.x += 3
	
	if bot.rect.x > 750:
		x_change_bot = 0
		bot.continuer_animation_bot = False
		bot.rect.x -= 3
	
	
	bot.rect.x += x_change_bot
	bot.rect.y += y_change_bot
	
	
	if joueur.block_mouv_cookie:
		if cpt_block_mouv_cookie == 0 or cpt_block_mouv_cookie > 0:
			cpt_block_mouv_cookie += 1
		if cpt_block_mouv_cookie == 45:
			joueur.block_mouv_cookie = False
			cpt_block_mouv_cookie = 0
			joueur.continuer_animation = False
			if joueur.direction_gauche == True:
				joueur.image = personnage_gauche_arret
			if joueur.direction_droite == True:
				joueur.image = personnage_droite_arret
	
	#~ if window.get_at((joueur.rect.x+28,joueur.rect.y+10)) == bleu or window.get_at((joueur.rect.x+4,joueur.rect.y+10)) == bleu:
		#~ grimpe = True
		#~ saut = False
	#~ else:
		#~ grimpe = False
	
	if Map.get_at((joueur.rect.x+28,joueur.rect.y+10)) != bleu or Map.get_at((joueur.rect.x+4,joueur.rect.y+10)) != bleu:
		block_phy = False
		grimpe = False
		joueur.direction_monter = False
		
	
	if block_phy == False:
		if saut == False:
			if Map.get_at((joueur.rect.x+16,joueur.rect.y+35)) != jaune or Map.get_at((joueur.rect.x+11,joueur.rect.y+35)) != jaune:
				cpt_phy += 1
				if cpt_phy > 7 and cpt_phy < 11:
					y_change += 1
				if cpt_phy > 10:
					y_change += 1
	
	if grimpe == False:
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
			if direction_balle == "gauche":
				joueur.direction_gauche = True
				joueur.direction_droite = False
				joueur.image = personnage_gauche_arret
			if direction_balle == "droite":
				joueur.direction_droite = True
				joueur.direction_gauche = False
				joueur.image = personnage_droite_arret
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
		joueur.rect.x += 2
		
	if Map.get_at((x_pied_j+28,y_pied_j+5)) == jaune or Map.get_at((x_pied_j+28,y_pied_j+10)) == jaune or Map.get_at((x_pied_j+22,y_pied_j+20)) == jaune:
		joueur.rect.x -= 2
		
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
	pygame.draw.rect(Map, bleu,(538,150,60,290))
	pygame.draw.rect(Map, jaune,(450,285,90,13))
	pygame.draw.rect(Map, jaune,(595,253,140,13))
	pygame.draw.rect(Map, jaune,(595,316,55,13))
	#~ pygame.draw.rect(Map, jaune,(150,425,10,100))
	grp_j.draw(window)
	grp_b.draw(window)
	sol_deco()
	
	if tire:
		pygame.draw.rect(window, jaune,( x_balle, y_balle , 10 ,5))
	
	if nb_vie_j == 4:
		window.blit(coeur,(10,10))
		window.blit(coeur,(44,10))
		window.blit(coeur,(78,10))
		window.blit(coeur,(110,10))
	if nb_vie_j == 3:
		window.blit(coeur,(10,10))
		window.blit(coeur,(44,10))
		window.blit(coeur,(78,10))
	if nb_vie_j == 2:
		window.blit(coeur,(10,10))
		window.blit(coeur,(44,10))
	if nb_vie_j == 1:
		window.blit(coeur,(10,10))
	#~ if nb_vie_j == 0:
		#~ print("vous êtes bientôt mort")

	window.blit(cookie,(10,67))
	arial = pygame.font.SysFont("arial",30)
	affiche = arial.render("X "+str(nb_cookie),True,black)
	window.blit(affiche,(65,75))
	
	bounce_obstacle1.update()
	bounce_obstacle2.update()
	bot.update()
	joueur.update()
	pygame.display.update()
	clock.tick(60)
	

