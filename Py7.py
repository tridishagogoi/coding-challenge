#Write a program to check whether the entered string ends with the character that user entered

#Input:
#1. The string input
#2. The Character to be checked

#Output:
#If the string ends with the character entered by the user then print "YES" else print "NO"


a=input("")
b=a[-1]
c=input("")
if c==b:
  print("YES")
else:
  print("NO")