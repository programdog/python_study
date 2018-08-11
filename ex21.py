def add(a, b):
	print(f"ADDING {a} + {b}")
	return a + b

def subtract(a, b):
	print(f"SUBTRACTING {a} - {b}")
	return a - b

def multiply(a, b):
	print(f"muliply {a} * {b}")
	return a * b

def divide(a, b):
	print(f"divide {a} / {b}")
	return int (3 + a / b - 2 * 5)


print("let's test ")

age = add(30, 5)
height = subtract(78, 4)
weignt = multiply(90, 2)
iq = divide(10, 2)

print(f"Age = {age}, height = {height}, weignt = {weignt}, iq = {iq}")


print("Here is a puzzle")

what = add(age, subtract(height, multiply(weignt, divide(iq, 2))))

print("that becomes: ", what, "can you do it by hand?")

f_test = int(input())
print(f"f_test = {f_test}")