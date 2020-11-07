#Create a program that reads three integers from the user and displays them in sorted order (from smallest to largest).
#Use the min and max functions to find the smallest and largest values.
#The middle value can be found by computing the sum of all three values, and then subtracting the minimum value and the maximum value.

a=int(input())
b=int(input())
c=int(input())
smallest=min(a,b,c)
largest=max(a,b,c)
middle=(a+b+c)-smallest-largest
print("The minimum value is",smallest)
print("The maximum value is",largest)
print("The middle value is",middle)
