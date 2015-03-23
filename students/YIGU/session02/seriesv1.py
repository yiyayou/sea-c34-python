def fibonacci(n):
	if n==0 or n==1:
		i=n
		return i

	else:
		a=0
		b=1
		for i in range(n-1):
			i=a+b
			a=b
			b=i
		return i

if __name__ == "__main__":
	print fibonacci(6)