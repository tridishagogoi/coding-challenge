#Write a program that begins by reading a temperature from the user in degreesCelsius.
#Then your program should display the equivalent temperature in degrees Fahrenheit.
#The calculations needed to convert between different units of temperature is your task

celsius = float(input(""))
fahrenheit = (celsius * 1.8) + 32
print('The fahrenheit value for %0.1f celsius is %0.2f fahrenheit' %(celsius,fahrenheit))