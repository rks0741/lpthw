
import numpy as np

print ("enter 6 numbers")
L = np.array([int(x) for x in input("Enter multiple values\n").split(', ')])
print("\nThe values of input are", L)

Disp= np.var(L)
print (Disp)
