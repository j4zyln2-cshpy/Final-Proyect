import os

screen_width = 800 #ancho de pantalla
scrrehn_height = 40
fps = 60
game_title = "Kingdom Defene 1D"

ground_y_position = 300
tower_x_position = 700
position_spawn_x = 0

background_color = (40, 50, 60)
text_color = (255, 255, 255)
colorcito_orito = (255, 215, 0) #:3

dir_base =  os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
dir_assets =  os.path.join(dir_base, "assets")
dir_images =  os.path.join(dir_assets, "images")
dir_sounds = os.path.join(dir_assets, "sounds")

#tomorrow i'll upload this with the dirdatabase