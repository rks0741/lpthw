from sys import argv
script, user_name = argv
prompt = '> '
print(f"Hi {user_name}, I am the {script} script!")

print("Here are some questions for you:")
print(f"do you like me, {user_name}?")
likes=input(prompt)
print(f"Where do you live {user_name}?")
lives=input(prompt)
print("What kind of PC do you have?")
computer=input(prompt)
print(f"""
OK, so you said you {likes} about liking me.
You live in {lives}. Where is it?
And you have a {computer} computer. nice)
""")
