#!/usr/bin/env python
# coding: utf-8

# In[9]:


#get user's hourly rate of pay
rate=float(input("How much do you make an hour?: " ))
#get user's hours worked
hours=float(input("How many hours did you work this week?: "))
#calculate weekly pay
pay= rate * hours
#output message
print(f"Your weekly pay is: ${pay:.2f}")


# In[ ]:




