import pygame
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

display_width = 800
display_hight = 600
gameDisplay = pygame.display.set_mode((display_width,display_hight))

pygame.display.set_caption('Snake')

icon = pygame.image.load('icon.png')	
pygame.display.set_icon(icon)

img = pygame.image.load('snakehead.png')
appleimg = pygame.image.load('apple.png') 

clock = pygame.time.Clock()

flag = True	
appleThikness = 30	
block_size = 20     
FPS = 15


smallfont = pygame.font.SysFont("comicsansms" , 25)   
medfont = pygame.font.SysFont("comicsansms" , 50) 
semimedfont = pygame.font.SysFont("comicsansms" , 35) 
largefont = pygame.font.SysFont("comicsansms" , 80) 

def pause():	
	
	paused = True
	
	message_to_screen("paused" , black , -100 ,size = "large")
	message_to_screen("press C to play or Q to Quit" , black , 25 , "semimed")	
	pygame.display.update()
	
	while paused:
		for event in pygame.event.get():
                	if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
				if event.key == pygame.K_c:
					paused = False
							
		
def game_intro():  
	
	global flag	
	flag = False	
	intro = True
	gameDisplay.fill(white)
	
	message_to_screen("Welcom to Slither" , green , -100 , "large")
	message_to_screen("The objective of the game is to eat red apples" , black , -30)
	message_to_screen("The more apple you eat the longer you get" , black , 10)
	message_to_screen("If you run in to your self or edges you die!" , black , 50)
	message_to_screen("press C to play, P to pause or Q to Quit" , black , 180 , "semimed")
			
	pygame.display.update()
	
	while intro:
		for event in pygame.event.get():
                	if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
				if event.key == pygame.K_c:
					intro = False

def snake(block_size, snakeList):
    if direction == 'right':        
        head = pygame.transform.rotate(img , 270)
    if direction == 'left':        
        head = pygame.transform.rotate(img , 90)
    if direction == 'up':        
        head = img
    if direction == 'down':        
        head = pygame.transform.rotate(img , 180)

    gameDisplay.blit(head , (snakeList[-1][0] , snakeList[-1][1]))  
    
    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay , green , [XnY[0],XnY[1],block_size,block_size])
   
   
def randAppleGen():
	randAppleX = random.randrange(0 , display_width-appleThikness)
	randAppleY = random.randrange(0 , display_hight-appleThikness)
	
	return randAppleX , randAppleY

def score(score):
	text = smallfont.render("score: " + str(score) , True , black)
	gameDisplay.blit(text , [0,0])   

def message_to_screen(msg,color,y_displace = 0,size = "small"):
    if size == "small":	
    	textSurface = smallfont.render(msg, True , color)
    if size == "med":	
    	textSurface = medfont.render(msg, True , color)
    if size == "large":	
    	textSurface = largefont.render(msg, True , color)
    if size == "semimed":	 			
    	textSurface = semimedfont.render(msg, True , color)
    textRect = textSurface.get_rect()
    textRect.center = (display_width / 2) , (display_hight / 2) + y_displace 
    gameDisplay.blit(textSurface , textRect)
    
	
def gameLoop():
    global direction      
    direction = 'right'      
    gameExit = False
    gameOver = False

    if flag:	
    	game_intro()  		

    lead_x = display_width/2
    lead_y = display_hight/2

    lead_x_change = 10      
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX , randAppleY = randAppleGen()	

    while not gameExit:

	if gameOver:	
		message_to_screen("Game over" , red , -50 , "large")  
		message_to_screen("Press C to play again or Q to Quit" , black , 50 , "semimed")
		pygame.display.update()
		
        while gameOver == True:	
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    gameOver = False
                    gameExit = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = False
                        gameExit = True
                    if event.key == pygame.K_c:
                        gameLoop()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 'left'          
                    lead_x_change = -block_size
                    lead_y_change = 0   
                elif event.key == pygame.K_RIGHT:
                    direction = 'right'         
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = 'up'            
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = 'down'          
                    lead_y_change = block_size
                    lead_x_change = 0
		elif event.key == pygame.K_p:	
			pause()

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_hight or lead_y < 0:
            gameOver = True

            
        lead_x += lead_x_change
        lead_y += lead_y_change

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if (len(snakeList) > snakeLength):
            del(snakeList[0])

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
                       
        gameDisplay.fill(white)


        gameDisplay.blit(appleimg , (randAppleX , randAppleY))
        snake(block_size ,snakeList)
        
        score(snakeLength-1)
        
        pygame.display.update()
        clock.tick(FPS)

        if lead_x > randAppleX and lead_x < randAppleX + appleThikness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + appleThikness:
            if lead_y > randAppleY and lead_y < randAppleY + appleThikness or lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + appleThikness:
                randAppleX , randAppleY = randAppleGen()
                snakeLength += 1


    pygame.quit()  
    quit()   

if __name__ == "__main__":
    gameLoop()
