def fib(max):
	a, b = 0, 1

	while a < max:
		yield a
		a, b = b, a + b

if __name__ == '__main__':
	count = fib(20)
	for x in range(0,8):
		print(next(count))