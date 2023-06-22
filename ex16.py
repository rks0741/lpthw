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

print("No enter three new lines")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I am going ro write it into the file")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally closing the file")
target.close()
