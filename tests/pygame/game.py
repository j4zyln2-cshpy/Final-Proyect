import pygame #this is an example of an game, we import the library
from sys import exit #useful for my game

pygame.init() #inits the pytgame
screen = pygame.display.set_mode((800, 400)) #we define the height-width relationship on the window, is (width, height)
clock = pygame.time.Clock() #we insert our clock to manage our game loop
pygame.display.set_caption('idk') #we define the title or caption of our window
p_surface = pygame.Surface((100,200)) #it creates a surface, the surface is techincally what u see on the game, it's the game window 

#now, let's display images

superficie_cielo = pygame.image.load("tests/pygame/graphics/Sky.png") #we give pygame an image "sky.png" to load on the screen
superficie_suelo = pygame.image.load("tests/pygame/graphics/ground.png") #also an image "ground.png" to load on the window

#we can blit fonts? YES, WE CAN, BUT HOW?

text_font = pygame.font.Font('tests/pygame/font/Pixeltype.ttf', 50) #first we call the font, we declare one font at specific, and we declare also the length of it
text_font_surface = text_font.render('This is an test mothafucka', 50, 'Blue') #and now we render the font, we give the tirle of the font. the length, and the color of it lol

#the "main" code:

while True: #this will be executed until we quit the window
    for event in pygame.event.get(): 
         if event.type == pygame.QUIT:
            pygame.quit() #we quit the game  
            exit() #we exit the window 
    screen.blit(superficie_cielo, (0,0))   #this will be at top, X: 0, Y:0, it will be at the top of the window
    screen.blit(superficie_suelo, (0,300))  #meanwhile, this will be at the other end of the window, that means, it'll be at the bottom lol
    screen.blit(text_font_surface, (250,15))
    pygame.display.update() #updates EVERYTHING (in 60fps btw)
    clock.tick(60) #the loop tells pygame that the game or frame loop "it cant'be faster than 60 times per second, or 17 milliseconds"
    #print("hello :3") #this is perfect, u can use it to see how the game loop works



#most common event types: QUIT, ACTIVEEVENT, KEYDOWN, KEYUP, MOUSEMOTION, MOUSEBUTTONUP, VIDEORESIZE, VIDEOEXPOSE, USEREVENT

#pd: todos estos fondos no son míos, son de Clear Code, solo busquenlo en Github