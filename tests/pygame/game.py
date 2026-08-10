import pygame #this is an example of an game, we import the library
from sys import exit #useful for my game

pygame.init() #inits the pytgame
screen = pygame.display.set_mode((800, 400)) #we define the height-width relationship on the window, is (width, height)
clock = pygame.time.Clock() #we insert our clock to manage our game loop
pygame.display.set_caption('idk') #we define the title or caption of our window
p_surface = pygame.Surface((100,200)) #it creates a surface, the surface is techincally what u see on the game, it's the game window 
player_gravity = 0
#now, let's display images

#we'll use an convert function ()

superficie_cielo = pygame.image.load("tests/pygame/graphics/Sky.png").convert() #we give pygame an image "sky.png" to load on the screen
superficie_suelo = pygame.image.load("tests/pygame/graphics/ground.png").convert() #also an image "ground.png" to load on the window
caracol_superficie = pygame.image.load("tests/pygame/graphics/snail1.png").convert_alpha() #we also create an variable to load the image of the snail
player_superficie = pygame.image.load("tests/pygame/graphics/player_walk_1.png")
caracol_x = 600 #we create a varaible for the axe x for the snail

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
score = text_font.render('This is an test mothafucka', 50, 'Blue') #and now we render the font, we give the tirle of the font. the length, and the color of it lol

score_rect = score.get_rect(center= (400, 50 )) #now we center the score lol

# and now we create the variable, game_active, it will be a boolean value, if it's False, the game will end

game_active = True

#the "main" code:      

while True: #this will be executed until we quit the window
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit() #we quit the game  
            exit() #we exit the window 
        if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
            if player_rect.collidepoint(event.pos): print('collision')
            player_gravity -= 20            
        if event.type == pygame.KEYDOWN and player_rect.bottom >= 300:
            if event.key == pygame.K_SPACE:
                 player_gravity -= 20
                 #print('jump')          
        #if event.type == pygame.KEYUP:
                    #print('key up')  
    if game_active:
       screen.blit(superficie_cielo, (0,0))   #this will be at top, X: 0, Y:0, it will be at the top of the window
       screen.blit(superficie_suelo, (0,300))  #meanwhile, this will be at the other end of the window, that means, it'll be at the bottom lol
       pygame.draw.rect(screen, 'Pink', score_rect, 100)  #we draw a rectangle
       pygame.draw.line(screen, 'Gold', (0, 0), pygame.mouse.get_pos(), 10)
       #pygame.draw.ellipse(screen, 'Red', pygame.Rect(50, 200, 100, 100)) - we draw a ellipse
       screen.blit(score, score_rect) #i changed the name of the variable 

       caracol_rect.x -= 2 #now, on the game loop, he will move 2 to the left
       if caracol_rect.right < 0: caracol_rect.left = 800
       screen.blit(caracol_superficie, caracol_rect) #now we blit the snail to the window

       player_gravity += 1
       screen.blit(player_superficie, player_rect)
       player_rect.y += player_gravity
       if player_rect.bottom >= 300: player_rect.bottom = 300
    #player_rect.left += 1

       if caracol_rect.colliderect(player_rect): #in case the player and the snail collides on the window, it will "unable" the True boolean value, and the game will end or freeeze to create the game_over state 
         game_active = False
    else:
         screen.fill('Red')

       #if caracol_x < -100: caracol_x = 800

    #now we're gonna use collisions

    #player_rect.colliderect(caracol_rect) #is a method or function used to know if two rectangles are intercepted or touching on the scrren

    pygame.display.update() #updates EVERYTHING (in 60fps btw), but? we can create an statement? YES, WE CAN,
    clock.tick(60) #the loop tells pygame that the game or frame loop "it cant'be faster than 60 times per second, or 17 milliseconds"
    #print("hello :3") #this is perfect, u can use it to see how the game loop works



























# EXTRA:
#most common event types: QUIT, ACTIVEEVENT, KEYDOWN, KEYUP, MOUSEMOTION, MOUSEBUTTONUP, VIDEORESIZE, VIDEOEXPOSE, USEREVENT

#pd: todos estos fondos no son míos, son de Clear Code, pueden encontrarlo en youtube, solo busquenlo en Github
#pd2: obviamente haré otro juego,y daré más documentación, aunque no se sorprendan si prefiero primero terminar el proyecto.



