
def division(a, b):
	try:
		
		result = float(a / b)
		print("answer is " + str(result))
	except ZeroDivisionError:
		print("Division by 0 is not possible!")

# Look at parameters and note the working of Program
division(5, 8)
