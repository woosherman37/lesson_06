def double_the_amount_minus1(number):

	double = number * 2
	double_minus1 = double - 1
	return double_minus1

num = input(f"\nGive me a number? ")

num = int(num)


result = double_the_amount_minus1(number = num)

print(result)

