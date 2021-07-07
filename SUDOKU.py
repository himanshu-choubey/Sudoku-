import sys, pygame
import os
pygame.font.init()

WIDTH, HEIGHT = 450, 450
NO_FONT = pygame.font.SysFont('comicsans', 40)
FPS = 30
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255,255,255)
YELLOW = (255, 255, 0)
GREEN = (0,255,0)
RED = (255,0,0)
BLACK = (0,0,0)
ROWS = 9
COLS = 9
BG_IMG = pygame.image.load(os.path.join('Assets', 'bg.jpg'))
HL_IMG = pygame.image.load(os.path.join('Assets', 'hL.png'))
CORRECT_IMG = pygame.image.load(os.path.join('Assets', 'green.png'))
INCORRECT_IMG = pygame.image.load(os.path.join('Assets', 'red.png'))
BG = pygame.transform.scale(BG_IMG, (HEIGHT, HEIGHT))
HL = pygame.transform.scale(HL_IMG, (45,45))
CORRECT = pygame.transform.scale(CORRECT_IMG, (45,45))
INCORRECT = pygame.transform.scale(INCORRECT_IMG, (45,45))
pygame.display.set_caption("Sudoku!")
WIN.fill(WHITE)

def empty(ques):
	for i in range(9):
		for j in range(9):
			if(not ques[i][j]):
				return [i, j];
	return None

def solve(ques):
	find = empty(ques)
	if not find:
		return True

	else:
		row, col = find[0],find[1]

	for i in range(1, 10):
		if get_ans(row*49, col*49, i, ques):
			ques[row][col] = i

			if solve(ques):
				return True

			ques[row][col] = 0

	return False




def check_no(ques):
	for i in range(9):
		ksi  = {}
		for j in range(9):
			if(ksi.get(ques[i][j]) and ques[i][j]!=0):
				return False
			else:
				ksi[ques[i][j]] = 1
	for i in range(9):
		ksi  = {}
		for j in range(9):
			if(ksi.get(ques[j][i]) and ques[j][i]!=0):
				return False
			else:
				ksi[ques[j][i]] = 1
	for i in range(0,9,3):
		for j in range(0,9,3):
			ksi = {}
			for k in range(i,i+3):
				for l in range(j, j+3):
					if(ksi.get(ques[k][l]) and ques[k][l]!=0):
						return False
					else:
						ksi[ques[k][l]] = 1
	return True


def get_ques():
	# ques = [[0 for i in range(COLS)] for j in range(ROWS)]
	return [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

def get_ans(i,j,n, ques):
	i = i//49
	j = j//49
	ques[i][j] = n
	if(check_no(ques)):
		return True
	else:
		ques[i][j] = 0
		return False
	



def draw_window(BG, highlight, the_color, pressed, ques):
																						
	WIN.blit(BG, (0,0))
	WIN.blit(HL, (highlight.x, highlight.y))
	# ques = get_ques()
	for i in range(9):
		for j in range(9):
			if ques[i][j]!=0:
				number = NO_FONT.render(str(ques[i][j]), 1, BLACK)
				WIN.blit(number, (j*49+14, i*49+14))
	new_no = NO_FONT.render(str(pressed), 1, GREEN)
	if(the_color and pressed!=0):
		new_no = NO_FONT.render(str(pressed), 1, GREEN)
		WIN.blit(new_no, (highlight.x+7, highlight.y+7))
	elif(pressed != 0):
		new_no = NO_FONT.render(str(pressed), 1, RED)
		WIN.blit(new_no, (highlight.x+7, highlight.y+7))
	# WIN.blit(new_no, (highlight.x, highlight.y))
				
	pygame.display.update()

def solve_draw(ques):
	for i in range(9):
		for j in range(9):
			if ques[i][j]!=0:
				number = NO_FONT.render(str(ques[i][j]), 1, BLACK)
				WIN.blit(number, (j*49+14, i*49+14))

	pygame.display.update()

def win_draw():
	WIN.fill(WHITE)
	win = NO_FONT.render("YAY!", 1, RED)
	WIN.blit(win, (0, 0))
	pygame.display.update()

def main():
	# highlight = pygame.Rect(0,0,100,100)
	run = True
	HLX = 7
	HLY = 7
	clock = pygame.time.Clock()
	the_color = False
	pressed = 0
	ques = get_ques()
	arr = get_ques()
	solve(arr)

	i=0
	j=0
	while(run):
		clock.tick(FPS)

		# if(not empty(ques)):
		# 	wins = NO_FONT.render("YOU WON", 1, BLACK)
		# 	WIN.blit(wins, (0,0))
		# 	pygame.time.delay(20)
		# 	run = False

		if(arr==ques):
			win_draw()

		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
			

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					solve(ques)
					solve_draw(ques)
					pygame.time.delay(3000)
					run  = False
				if event.key == pygame.K_LEFT and highlight.x>50:
					HLX-=49
				if event.key == pygame.K_RIGHT and highlight.x<352:
					HLX+=49
				if event.key == pygame.K_DOWN and highlight.y<352:
					HLY+=49
				if event.key == pygame.K_UP and highlight.y>50:
					HLY-=49
				if event.key == pygame.K_9:
					j = HLX//49
					i = HLY//49
					the_color = get_ans(HLY, HLX, 9, ques)
					pressed = 9
				if event.key == pygame.K_8:
					j = HLX//49
					i = HLY//49
					pressed = 8
					the_color = get_ans(HLY, HLX, 8, ques)
				if event.key == pygame.K_7:
					j = HLX//49
					i = HLY//49
					pressed = 7
					the_color = get_ans(HLY, HLX, 7, ques)
				if event.key == pygame.K_6:
					j = HLX//49
					i = HLY//49
					pressed = 6
					the_color = get_ans(HLY, HLX, 6, ques)
				if event.key == pygame.K_5:
					j = HLX//49
					i = HLY//49
					pressed = 5
					the_color = get_ans(HLY, HLX, 5, ques)
				if event.key == pygame.K_4:
					j = HLX//49
					i = HLY//49
					pressed = 4
					the_color = get_ans(HLY, HLX, 4, ques)
				if event.key == pygame.K_3:
					j = HLX//49
					i = HLY//49
					pressed = 3
					the_color = get_ans(HLY, HLX, 3, ques)
				if event.key == pygame.K_2:
					j = HLX//49
					i = HLY//49
					pressed = 2
					the_color = get_ans(HLY, HLX, 2, ques)
				if event.key == pygame.K_1:
					j = HLX//49
					i = HLY//49
					pressed = 1
					the_color = get_ans(HLY, HLX, 1, ques)
		highlight = pygame.Rect(HLX, HLY, 45, 45)

		

		draw_window(BG, highlight, the_color, pressed, ques)



	main()


if __name__=="__main__":
    main()
