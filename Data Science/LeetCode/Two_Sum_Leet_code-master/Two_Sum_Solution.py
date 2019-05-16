#!/usr/bin/env python
# coding: utf-8

# In[3]:


def twoSum(nums, target):
    for a in range(0, len(nums)-1):
         for b in range(a+1, len(nums)):
            if (nums[a] + nums[b] == target):
                return [a,b]


# In[4]:


twoSum([2, 7, 11, 15],9)


# In[ ]:




