print("Lets practice everything")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n new lines and \t tabs.')

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of lovel
nor comprehend passion from intuition
and requires a explanation
\n\t\twhere there is none.
"""

print("--------------------")
print(poem)
print("--------------------")

five = 10 - 2 + 3 - 6
print(f"this should be  five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates



start_point = 10000
beans, jars, crates = secret_formula(start_point)

#remember there is another way to farmat the string
print("with a starting point of:{}".format(start_point))
#it is just like with f"" string
print(f"We have {beans} beans, {jars} jars and {crates} crates.")

start_point = start_point/10

print("We can also do it this way:")
formula = secret_formula(start_point)
#this is an easy way to apply a list to a formula string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
