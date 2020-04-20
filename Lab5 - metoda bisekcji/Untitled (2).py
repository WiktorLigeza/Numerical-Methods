#!/usr/bin/env python
# coding: utf-8

# In[33]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[34]:


x1 = np.float32(input("Wprowadź wartość x1: "))


# In[35]:


x2 =  np.float32(input("Wprowadź wartość x2: "))


# In[5]:


tol = np.float32(input("Wprowadź wartość x: "))


# In[6]:


iloscIteracji = int(input("Podaj ilosc iteracji: "))


# In[36]:


def metodaBisekcji(y,x1,x2):
    red = [[x1,y(x1)]] #x2
    green = [[x2,y(x2)]] #x1
    yellow =[] #root
#-----------------------------funckja--------------------------------   
    if y(x1)*y(x2) > 0:
        print("brak pierwiastka w danej sekcji")
        return 0
        
    if y(x1) == 0:
        print("x1 jednym pierwiastków")
        return 0
        
    if y(x2) == 0:
        print("x2 jednym pierwiastków")
        return 0
    
    #jeżeli żadne z powyższych ifów się nie spełnił
    #znacz to że że pierwiastek znajduje się w podanym przedziale
    for i in range(iloscIteracji):
        c = (x1+x2)/2 #bisekcja
        if y(c)*y(x1) < 0: #pierwiastek znajduje się pomiędzy c a x1 więc x2 przyjumje wartość c
            x2 = c
            green.append([x2,y(x2)])
        else:              #pierwiastek znajduje się pomiędzy c a x2 więc x1 przyjumje wartość c
            x1 = c
            red.append([x1,y(x1)])
        if abs(y(x1)) < tol:
            print("ilość wykonanych iteracji: ",i) 
            break
#------------------------------------------------------------- 
    print("pierwiastek znajduje się w x: ",x1)
    yellow.append([x1,y(x1)]) #root
    x_list = np.linspace(0,2.5,100)
    x_list[0] = 0.00001
    fplot = list(map(y, x_list))
    plt.plot(x_list, fplot)
    #x1
    x, y = list(zip(*green))
    plt.scatter(x, y, c='r')
    #x2
    x, y = list(zip(*red))
    plt.scatter(x, y, c='g')
    #result           
    x, y = list(zip(*yellow))
    plt.scatter(x, y, c='y')


# In[37]:


wilomianowa = lambda x: 2*x**2 - 5*x +3
logarytmiczna = lambda x: np.log(x**2 + 2*x)
trygonometryczna = lambda x: np.sin(x**3 - 2*x)


# In[38]:


metodaBisekcji(wilomianowa,x1,x2)


# In[39]:


metodaBisekcji(trygonometryczna,x1,x2)


# In[40]:


x1 = np.float32(input("Wprowadź wartość x1: "))


# In[41]:


x2 =  np.float32(input("Wprowadź wartość x2: "))


# In[42]:


metodaBisekcji(logarytmiczna,x1,x2)


# Kolor zielony oznacza x1, czerowny x2, żółty wynik

# In[ ]:




