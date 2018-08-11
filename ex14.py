
from sys import argv

script, user_name, date = argv
symbol = '> '

print(f"Hi {user_name}, I'm the {script} script .")
print("I'd like to ask you a few question .")
print(f"Do you like me {user_name}?")
like = input(symbol)

print(f"where do you live {user_name} ?")
lives = input(symbol)

symbol = '>*> '
print("What kind of computer do you like ?")
computer = input(symbol)

print(f"""
	
so, today is #{date}

Alright, so you said {like} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")