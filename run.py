#SIMPLE OBJECT DODGE GAME IN PYTHON USING PYGAME
import sys, pygame, time, random
pygame.init()

################## GLOBAL ##################
size = width, height = 1250, 700
speed = [2,2]
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Racing Game')
clock = pygame.time.Clock()
carImg = pygame.image.load('car.jpg')
##############################################

def myrand(x, y):
	#GENERATE NUMBER IN RANGE [x,y]
	return random.randrange(x,y)	
def car(x,y) :
	screen.blit(carImg,(x,y))
def text_objects(text, font, clr) :
	textSurface = font.render(text, True, clr)
	return textSurface, textSurface.get_rect()
def message_display(text, x, y, sz, clr) :
	text_ = pygame.font.Font('freesansbold.ttf',sz)
	textSurface, textRect = text_objects(text, text_,clr)
	textRect.center = (x, y)
	screen.blit(textSurface, textRect)
	pygame.display.update()
def things(thingx, thingy, thingw, thingh, color) :
	pygame.draw.rect(screen,color, [thingx, thingy, thingw, thingh])
def crash(block_start_x, block_start_y, block_width, x, y, car_width) :
	if block_start_y >= height * 0.8 and block_start_x >= x and block_start_x <= x + car_width :
		return True
	elif block_start_y >= height * 0.8 and block_start_x + block_width >= x and block_start_x + block_width <= x + car_width :
		return True
	return False	

def game_loop() :
	exit_game = False
	decide = False
	game_score = 0
	car_width = 132
	block_width = 100
	block_height = 100
	block_start_x = random.randrange(0,width-block_width)
	block_start_y = -600 - random.randrange(100,300)
	block_speed = 5
	x = width * 0.45
	y = height * 0.8
	x_change = 0
	while not exit_game :
		for event in pygame.event.get() :
			if event.type == pygame.QUIT : #'X'
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_LEFT :
					x_change -= 20
					#message_display('LEFT ;O', x * 0.45, y * 0.5, red)
				
				elif event.key == pygame.K_RIGHT :
					x_change += 20
					#message_display('RIGHT :X', x * 0.45, y * 0.5, red)
					
			if event.type == pygame.KEYUP :
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
					x_change = 0
			x += x_change
			#BELOW INDENT PART WAS FOR FIXED WIDTH TRACK
			#if x > 0.6 * width :
			#	x = 0.6 * width
			#	x_change = 0
			#elif x < 0.3 * width :
			#	x = 0.3 * width
			#	x_change = 0
			if x > width - car_width :
				x = width - car_width
				x_change = 0
			elif x < 0 :
				x = 0
				x_change = 0
		
		screen.fill(black)
		car(x,y)
		things(block_start_x, block_start_y, block_width, block_height, blue)
		message_display('SCORE : ' + `game_score`,width * 0.1, 20, 15, red)
		pygame.display.update()
		if crash(block_start_x, block_start_y, block_width, x, y, car_width) :
			#message_display(text, x, y, sz, clr)
			message_display('CRASHED', width * 0.45, height * 0.5,115, red)
			time.sleep(1)
			exit_game = True
		block_start_y += block_speed
		if block_start_y > height :
			block_start_y = -500
			block_start_x = random.randrange(0,width-block_width)
			game_score += 1
		#clock.tick(60)
	while not decide :
		screen.fill((myrand(0,255),myrand(0,255),myrand(0,255)))
		message_display('PRESS <- FOR NEW GAME ELSE PRESS ANY KEY TO EXIT', width * 0.5, height * 0.5, 30, (myrand(0,255),myrand(0,255),myrand(0,255)))
		pygame.display.update()
		for event in pygame.event.get() :
			if event.type == pygame.QUIT : #'X'
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_LEFT :
					game_loop()
					decide = True
				else  :
					decide = True
		time.sleep(0.3)

game_loop()
pygame.quit()
