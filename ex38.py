ten_things = "apples oranges crows telephone light sugar"

print("wait there are not 10 thing in that list . let's fix that.")

stuff = ten_things.split(' ')
print(f"{stuff}")
more_stuff = ["day", "night", "song", "frisbee", "corn", "banana", "girl", "boy"]
print(f"{len(stuff)}")

while len(stuff) < 10:

	next_one = more_stuff.pop()
	print("adding: ", next_one)
	stuff.append(next_one)
	print(f"len(stuff) = {len(stuff)}")
	print(f"there are {len(stuff)} items now")


print("there we go: ", stuff)

print("let's do something")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what? cool!
print('#'.join(stuff[3:7])) # super stellar!

