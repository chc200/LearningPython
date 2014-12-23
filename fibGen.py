def fib(max):
	a, b = 0, 1

	while a < max:
		yield a
		a, b = b, a + b

if __name__ == '__main__':
	for x in fib(20):
		print(x)