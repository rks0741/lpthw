#i = int(input("Input i: "))
#b = int(input("input b: "))

i = 0
b = int(input("input b: "))
#inc = int(input("input inc: "))
numbers = []


#def num_inc(arg_a, arg_b, incr):

#    while arg_a < arg_b:
#        print(f"At the top of list is {arg_a}")
#        numbers.append(arg_a)

#        arg_a = arg_a + incr
#        print("numbers now:", numbers)
#        print(f"At the bottom i is {arg_a}")
#    return numbers

def num_for(arg_a, arg_b):

    for arg_a in range(arg_b):
        print(f"At the top of list is {arg_a}")
        numbers.append(arg_a)


        print("numbers now:", numbers)
        print(f"At the bottom i is {arg_a}")
    return numbers


num_mass = num_for(i, b)

print("The numbers: ")

for num in num_mass:
    print(num)
