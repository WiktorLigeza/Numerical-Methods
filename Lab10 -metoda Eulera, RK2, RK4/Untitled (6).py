#!/usr/bin/env python
# coding: utf-8

# # Wiktor Ligęza IO gr.lab 2

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy as sy
from sympy.parsing.sympy_parser import (parse_expr,
standard_transformations, implicit_application)
from sympy.abc import x, y


# ### DATA

# In[10]:


funkcja = input("(np: 2^2 = 2**2, 2a = 2*a, cot(a) = cot a)podaj funkcję: ")
transformations = standard_transformations + (implicit_application,)
f = parse_expr(funkcja, transformations=transformations)
f


# In[11]:


print("podaj warunki początkowe")
x0 = np.float32(input("Wprowadź wartość x0: "))
xn = np.float32(input("Wprowadź wartość xn: "))
y0 = np.float32(input("Wprowadź wartość y: "))


# ### EULER

# In[12]:


def metodaEulera(f, x0, xn, y0, delta):
    #lambdify
    s = (x, y)
    f = sy.lambdify(s, f)
    
    #init
    i = x0
    iteracje = 0
    
    while i <= xn-delta :
        y0 += f(i, y0)*delta
        i += delta
        iteracje += 1

    print("Euler wynik: ",y0, "| liczba iteracji: ", iteracje)


# ### RUNGE-KUTTA 2

# In[13]:


def metodaRK2(f, x0, xn, y0, delta):
    #lambdify
    s = (x, y)
    f = sy.lambdify(s, f)
    
    #init
    i = x0
    iteracje = 0
    
    while i <= xn-delta :
        k1 = f(i, y0)
        k2 = f(i + delta, y0 + delta*k1)
        i += delta
        o = 0.5*(k1 + k2)
        y0 = y0 + delta*o
        iteracje += 1

    print("RK2 wynik  : ",y0, "| liczba iteracji: ", iteracje)


# ### RUNGE-KUTTA 4

# In[14]:


def metodaRK4(f, x0, xn, y0, delta):
    #lambdify
    s = (x, y)
    f = sy.lambdify(s, f)
    
    #init
    i = x0
    iteracje = 0
    
    while i <= xn-delta :
        k1 = f(i, y0)
        k2 = f(i + 0.5*delta, y0 + 0.5*delta*k1)
        k3 = f(i + 0.5*delta, y0 + 0.5*delta*k2)
        k4 = f(i + delta, y0 + delta*k3)
        i += delta
        o = (1/6)*(k1 + 2*k2 + 2*k3 + k4)
        y0 = y0 + delta*o
        iteracje += 1

    print("RK4 wynik  : ",y0, "| liczba iteracji: ", iteracje)


# #### WYNIKI 

# In[16]:


delta = np.float32(input("Wprowadź wartość h: "))


# In[17]:


metodaEulera(f, x0, xn, y0, delta)
metodaRK2(f, x0, xn, y0, delta)
metodaRK4(f, x0, xn, y0, delta)


# In[18]:


delta = np.float32(input("Wprowadź wartość h: "))


# In[19]:


metodaEulera(f, x0, xn, y0, delta)
metodaRK2(f, x0, xn, y0, delta)
metodaRK4(f, x0, xn, y0, delta)


# uwagi: liczba kroków jest taka sama dla każdej z metod ponieważ warunki początkowe są takie same

# ### WNIOSKI
Dla funkcji 𝑓=𝑥𝑦 gdzie 𝑥∈[0,2] oraz warunków początkowych: 𝑦=1, delta(h)=0.01 jak i dla delta(h)=0.03
najbardziej dokładną metodą okazała się metoda RUNGEGO-KUTTY czwartego rzędu.
Wynik analityczny jest równy 7.389056
Jak widać im mniejsza wielkość skoku tym bardziej dokładny wynik, niestety kosztem szybkości obliczeń.