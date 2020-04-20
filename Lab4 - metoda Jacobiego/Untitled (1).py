#!/usr/bin/env python
# coding: utf-8

# # Wiktor Ligęza IO gr.lab 2

# typ: sprawozdanie\
# temat: metoda Jacobiego\
# środowisko: jupyter\
# język: Python\
# zadanie: program wczytuje dane z pliku tekstowego i przy użyciu metody Jacobiego rozwiązuje układ równań\

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[22]:


df = pd.read_csv('formatZadania.csv',header=None)
formatZadania = df.to_numpy()
size = int(formatZadania[0])
stop = int(formatZadania[size+1])
minimum = np.float64(formatZadania[size+2])
print("rozmiar:", size)
print("tolerancja:", minimum)
print("ilosc powtorzen:", stop)
df


# In[3]:


#initial matrix
matrix= pd.read_csv('formatZadania.csv',header=None, sep=' ',skiprows=1, nrows=size,dtype=np.float32).values
matrix


# In[4]:


_A = matrix[0:size, 0:size].copy()
_A


# In[5]:


_B = matrix[0:size, size:size+1].copy()
_B.reshape(1,-1)[0]


# In[6]:


X = np.zeros(len(_B),float)
rez = np.zeros(len(_B),float)
rez


# In[7]:


n = len(_B)
A = _A.copy()


# In[8]:


#SPRAWDZANIE CZY DIAGONALNA JEST DOMINUJĄCA
iterator = 0
D = np.diag(A) #diagonalna macierzy A
isItDominant = False
A = A-np.diagflat(D)
for i in range(n) :
    for j in range(n) :
        if np.fabs(A[i,j]) < np.fabs(D[i]) :
            iterator = iterator+1
if iterator == n*n :
    isItDominant = True
       
print("diagonalna:",D)
print("czy diagonalna jest dominujaca:",isItDominant) 


# ### w tym przypadku diagonalna jest dominująca

# In[9]:


stop = 1
A, B = _A.copy(), _B.copy()


# In[10]:


## DLA 1 POWTÓRZENIA
for stopwatch in range(stop): #ogranicznik wykonywania się pętli 
    for i in range(n):
        sum = 0 #inicjalizacja sumy, wartość startowa = 0
        for j in range(n):
            if j != i :
                sum = sum + A[i,j]*X[j]
        rez[i] = -1/A[i,i]*(sum - B[i])
    X = rez
print("wynik dla jednego powtorzenia: " ,rez)


# In[11]:


stop = 10
A, B = _A.copy(), _B.copy()


# In[12]:


## DLA 10 POWTÓRZEŃ
for stopwatch in range(stop):
    for i in range(n):
        sum = 0 
        for j in range(n):
            if j != i :
                sum = sum + A[i,j]*X[j]
        rez[i] = -1/A[i,i]*(sum - B[i])
    X = rez
print("wynik dla 10 powtorzen: " ,rez)


# In[13]:


stop = 100
A, B = _A.copy(), _B.copy()


# In[14]:


## DLA 100 POWTÓRZEŃ
for stopwatch in range(stop): 
    for i in range(n):
        sum = 0
        for j in range(n):
            if j != i :
                sum = sum + A[i,j]*X[j]
        rez[i] = -1/A[i,i]*(sum - B[i])
    X = rez
print("wynik dla 100 powtorzen: " ,rez)


# In[15]:


A, B = _A.copy(), _B.copy()
minimum = 0.000001


# In[16]:


## Z PRZERWANIEM dla danej dokładności 
for stopwatch in range(stop): 
    breaker = True
    for i in range(n):
        sum = 0
        for j in range(n):
            if j != i :
                sum = sum + A[i,j]*X[j]
        rez[i] = -1/A[i,i]*(sum - B[i])
        if np.fabs(rez[i] - X[i]) > minimum:
            breaker = False
    if breaker:
        break
    X = rez
print("wynik: " ,rez)


# In[17]:


A, B = _A.copy(), _B.copy()


# In[18]:


print("wynik poprawny (obliczony przez numpy):" )
print(np.linalg.solve(A,B).reshape(1,-1)[0])


# Jak widać wynik jest poprawny

# WNIOSKI: Dokładność rozwiązania zależy od ilość powtórzeń oraz ważne jest żeby zachodziła diagonalna domincja 
