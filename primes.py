GOODVALS = []

def isPrime(primeOrNot):
	temp = False

	for x in range(2,(primeOrNot//2)+1):
		if(primeOrNot%x == 0):
			temp = True
			break
		else:
			temp = False

	if(temp == False):
		GOODVALS.append(primeOrNot)

	temp = False

if __name__ == '__main__':
	for x in range(2,40):
		isPrime(x)
		
	GOODVALS.sort()
	print(GOODVALS)

	total = 0
	for x in range(0,(len(GOODVALS))):
		total = total + GOODVALS[x]

	print(total)