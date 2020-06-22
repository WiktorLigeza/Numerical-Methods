#!/usr/bin/env python
# coding: utf-8

# # Wiktor Ligęza IO gr.lab 2
# 

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy as sy
from sympy.parsing.sympy_parser import (parse_expr,
standard_transformations, implicit_application)


# ### DANE

# In[124]:


funkcja = input("(np: 2^2 = 2**2, 2a = 2*a, cot(a) = cot a)podaj funkcję: ")
transformations = standard_transformations + (implicit_application,)
f1 = parse_expr(funkcja, transformations=transformations)
f1


# In[125]:


ilośćPodziałów = int(input("Podaj ilość podziałów: "))


# In[130]:


przedział = input("podaj przedział(np: pi/2,0): ").split(",")
transformations = standard_transformations + (implicit_application,)
przedział[0] = parse_expr(przedział[0], transformations=transformations)
przedział[1] = parse_expr(przedział[1], transformations=transformations)
przedział[0] = np.float64(przedział[0])
przedział[1] = np.float64(przedział[1])
przedział


# ##### wartość "skoku"

# In[131]:


delta = (przedział[1]-przedział[0])/ilośćPodziałów
delta


# In[132]:


x = sy.symbols("x")
f = sy.lambdify(x, f1)


# ### METODA PROSTOKĄTÓW

# In[151]:


suma = 0
for i in range(ilośćPodziałów):
    podstawa = (przedział[0]+(i+1)*delta)-(przedział[0]+i*delta)
    suma += f(przedział[0]+i*delta)*podstawa
wynik1 = suma
print("wynik: ",suma)


# ### METODA TRAPEZÓW

# In[152]:


suma = (f(przedział[0])+f(przedział[1]))*0.5
for i in range(ilośćPodziałów):
    suma += f(przedział[0]+i*delta)
wynik2 = delta*suma
print("wynik: ",wynik)


# ### WNIOSKI

# In[153]:


# wynik analityczny = 1
wynik1 = abs(wynik1-1) #metoda prostokątów 
wynik2 = abs(wynik2-1) #metoda trapezów
if(wynik2 < wynik1):
    print(wynik2,"<", wynik1)


# Jak widać dla tej samej liczby podziałów metoda trapezów jest bardziej dokładna (bliższa, w tym przypadku, wynikowi równemu 1).
# Na wynik ma wpływ również liczba przedziałów, im większa jest to liczba, tym dokładniejszy będzie to wynik.
