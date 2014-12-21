total = 0
GOODVALS = []

def sums(below):
	if below == 0:
		return 0
	elif below == 1:
		return 1
	else:

		return sums(below-1) + sums(below-2)

if __name__ == '__main__':
	for x in range(0,30):
		GOODVALS.append(sums(x))
		GOODVALS.sort()
		print(GOODVALS)
