import time
import getch

startGame = False

def begin(distance):
	while (distance < 50):

		beginTime = time.time()
		fst =getch.getch()
		if fst == 'z':
			snd = getch.getch()
			if snd == 'x':
				distance += 1
				if distance == 25:
					print("***** You're halfways there! ******")
				if distance == 50:
					totalTime = time.time()-beginTime
					print("Score {}".format((totalTime*100)))


if __name__ == '__main__':
	name = input("Enter your name: ")
	print ("Hello {}".format(name) + ".  In order to play the game you must press z and x alternating. ")
	
	while(startGame == False):
		hold = input("Input zx to start: ")
		if(hold == "zx"):
			startGame=True
			distance = 0
			begin(distance)