from sys import argv

script, filename = argv

print(f"We are giong to erase a file {filename}")
print("If you do not want to erase the file, hit CTRL-C(^C).")
print("If you do want, hit return.")

input("?")

print("Opening file...")
target = open (filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now i am going to ask you about some lines")

line1 = input("line 1 :")
line2 = input("line 2 :")
line3 = input("line 3 :")

print("I am going to write this lines into the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("and finally we close it")
target.close()
