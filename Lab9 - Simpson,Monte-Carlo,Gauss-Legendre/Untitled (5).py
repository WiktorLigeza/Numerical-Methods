#!/usr/bin/env python
# coding: utf-8

# # Wiktor Ligęza IO gr.lab 2

# In[221]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy as sy
from sympy.parsing.sympy_parser import (parse_expr,
standard_transformations, implicit_application)
import random as random


# ### DANE

# In[202]:


funkcja = input("(np: 2^2 = 2**2, 2a = 2*a, cot(a) = cot a)podaj funkcję: ")
transformations = standard_transformations + (implicit_application,)
f1 = parse_expr(funkcja, transformations=transformations)
f1


# In[203]:


ilośćPodziałów = int(input("Podaj ilość podziałów: "))


# In[204]:


przedział = input("podaj przedział(np: pi/2,0): ").split(",")


# In[205]:


#INPUT CONVERSION 
x = sy.symbols("x")
f = sy.lambdify(x, f1)

transformations = standard_transformations + (implicit_application,)
przedział[0] = parse_expr(przedział[0], transformations=transformations)
przedział[1] = parse_expr(przedział[1], transformations=transformations)
przedział[0] = np.float64(przedział[0])
przedział[1] = np.float64(przedział[1])
przedział


# ### METODA SIMPSONA

# In[196]:


#n-number of divisions(even), r-range, f-funktion
def Simpson(n,r,f): 
    delta = (przedział[1]-przedział[0])/ilośćPodziałów
    s = abs(f(r[0])+f(r[1]))
    for i in range(1,n,2):
        s += 4*f(r[0]+i*delta)
    for i in range(2,n-1,2):
        s += 2*f(r[0]+i*delta)
    return (1/3)*s*delta


# ### METODA MONTE CARLO

# In[299]:


#n-number of divisions(even), r-range, f-funktion
def Monte_Carlo(n,r,f): 
    y = 0
    for i in range(n):
        y += f(random.uniform(r[0], r[1]))
    avg = y/n
    return avg*(r[1]-r[0])


# ### METODA KWADRATURY GAUSSA - LEGENDRE'A

# In[447]:


#2 węzłowa
#r-range, f-funktion
def Gauss_Legendre_2(n,r,f): 
    #stałe
    x2 = 0.577350
    x1 = -x2
    #skalowanie
    delta = (przedział[1]-przedział[0])/n
    s = 0;
    for i in range(n):
        a = r[0]+i*delta
        b = r[0]+(i+1)*delta
        t1 = ((a + b )/2)+((b-a)/2)*x1
        t2 = ((a + b )/2)+((b-a)/2)*x2
        t = (t1,t2)
        #obliczanie podcałki
        for j in range(2):
            s += ((b-a)/2)*f(t[j])
    return s


# In[493]:


#4 węzłowa
#r-range, f-funktion
def Gauss_Legendre_4(n,r,f): 
   #stałe
    #x
    x3 = 0.33998
    x4 = 0.86114
    x1 = -x4
    x2 = -x3
    #a
    a1 = 0.34785
    a2 = 0.65214
    a3 = 0.65214
    a4 = 0.34785
    A = (a1,a2,a3,a4)
    delta = (przedział[1]-przedział[0])/n
    s = 0;
    for i in range(n):
        a = r[0]+i*delta
        b = r[0]+(i+1)*delta
        t1 = ((a + b )/2)+((b-a)/2)*x1
        t2 = ((a + b )/2)+((b-a)/2)*x2
        t3 = ((a + b )/2)+((b-a)/2)*x3
        t4 = ((a + b )/2)+((b-a)/2)*x4
        t = (t1,t2,t3,t4)
        #obliczanie podcałki
        for j in range(4):
            s += (((b-a)/2)*f(t[j]))*A[j]
    return s


# ### WYNIKI
Wyniki dla funkcji 𝑥sin(𝑥), przedziału: 0 do pi/2 oraz 18 podziałów. Parametry można łatwo edytować w sekcji: DANE
# In[518]:


#wyniki dla tych samych danych wejściowych, wynik analityczny jest równy 1 
print("Simpson:           ",Simpson(ilośćPodziałów ,przedział,f)) #dla tej funkcji ilość podziałów powinna być parzysta 
print("Monte Carlo:       ",Monte_Carlo(ilośćPodziałów ,przedział,f))
print("Gaussa-Legendre 2: ",Gauss_Legendre_2(ilośćPodziałów,przedział,f))
print("Gaussa-Legendre 4: ",Gauss_Legendre_4(ilośćPodziałów,przedział,f))


# ### WNIOSKI
UWAGI: W przypadku Gaussa-Legendre 2 oraz 4, przedział(a,b) dzielony jest za pomocą wzoru: delta=(b-a)/n, następnie każdy kolejny podprzedział z zakresu n cechuje sie granicami ai oraz bi (gdzie ai = a+i*delta oraz bi = a+(i+1)*delta), następnie przeprowadzane jest skalowanie. 
Nie wyświetlam tych danych, ponieważ wpłynęłoby to negatywnie na czytelność sprawozdania.
# In[546]:


S  = abs(0.9999990319568973-1)
M  = abs(0.9976731836651214-1)
G2 = abs(1.0000000399943598-1)
G4 = abs(0.9999900008483511-1)
arr = (S,M,G2,G4)
for i in range(4):
    if min(arr) == S:
        print("Simpson")
        break;
    if min(arr) == M:
        print("Monte Carlo")
        break;
    if min(arr) == G2:
        print("Gaussa-Legendre 2")
        break;
    if min(arr) == G4:
        print("Gaussa-Legendre 4")
        break;

w tym przypadku matoda 2-węzłowa(Gaussa-Legendre) okazała się najbardziej trafna(wynik analityczny = 1)