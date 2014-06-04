def print_numbers(max, increment):
	i = 0
	numbers = []

	while i < max:
		print "At the top i is %d" % i
		numbers.append(i)

		i += increment;
		print "numbers now: ", numbers
		print "at the bottom i is %d" % i

	print "The numbers: "
	for num in numbers:
		print num

def print_numbers2(max, increment):
	print "using for-loops"
	numbers = []
	for num in range(0,max, increment):
		print num

print_numbers(10, 3)
print_numbers2(10, 3)