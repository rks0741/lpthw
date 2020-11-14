from sys import argv

script, filename = argv

print(f"We are going to erase a file {filename}")
print("If you do not want to erase the file, hit CTRL-C(^C).")
print("If you do want, hit return.")



print("Opening file...")
target = open (filename, 'a')

print("Truncating the file. Goodbye!")
target.truncate(4)



print("and finally we close it")
target.close()
