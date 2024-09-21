#!/usr/bin/env python
# coding: utf-8

# In[1]:


from itertools import permutations

string = "yasuj"

all_permutations = [''.join(p) for p in permutations(string)]


valid_permutations = [p for p in all_permutations if p[0] < p[-1]]


print(len(valid_permutations))


# In[ ]:




