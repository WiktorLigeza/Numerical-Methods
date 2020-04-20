#!/usr/bin/env python
# coding: utf-8

# ## Wiktor Ligęza IO gr.lab 2 

# typ: sprawozdanie

# temat: metoda eliminacji Gaussa

# środowisko: jupyter 
# 

# język: Python

# zadanie: program wczytuje dane z pliku tekstowego i przy użyciu metody eliminacji GAUSSA rozwiązuje układ równań

# In[15]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# #### WCZYTYWANIE DANYCH Z PLIKU TEKSTOWEGO

# In[2]:


_A = pd.read_csv('A.csv',header=None, sep=' ', dtype=np.float32).values
_A


# In[3]:


_B = pd.read_csv('B.csv',header=None, sep=' ', dtype=np.float32).values.reshape(1,-1)[0]
_B


# In[18]:


A, B = _A.copy(), _B.copy() #kopiowanie tablic dla porównywalnych wyników 


# #### DEFINICJE

# In[5]:


n = B.shape[0]
_X = np.zeros(n,float)
A, B, X = _A.copy(), _B.copy(), _X.copy()


# #### ELIMINACJA BEZ PIVOTINGU

# In[6]:


for k in range(n-1):
    for i in range(k+1,n):
        if A[i,k] == 0:
            continue #jeżeli już jest 0, pomijamy
        x = A[k,k]/A[i,k]
        for j in range(k,n):
            A[i,j] = A[k,j] - A[i,j]*x
        B[i]=B[k]-B[i]*x
print("macierz A:\n",A,"\n")
print("macierz B:\n",B)            


# In[7]:


#PODSTAWIENIA 
X[n-1] = B[n-1]/A[n-1,n-1] 
for i in range(n-2,-1,-1):
    y = 0
    for j in range(i+1,n):
        y += A[i,j] * X[j]
    X[i] = (B[i] - y) / A[i,i]
print("macierz  X:\n",X)


# jak widać powyżej, w przypadku macierzy na której diagonalnej znajduje/znajdują się 
# zero/a wynik jest niepoprawny, ze względu na dzielenie przez zero 

# #### ELIMINACJA Z PIVOTINGIEM

# In[9]:


A, B, X = _A.copy(), _B.copy(), _X.copy()


# In[10]:


for k in range(n-1):
    if np.fabs(A[k,k]) == 0: #jeżeli wystąpi 0 na diagonalnej, zamieniamy wiersze aby uniknąć dzielenia przez 0
        for i in range (k+1,n):
            if np.fabs(A[i,k]) > np.fabs(A[k,k]):
                A[[k,i]] = A[[i,k]]
                B[[k,i]] = B[[i,k]]
                break
    for i in range(k+1,n):
        if A[i,k] == 0:
            continue
        x = A[k,k]/A[i,k]
        for j in range(k,n):
            A[i,j] = A[k,j] - A[i,j]*x
        B[i]=B[k]-B[i]*x
print("macierz A:\n",A,"\n")
print("macierz B:\n",B)      


# In[11]:


#PODSTAWIENIA 
X[n-1] = B[n-1]/A[n-1,n-1] 
for i in range(n-2,-1,-1):
    y = 0
    for j in range(i+1,n):
        y += A[i,j] * X[j]
    X[i] = (B[i] - y) / A[i,i]
print("macierz  X:\n",X)


# In[12]:


######## poprawny wynik
print("wynik poprawny (obliczony przez numpy):" )
print(np.linalg.solve(_A,_B))


# jak widać wynik jest poprawny

# Uwagi: wygląd macierzy A oraz B może być nieczytelny ze względu na użycie dość dużego typu zmiennej(float64), oraz randomowych liczb.
# 

# In[ ]:




