
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copy from {from_file} to {to_file}")

in_file = open(to_file)
in_data = in_file.read()

print(f"The input file is {len(in_data)} bytes long")

print(f"does the output file exists? {exists(to_file)}")

print("Ready. Hit return or CTRL+C to abort")
input(">:  ")

out_file = open (to_file, 'w')
out_file = write (in_data)

print("Alright. all done")

out_file.close()
in_file.close()
