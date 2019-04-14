#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pwd


# In[ ]:


cd C:\Users\Abhishek\Downloads


# ### Question that can analyised from this data set
#  1.Movies which had most and least profit<br>
#  2.Movies with largest and lowest budget<br>
#  3.Movies with most and least earned revenu<br>
#  4.Movies with longest and shortest runtime values<br>
#  5.Average runtime of all the movies<br>
#  6.IN which year we had most no of profitable movies<br>
#  7.Successful genres(with respect to the profitablity of the movie)<br>
#  8.Most frequent cast(with respect to the profitability of the movie)<br>
#  9.Average budget(with respect to the profitability of the movie)<br>
#  10.Average revenue(with respect to the profitability of the movie)<br>
#  11.average duration of the movie(with respect to the profitability of the movie)<br>

# In[65]:


import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
data=pd.read_csv("tmdb-movies.csv")
#data.head()
print(data.dtypes)


# In[6]:


#creating a list of column to be deleted
list_del=['id','imdb_id','popularity','homepage','overview','production_companies','vote_count','vote_average','keywords',
          'budget_adj','revenue_adj']
data=data.drop(list_del,1)
#print(data.dtypes)
#print(data.head(3))


# In[7]:


#Removing the duplicates row
rows,col=data.shape
print("total number of rows and columns are {} and {} respectively in the dataset".format(rows,col))
data.drop_duplicates(keep='first',inplace=True)
rows,col=data.shape
print("After deleting the duplicates rows total number of rows and columns are {} and {} ".format(rows,col))


# In[8]:


#Removing 0's from revenue and budget ciloumn

#below two line replace all the 0's of budget and revenue column with NAN value
remove_list=['revenue','budget']
data[remove_list]=data[remove_list].replace(0,np.NAN)
#removing all the rows which contain contain NAN value either in budget or in revenue column 
data.dropna(subset=remove_list,inplace=True)
print(data.shape)


# In[9]:


#Changing the release date column into standard date format
data.release_date=pd.to_datetime(data['release_date'])
print(data['release_date'].dtypes)


# In[10]:


#Replacing 0's value with NAN value from runtime column
data['runtime']=data['runtime'].replace(0,np.NAN)


# In[11]:


#Changing the datatype of revenue and budget column 
print(data.dtypes)
chg_list=['budget','revenue']
data[chg_list]=data[chg_list].applymap(np.int)
print(data.dtypes)


# In[12]:


#Inserting a new column profit in this dataset
data.insert(2,'profit',data['revenue']-data['budget'])
#print(data.dtypes)
print(data.head(3))


# In[13]:


print(data['profit'].idxmax())


# In[14]:


import pprint
def calculate(pro):
    highest=data[pro].idxmax()
    print(highest)
    highest_detail=pd.DataFrame(data.loc[highest])
    lowest=data[pro].idxmin()
    lowest_detail=pd.DataFrame(data.loc[lowest])
   # collection of data in one frame
    sets=pd.concat([highest_detail,lowest_detail],axis=1)
    return(sets)


# In[15]:


#Movies which had most and least profit
calculate('profit')


# In[16]:


#Movies with largest and lowest budget
calculate('budget')


# In[17]:


#Movies with most and least earned revenue
calculate('revenue')


# In[18]:


#Movies with longest and shortest runtime
calculate('runtime')


# In[19]:


#Average runtime of the movies
print(data['runtime'].mean())


# In[20]:


#Visualising the avg runtime through histogram
plt.figure(figsize=(9,4),dpi=100)
#on X-axis
plt.xlabel('Runtime of the movies',fontsize=20)
plt.ylabel('No of the movies in the Dataset',fontsize=20)
plt.title("Runtime of all the movies")
plt.hist(data['runtime'],rwidth=.8,bins=40)
plt.show()


# In[25]:


#The second plot is the plot of points of runtime of movies
plt.figure(figsize=(10,5),dpi=100)
sns.swarmplot(data['runtime'],color='red')
plt.show()


# In[26]:


print(data['runtime'].describe())


# In[27]:


#Year of release Vs profitability
total_profit=data.groupby('release_year')['profit'].sum()
plt.figure(figsize=(9,6),dpi=120)
plt.xlabel('Release year of the movie in the data set',fontsize=15)
plt.ylabel("toal profit earned by movies",fontsize=15)
plt.title("Total profit VS Released Year",fontsize=25)
plt.plot(total_profit)
plt.show()


# In[28]:


#To find which year made the highest profit
print(total_profit.idxmax())


# In[30]:


#Here we are considering only those movies who have earned more than $40M
profit_list=data[data['profit']>=40000000]
profit_list.index=profit_list.index+1
profit_list.head(3)


# In[31]:


#counting total number of rows in our new dataset
print(len(profit_list))


# In[54]:


#Q.6 succesful genres
def successful_genres(krishna):
    x=profit_list[krishna].str.cat(sep='|')
    x=pd.Series(x.split('|'))
    count=x.value_counts(ascending=False)
    return(count)


# In[53]:


count=successful_genres('genres')
print(count.head(5))


# In[55]:


#Q.7 Most frequent cast
count=successful_genres('cast')
print(count.head(5))


# In[60]:


# Function which return avg
def aver(krishna):
    return(profit_list[krishna].mean())


# In[61]:


#Q.8 Average Budget of the movie
print(aver('budget'))


# In[62]:


#Q.9 Average revenue earned by the movie
print(aver('revenue'))


# In[63]:


#Q.10 average duration of the movie
print(aver('runtime'))


# In[ ]:





# In[ ]:





# In[ ]:




