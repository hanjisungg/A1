#exercices A1

from random import*
from time import*


#exercice 1: implementer des fonctions

def tri_insertion(t):
    x = 0
    j = 0
    for i in range(1, len(t)):
        x = t[i]
        j = i
        while j>0 and x<t[j-1]:
            t[j]= t[j-1]
            j = j-1
        t[j] = x
    return t


def tri_selection(t):
    acc = 0
    for i in range(0, len(t)):
        min = t[i]
        imin = i
        for j in range(i+1, len(t)):
            if t[j]<min:
                min = t[j]
                imin = j
        acc = t[i]
        t[i] = t[imin]
        t[imin] = acc
    return t


#exercice 2: implementer des fonctions

def ttc(n, d):
    t = [0]*n
    for i in range(n):
        t[i] = randint(t[i-1], d)
    return t
        

#exercice 3: implementer des fonctions

def copie(t):
    c = [0]*len(t)
    for i in range(len(t)):
        c[i] = t[i]
    return c

def test_tri_insertion():
    for n in range(0, 100):
        t0 = [0]*n
        t1 = ttc(n, n//5)
        t2 = ttc(n, n**2)
        c0 = copie(t0)
        c1 = copie(t1)
        c2 = copie(t2)
        shuffle(t0)
        shuffle(t1)
        shuffle(t2)
        tri_insertion(t0)
        tri_insertion(t1)
        tri_insertion(t2)
        assert t0 == c0
        assert t1 == c1
        assert t2 == c2
        
def test_tri_selection():
    for n in range(0, 100):
        t0 = [0]*n
        t1 = ttc(n, n//5)
        t2 = ttc(n, n**2)
        c0 = copie(t0)
        c1 = copie(t1)
        c2 = copie(t2)
        shuffle(t0)
        shuffle(t1)
        shuffle(t2)
        tri_selection(t0)
        tri_selection(t1)
        tri_selection(t2)
        assert t0 == c0
        assert t1 == c1
        assert t2 == c2
        
        
        
#exercice 4: implementer des fonctions
        
def créer_t_non_tries(n):
    t = [0]*n
    for i in range(n):
        t[i] = randint(0, 1000)
    return t
    
    
def temps_tri_insertion(n):
    t = créer_t_non_tries(n)
    debut = perf_counter()
    tri_insertion(t)
    fin  = perf_counter()
    return((fin - debut)*1000)
    

def temps_tri_selection(n):
    t = créer_t_non_tries(n)
    debut = perf_counter()
    tri_selection(t)
    fin  = perf_counter()
    return((fin - debut)*1000)
    


#exercice 5
    
def ex5_insertion():
    i = 100
    while i <= 1000:
        a = temps_tri_insertion(i)
        print("pour", i, ": temps =", a)
        i += 100
    
def ex5_selection():
    i = 100
    while i <= 1000:
        a = temps_tri_selection(i)
        print("pour", i, ": temps =", a)
        i += 100

    
    
    
    
    
    

   