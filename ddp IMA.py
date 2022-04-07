#!/usr/bin/env python
# coding: utf-8

# In[5]:


def function1() :
    n = input("please enter your string")
    lower = 0  
    upper = 0  
    for c in n:
        if c.isupper():
            upper += 1
        elif c.islower():
            lower += 1
    print('lowercase: %d,uppercase: %d' %(lower,upper))
function1()
        


# In[ ]:





# In[ ]:





# In[ ]:




