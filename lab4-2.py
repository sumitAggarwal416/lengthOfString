#I, Sumit Aggarwal, student number 000793607, certify that all code submitted is
#my own work and I have not copied from any source. I also certify that I have
#not allowed anyone else to copy my work
import math
a= int(input("Enter a "))
b=int(input("Enter b "))
c= int(input("Enter c "))
formula1= (-b - (math.sqrt(b**2 - 4*a*c)))/(2*a)
formula2= (-b + (math.sqrt(b**2 - 4*a*c)))/(2*a)
#print(formula1)
#print(formula2)
if formula1>0 and formula2>0:
    print("It is true that Formula  and Formula 2's answer are both positive")
else:
    print("It is false that Formula 1 and Formula 2's answer are both positive")
