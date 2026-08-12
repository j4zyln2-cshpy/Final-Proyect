import pygame #this is an example of an game, we import the library
from sys import exit #useful for my game
from random import randint, choice


pygame.init() #inits the pytgame
screen = pygame.display.set_mode((800,400),pygame.RESIZABLE)#we define the height-width relationship on the window, is (width, height)
clock = pygame.time.Clock() #we insert our clock to manage our game loop
pygame.display.set_caption('idk') #we define the title or caption of our window
p_surface = pygame.Surface((100,200)) #it creates a surface, the surface is techincally what u see on the game, it's the game window 
player_gravity = 0
start_time = 0
score = 0
bg_music = pygame.mixer.Sound("tests/pygame/sounds/music.mp3")
bg_music.play(loops = -1)
bg_music.set_volume(0.5)
#now, let's display images

#we'll use an convert function ()

superficie_cielo = pygame.image.load("tests/pygame/graphics/Sky.png").convert() #we give pygame an image "sky.png" to load on the screen
superficie_suelo = pygame.image.load("tests/pygame/graphics/ground.png").convert() #also an image "ground.png" to load on the window
caracol_1 = pygame.image.load("tests/pygame/graphics/snail1.png").convert_alpha() #we also create an variable to load the image of the snail
caracol_2 = pygame.image.load("tests/pygame/graphics/snail2.png").convert_alpha()
caracol_frames = [caracol_1, caracol_2]
caracol_frame_index = 0
caracol_superficie = caracol_frames[caracol_frame_index]
player_walk_1 = pygame.image.load("tests/pygame/graphics/player_walk_1.png").convert_alpha()
player_walk_2 = pygame.image.load("tests/pygame/graphics/player_walk_2.png").convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_superficie = player_walk[player_index]
player_jump = pygame.image.load("tests/pygame/graphics/jump.png").convert_alpha()
player_stand = pygame.image.load("tests/pygame/graphics/player_stand.png").convert_alpha()
fly1 = pygame.image.load("tests/pygame/graphics/Fly1.png")
fly2 = pygame.image.load("tests/pygame/graphics/Fly2.png")
fly_frames = [fly1, fly2]
fly_frame_index = 0
fly_surface = fly_frames[fly_frame_index]

player_stand= pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

# pther variables
caracol_x = 600 #we create a varaible for the axe x for the snail
current_time = int(pygame.time.get_ticks() / 1000) - start_time # return milliseconds

#extra: 
#-- Convert(): Use this for opaque images (like background)
# -- Convert_alpha(): This is for transparent images (like character sprites). Preserves the semi-transparent pixels

#now, we'll use a get_rect function, for example:

# polla = polla.get_rect(bottomleft = (4949, 4i)) (obviouslt this is wrong but it's an example)

#extra : get_rect(): it creates an "invisible box" around an image or an text, it's the same size as our sprites :3, it also gives us permission to change our x/y coords 
# u only have to give him the dir of ur character and the x / y coords

caracol_rect = caracol_superficie.get_rect(bottomright= (600, 300))
player_rect = player_superficie.get_rect(midbottom= (80, 300))

#we can blit fonts? YES, WE CAN, BUT HOW?

text_font = pygame.font.Font('tests/pygame/font/Pixeltype.ttf', 50) #first we call the font, we declare one font at specific, and we declare also the length of it
#score = text_font.render(f'Score: {current_time}', False, (64,64, 64)) #and now we render the font, we give the tirle of the font. the length, and the color of it lol

#score_rect = score.get_rect(center= (400, 50 )) #now we center the score lol

# and now we create the variable, game_active, it will be a boolean value, if it's False, the game will end

game_active = False 

# the game_name variable

game_title = text_font.render('mis dos bolas', False, (111, 196, 169))
game_title_rect = game_title.get_rect(center = (400, 60))
game_message = text_font.render('Press space to jump', False, (111, 196, 169))
game_message_rect = game_message.get_rect(center = (400, 320))

#function for display_score():

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score = text_font.render(f'Score: {current_time}', False, (64,64, 64))
    score_rect = score.get_rect(center= (400, 50 )) 
    screen.blit(score, score_rect)
    return current_time


# obstacle_timer

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

obstacle_rect_list = []

snail_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_timer, 500)

fly_timer = pygame.USEREVENT + 1
pygame.time.set_timer(fly_timer, 200)

#extra: pygame.USEREVENT: is a constant used to define custom, user-defined events in Pygame (permite crear eventos propios en lugar de solo usar los predetermindos), it could be used to create warnings and program some few extra things to the game lol

# and now we create the function for the obstacle movement

def obstacle_movement(obstacle_list):
     if obstacle_list:
          for obstacle_rect in obstacle_list:
               obstacle_rect.x -= 5 
               if obstacle_rect.bottom == 300:
                   screen.blit(caracol_superficie, obstacle_rect)
               else:
                   screen.blit(fly_surface, obstacle_rect)
          return obstacle_list
     else: return []

# another functions for the collisions


def collisions(player,obstacles):
	if obstacles:
		for obstacle_rect in obstacles:
			if player.colliderect(obstacle_rect): return False
	return True

def collision_sprite():
	if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
		obstacle_group.empty()
		return False
	else: return True

# another function for the player_movement

def player_animation():
    global player_superficie, player_index

    if player_rect.bottom < 300:
        player_superficie = player_jump
    else:
        player_index += 0.1
        if player_index > len(player_walk): player_index = 0 
        player_superficie = player_walk[int(player_index)]


# as the final things to set_up, we're gonna add a class Player
class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		player_walk_1 = pygame.image.load('tests/pygame/graphics/player_walk_1.png').convert_alpha()
		player_walk_2 = pygame.image.load('tests/pygame/graphics/player_walk_2.png').convert_alpha()
		self.player_walk = [player_walk_1,player_walk_2]
		self.player_index = 0
		self.player_jump = pygame.image.load('tests/pygame/graphics/jump.png').convert_alpha()

		self.image = self.player_walk[self.player_index]
		self.rect = self.image.get_rect(midbottom = (80,300))
		self.gravity = 0

		self.jump_sound = pygame.mixer.Sound('tests/pygame/sounds/jump.wav')
		self.jump_sound.set_volume(0.5)

	def player_input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
			self.gravity = -20
			self.jump_sound.play()

	def apply_gravity(self):
		self.gravity += 1
		self.rect.y += self.gravity
		if self.rect.bottom >= 300:
			self.rect.bottom = 300

	def animation_state(self):
		if self.rect.bottom < 300: 
			self.image = self.player_jump
		else:
			self.player_index += 0.1
			if self.player_index >= len(self.player_walk):self.player_index = 0
			self.image = self.player_walk[int(self.player_index)]

	def update(self):
		self.player_input()
		self.apply_gravity()
		self.animation_state()

player = pygame.sprite.GroupSingle()
player.add(Player())

# and a class obstacle

class Obstacle(pygame.sprite.Sprite):
	def __init__(self,type):
		super().__init__()
		
		if type == 'fly':
			fly_1 = pygame.image.load('tests/pygame/graphics/fly1.png').convert_alpha()
			fly_2 = pygame.image.load('tests/pygame/graphics/fly2.png').convert_alpha()
			self.frames = [fly_1,fly_2]
			y_pos = 210
		else:
			snail_1 = pygame.image.load('tests/pygame/graphics/snail1.png').convert_alpha()
			snail_2 = pygame.image.load('tests/pygame/graphics/snail2.png').convert_alpha()
			self.frames = [snail_1,snail_2]
			y_pos  = 300

		self.animation_index = 0
		self.image = self.frames[self.animation_index]
		self.rect = self.image.get_rect(midbottom = (randint(900, 1100),y_pos))

	def animation_state(self):
		self.animation_index += 0.1 
		if self.animation_index >= len(self.frames): self.animation_index = 0
		self.image = self.frames[int(self.animation_index)]

	def update(self):
		self.animation_state()
		self.rect.x -= 6
		self.destroy()

	def destroy(self):
		if self.rect.x <= -100: 
			self.kill()

obstacle_group = pygame.sprite.Group()

#the "main" code:      

while True: #this will be executed until we quit the window
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit() #we quit the game  
            exit() #we exit the window 
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
               if player_rect.collidepoint(event.pos):
                     player_gravity -= 20            
            if event.type == pygame.KEYDOWN and player_rect.bottom >= 300:
                  if event.key == pygame.K_SPACE:
                         player_gravity -= 30
                 #print('jump')          
            #if event.type == pygame.KEYUP:
                    #print('key up')             
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect = 800
                start_time = int(pygame.time.get_ticks() / 1000)

        if game_active:
          if event.type == obstacle_timer and game_active:
            obstacle_group.add(Obstacle(choice(['fly','snail'])))
            if randint(0,2):
                obstacle_rect_list.append(caracol_superficie.get_rect(bottomright = (randint(900, 1100), 300)))
            else:
                obstacle_rect_list.append(fly_surface.get_rect(bottomright = (randint(900, 1100), 210)))

          if event.type == snail_timer:
              if caracol_frame_index == 0: caracol_frame_index = 1
              else:  caracol_frame_index = 0
              caracol_superficie = caracol_frames[caracol_frame_index]

          if event.type == fly_timer:
                        if fly_frame_index == 0: fly_frame_index = 1
                        else:  fly_frame_index = 0
                        fly_surface = fly_frames[fly_frame_index]
              
    if game_active:
       screen.blit(superficie_cielo, (0,0))   #this will be at top, X: 0, Y:0, it will be at the top of the window
       screen.blit(superficie_suelo, (0,300))  #meanwhile, this will be at the other end of the window, that means, it'll be at the bottom lol
       #we draw a rectangle
       # pygame.draw.line(screen, 'Gold', (0, 0), pygame.mouse.get_pos(), 10), it was funny :/
       #pygame.draw.ellipse(screen, 'Red', pygame.Rect(50, 200, 100, 100)) - we draw a ellipse
       score = display_score() #i changed the value of the variable 

       #caracol_rect.x -= 2 #now, on the game loop, he will move 2 to the left
       #if caracol_rect.right < 0: caracol_rect.left = 800
       #screen.blit(caracol_superficie, caracol_rect) #now we blit the snail to the window

      # player_gravity += 1
       #player_rect.y += player_gravity
       #if player_rect.bottom >= 300: player_rect.bottom = 300
       #player_animation()
      # screen.blit(player_superficie, player_rect)
       player.draw(screen)
       player.update()

       obstacle_group.draw(screen)
       obstacle_group.update()
       #player_rect.left += 1

       # obstacle_rect_list = obstacle_movement(obstacle_rect_list) #the obstacles movement
       game_active = collision_sprite()

       #if caracol_rect.colliderect(player_rect): #in case the player and the snail collides on the window, it will "unable" the True boolean value, and the game will end or freeeze to create the game_over state 
         #game_active = False
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0
        score_message = text_font.render(f'Score: {score}', False, (111, 196, 169))
        score_message_rect = score_message.get_rect(center = (400, 330))
        screen.blit(game_title, game_title_rect)


        if score == 0: screen.blit(game_message, game_message_rect)
        else: screen.blit(score_message, score_message_rect)
 

          #if caracol_x < -100: caracol_x = 800



    pygame.display.update() #updates EVERYTHING (in 60fps btw), but? we can create an statement? YES, WE CAN,
    clock.tick(60) #the loop tells pygame that the game or frame loop "it cant'be faster than 60 times per second, or 17 milliseconds"
    #print("hello :3") #this is perfect, u can use it to see how the game loop works


   #now, h0w we're gonna use collisions?
   #problem: too much enemies

    #player_rect.colliderect(caracol_rect) #is a method or function used to know if two rectangles are intercepted or touching on the scrren





















# EXTRA:
#most common event types: QUIT, ACTIVEEVENT, KEYDOWN, KEYUP, MOUSEMOTION, MOUSEBUTTONUP, VIDEORESIZE, VIDEOEXPOSE, USEREVENT
#pygame.transform:
# -- pygame module to transform:

        #pygame.transform.flip: flip vertically and horizontally
        #pygame.transform.scale: resize to new resolution
        #pygame.transform.rotate: rotate an image to an specific angle
        #pygame.transform.rotozoom: filtered scale and rotation
        #pygame.transform.scale2x: image doubler
        #pygame.transform.smooth_scale: scale an surface to an arbitrary size smoothly
        #pygame.transform.get_smoothscale_backend: return smoothscale file in case: GENERIC, MMX, SSE
        #pygame.transform.set_smoothscale_backend: set smoothscale file in case: GENERIC, MMX, SSE
        #pygame.transform.chop: gets an copy of an image with an interior area removed
        #pygame.transform.taplacian: find edges in a surface
        #pygame.transform.average_surface: finds the average surface of many surfaces
        #pygame.transform.average_color: finds the average color of a surface
        #pygame.transform.threshold: finds which, and how many pixels in a surface are without a threshold of search_surf or search_color

#pd: todos estos fondos no son míos, son de Clear Code, pueden encontrarlo en youtube, o tan solo busquenlo en Github
#pd2: obviamente haré otro juego,y daré más documentación, aunque no se sorprendan si prefiero primero terminar el proyecto.