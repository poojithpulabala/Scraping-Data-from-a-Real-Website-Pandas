#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests


# In[4]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[45]:


print(soup)



# In[ ]:





# In[46]:


soup.find('table', class_ = 'wikitable sortable')



# In[47]:


table = soup.find_all('table')[1]


# In[48]:


print(table)


# In[55]:


world_titles = table.find_all('th')


# In[56]:


world_titles


# In[58]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[59]:


import pandas as pd


# In[60]:


df = pd.DataFrame(columns = world_table_titles)
df


# In[66]:


column_data = table.find_all('tr')


# In[77]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
   
    length =len(df)
    df.loc[length] = individual_row_data
    
    


# In[78]:


df


# In[79]:


df.to_csv(r'C:\Users\chowd\OneDrive\Desktop\Poojith Resume\Scraping Data.csv', index = False)


# In[ ]:




