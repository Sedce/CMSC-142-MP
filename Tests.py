
# coding: utf-8

# In[3]:

import random

x = []
#test case: 
def random_test():
        l = random.sample(range(0, 100000), 1)   
        return l

def sorted_test():
        l = random.sample(range(0, 100000), 1)
        return sorted(l)

def reverse_sorted_test():
        l = random.sample(range(0, 100000),1)  
        return list(reversed(l))


def test_case():
    l = random.sample(range(0, 100000), 200)   
    return sorted(l)

def test_case2():
    l = random.sample(range(0, 100000), 200)   
    return list(reversed(l))


# In[4]:


def test_set_best_case():
    #First test case: len = 50
    w1 = []
    i = 1
    while ( i <= 10):
        w1.append(i);
        i += 1;
        
     #First test case: len = 50
    w2 = []
    i = 1
    while ( i <= 20):
        w2.append(i);
        i += 1;
    
    
    #First test case: len = 50
    w3 = []
    i = 1
    while ( i <= 50):
        w3.append(i);
        i += 1;
    
    
    #First test case: len = 50
    w4 = []
    i = 1
    while ( i <= 100):
        w4.append(i);
        i += 1;
    
    #First test case: len = 50
    w5 = []
    i = 0
    while ( i <= 150):
        w5.append(i);
        i += 1;
    
    #First test case: len = 50
    w6 = []
    i = 1
    while ( i <= 200):
        w6.append(i);
        i += 1;
    
    #First test case: len = 50
    w7 = []
    i = 1
    while ( i <= 250):
        w7.append(i);
        i += 1;
    
    #First test case: len = 50
    w8 = []
    i = 1
    while ( i <= 300):
        w8.append(i);
        i += 1;
        
    array = [w1,w2,w3,w4,w5,w6,w7,w8]
    return array


# In[5]:


def test_set_worst_case():
    #First test case: len = 50
    w1 = []
    i = 10
    while ( i > 0):
        w1.append(i);
        i -= 1;
        
     #First test case: len = 50
    w2 = []
    i = 20
    while ( i > 0):
        w2.append(i);
        i -= 1;
    
    
    #First test case: len = 50
    w3 = []
    i = 50
    while ( i > 0):
        w3.append(i);
        i -= 1;
    
    
    #First test case: len = 50
    w4 = []
    i = 100
    while ( i > 0):
        w4.append(i);
        i -= 1;
    
    #First test case: len = 50
    w5 = []
    i = 150
    while ( i > 0):
        w5.append(i);
        i -= 1;
    
    #First test case: len = 50
    w6 = []
    i = 200
    while ( i > 0):
        w6.append(i);
        i -= 1;
    
    #First test case: len = 50
    w7 = []
    i = 250
    while ( i > 0):
        w7.append(i);
        i -= 1;
    
    #First test case: len = 50
    w8 = []
    i = 300
    while ( i > 0):
        w8.append(i);
        i -= 1;
        
    array = [w1,w2,w3,w4,w5,w6,w7,w8]
    return array

