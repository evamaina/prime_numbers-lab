def primeNumbers(n):
	prime_numbers = []
	if isinstance(n,list):
		raise TypeError("Input cannot be a list")
	elif isinstance(n,dict):
		raise TypeError("Input cannot be a dictionary")
	elif n < 1:
		return []
	else:
		for num in range(2,n):
			for i in range(2,num):
				if (num%i) == 0:
					break
			else:
				prime_numbers.append(num)
	return prime_numbers

	
	print (primeNumbers(15))



