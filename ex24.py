print("let's practice everying.")
print('You \'d need to know \'bout escapes with \\ that do :')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with
cannot
nor
and
\n\t\twhere
"""

print("---------------")
print(poem)
print("---------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates


start_point = 10000
beans_temp, jars, crates = secret_formula(start_point)

#remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
#it's just like with an f""string
print(f"WE'd have {beans_temp} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("we can also do that this way:")
formula = secret_formula(start_point)
#this is an easy way to apply a list to format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))