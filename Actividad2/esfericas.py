from math import pi,sqrt,atan,acos
x = float(input("Introduce x: "))
y = float(input("Introduce y: "))
z = float(input("Introduce z: "))
r = sqrt((x**2)+(y**2)+(z**2))
theta= atan(y/x)
phi=acos(z/r)
p=phi*180/pi
d=theta*180/pi
print("r =",r," theta =", d, "phi=",p )