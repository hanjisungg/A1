#A1

#exercice 143

def est_trie(t):
    for i in range(1, len(t)):
        if t[i] < t[i-1]:
            return False
    return True

#exercice 144

def insere(t, i):
    x = t[i]
    j = i
    while j > 0 and t[j-1]>x:
        t[j] = t[j-1]
        j = j-1
    t[j] = x
             

def tri_par_insertion_externe(t):
    t2 = [0]*len(t)
    for i in range(len(t)):
        t2[i] = t[i]
        insere(t2, i)
    return t2


#exercice 145


def plus_petits(t, k):
    t2 = [0]*k
    for i in range(k):
        t2[i] = t[i]
        insere(t2, i)
    for i in range(k, len(t)):
        if t[i]<t2[-1]:
            t2[-1] = t[i]
            insere(t2, k-1)
    return t2


#exerice 146

def ex146(t):
    
    
    
    
    
    
    
    
    
    
    
    
    
    