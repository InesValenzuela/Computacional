# -*- coding: utf-8 -*-
from math import pi
G=6.67e-11
M=5.97e24
R=6371e3
T = float(input("ingrese el periodo del satélite:"))
h=((G* M * T**2/(4*pi**2))**(1./3))-R
print("La altitud del satelite es de", h , "metros")
