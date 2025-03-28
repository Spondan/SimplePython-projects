import pygame
pygame.init()
# Initialize Pygame
screen_width=800
screen_height=600

screen=pygame.display.set_mode((screen_width,screen_height))
player=pygame.Rect((300,250,50,50))

run=True
while run:

    screen.fill((0,0,0))  #fills the screen with black to not leave red back

    pygame.draw.rect(screen,(255,0,0),player)   #draws a rect in red
    
    key=pygame.key.get_pressed()
    if key[pygame.K_a] == True: #left
        player.move_ip(-1,0)
    elif key[pygame.K_d]==True: #right
        player.move_ip(1,0)
    elif key[pygame.K_w]==True: #up
        player.move_ip(0,-1)
    elif key[pygame.K_s]==True:  #down
        player.move_ip(0,1)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    pygame.display.update()

pygame.quit()