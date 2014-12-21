GOODVALS = []
def sums(below):
	total = 0	
	for x in range(0,below):
		if(x == 0):
			continue
		if((x%3) == 0):
			GOODVALS.append(x)
			continue
		if((x%5) == 0):
			GOODVALS.append(x)

	for t in GOODVALS:
		total= total+t

	return total

if __name__ == '__main__':
	print(sums(1000))