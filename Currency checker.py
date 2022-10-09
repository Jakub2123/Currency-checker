#!/usr/bin/env python
# coding: utf-8

# In[3]:


from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
from requests import get


# In[4]:


DP=    widgets.DatePicker(
        description='Pick a Date',
        disabled=False
)



CU=widgets.Select(
    options=['USD', 'EUR', 'PLN'],
    value='EUR',
    # rows=10,
    description='Currency:',
    disabled=False
)


# In[5]:


DP


# In[6]:


CU


# In[7]:



date=DP.value
date.strftime('%d-%m-%Y')
curr=CU.value


# In[8]:


date.strftime('%d-%m-%Y')


# In[28]:


url = f'http://api.nbp.pl/api/exchangerates/rates/a/{curr}/{date}/'

resp = get(url)
data = resp.json()

#print(data)

rates=data['rates']
first_rate=rates[0]
exchange_rate = first_rate['mid']

print(f'1 {curr} = {exchange_rate} PLN w dniu {date}')


# In[ ]:




