def timer(fn, *args):
    "Time the application of fn to args. Return (result, seconds)."
    import time
    start = time.clock()
    return fn(*args), time.clock() - start


def funcion():
	for i in range(1, 200):
		print i

if __name__ == '__main__':
	print timer(max, range(90))
	print(timer(funcion))
