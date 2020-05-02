#!/usr/bin/env python
# coding: utf-8

# # Wiktor Ligęza IO gr.lab 2

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy as sy
from sympy.parsing.sympy_parser import (parse_expr,
standard_transformations, implicit_application)
from sympy.abc import x, y


# # DANE

# In[45]:


tol = np.float32(input("Wprowadź wartość tol: "))


# In[18]:


iloscIteracji = int(input("Podaj maksymalną ilość iteracji: "))


# In[7]:


funkcja = input("(np: 2^2 = 2**2, 2a = 2*a, cot(a) = cot a)podaj funkcję: ")
transformations = standard_transformations + (implicit_application,)
f1 = parse_expr(funkcja, transformations=transformations)
f1


# In[8]:


funkcja = input("(np: 2^2 = 2**2, 2a = 2*a, cot(a) = cot a)podaj funkcję: ")
transformations = standard_transformations + (implicit_application,)
f2 = parse_expr(funkcja, transformations=transformations)
f2


# In[56]:


X0 = list(map(np.float32, input("podaj warunek począrkowy (np: X0 = 1,2): ").split(",")))
X0 = np.asarray(X0).reshape(-1,1)
Xroot = X0
Xroot


# # OBLICZANIE

# ### F(Xk)

# In[13]:


F = sy.Matrix([f1,f2])
F


# In[22]:


s = (x, y)
F_func = sy.lambdify(s, F, modules='numpy')


# ### J^-1[Xk]

# In[15]:


#Jakobian^-1
J = sy.Matrix([f1,f2]).jacobian(['x', 'y'])
J = J.inv()
J


# In[16]:


s = (x, y)
J_func = sy.lambdify(s, J, modules='numpy')


# ### metoda Newtona-Rhapsona

# In[57]:


for i in range(iloscIteracji):
    Xk = X0 - J_func(X0[0][0],X0[1][0]) @ F_func(X0[0][0],X0[1][0])
    X0 = Xk
    if stop(Xk) :
        break

print("ilosc powtórzeń:",i)


# #### wynik:

# In[58]:


print(X0)


# #### wartość funkcji w zadanym punkcie

# In[59]:


print(F_func(Xroot[0][0],Xroot[1][0]))  


# ###### jeżeli wektor dla otrzymanego punktu będzie = [0,0], oznacza to że wynik jest poprawny

# In[50]:


F_func(X0[0][0],X0[1][0])


# ### warunek przerwania 

# In[52]:


def stop(Xk):
    i=0
    j=0
    X = F_func(X0[0][0],X0[1][0])
    if abs(X[0]-0) < tol :
        i = 1
    if abs(X[1]-0) < tol :
        j = 1
    if j+i == 2 :
        return True
    else : 
        return False


# In[ ]:


### przykładowe funkcje
x*y+2*y-2
x**2+4*y**2-4


2*x+y**2 - 6
x*y-2

