from sys import argv
filenames = []

def show_content(filename):
	with open(filename) as f:
		print f.read()

filenames = argv
# for i in range(1, len(argv)):
# 	show_content(filenames[i])

for filename in filenames:
	show_content(filename)

#assert 1!=1, "1 itu sama dengan 1"
# show_content("ex37.py")

a = [x for x in range(5)]

def square(x):
	return x*x

print map(square, a)
def mul(x, y):
	return x*y
def is_event(x):
	return x > 0 and x % 2 == 0

res = map(square, a)
print filter (is_event, res)

del res[0]

print reduce(mul, res)

#test try catch
def test_try_except():
	try:
		print "try"
		filenya = open("ex37.py")
		print "exception: ", int("kkklk")
	except Exception, e:
		raise "exception nyanyanya.."
	else:
		print "else exception"
	finally:
		print "finally akhirnya should always executed"
		filenya.close()

# test_try_except()

f = lambda x: x**2 + 2*x - 5
bil = [x**2 + 2*x - 5 for x in range(25)]

mult3 = filter(lambda x: x % 3 == 0, bil)

print mult3

polynome = map (f, [x for x in range(1, 4)])
print polynome