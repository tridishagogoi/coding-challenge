#When the length of its base and its height were known. It is also possible to compute the area of a triangle when the lengths of all three sides are known. Let s1, s2 and s3 be the lengths of the sides. Let s = (s1 + s2 + s3)/2. Then the area of the triangle
#can be calculated using the following formula:
#area = sqrt(s*(s-s1)*(s-s2)*(s-s3))
#Develop a program that reads the lengths of the sides of a triangle from the user and displays its area.
#Display the output to two floating point digits (%0.2f, %variablename)

s1 = int(input(""))
s2 = int(input(""))
s3 = int(input(""))
s = (s1 + s2 + s3) / 2
area = (s*(s-s1)*(s-s2)*(s-s3))**0.5
print('The area of the triangle is %0.1f' %area)