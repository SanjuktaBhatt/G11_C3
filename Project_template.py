import pygame
pygame.init() 
WHITE = (255,255,255)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (255,0,0)
ORANGE = (255,100,0)
YELLOW = (255,255,0)
size = (400, 400)

#Player rectangle object details
player=pygame.Rect(0,200,20,20)
playerx=1

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Project C3")
carryOn = True
while carryOn:
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
      carryOn = False             
  screen.fill(YELLOW)
  
  #Check if user pressed any key(i.e. check if even type is KEYDOWN)
  
    #Check if user pressed right key(i.e. check if key is K_RIGHT)
    
      #Check if player is within right boundary(i.e. check x coordinate is less than 380)
      
        #increase player x coordinate
        
    #Check if user pressed right key(i.e. check if key is K_RIGHT)
    
      #Check if player is within right boundary(i.e. check x coordinate is greater than 0)
      
        #decrease player x coordinate
       
  
  pygame.draw.rect(screen,LIGHTBLUE,player)
  pygame.display.flip()
pygame.quit()
