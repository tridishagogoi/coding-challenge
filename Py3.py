#Write a Python Program to Find the Gravitational Force Acting Between Two Objects


m1=float(input(""))
m2=float(input(""))
r =float(input(""))
G=6.673*(10**-11)
f=(G*m1*m2)/r**2
print("%0.2f" %f)
