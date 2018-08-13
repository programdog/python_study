print("""you enter a dark room with two doors.
do you go through door #1 or door #2?""")

door = input("> ")

if door == '1':
	print("T")
	print("w")
	print("1.")
	print("2.")

	bear = input("> ")

	if bear == "1":
		print("bear = 1!")
	elif "2" == bear:
		print("2 = bear")
	else:
		print("bear not 1 or 2")


elif '2' == door:
	print("Y")
	print("1.")
	print("2.")
	print("3.")

	insanity = input("> ")

	if insanity == "1" or insanity == "2":
		print("Y")
		print("G")
	else:
		print("T")
		print("G")
else:
	print("Y")

	# range_test = input("> ")
	# if x in range(1, 10):
	# 	print("in 1-10")
	# elif x in range(10, 20):
	# 	print("in 10-20")
	# elif x in range(21, 30):
	# 	print("in 21-30")
	# else:
	# 	print("in none")