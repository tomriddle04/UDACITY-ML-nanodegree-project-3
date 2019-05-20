#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pwd


# In[ ]:


cd C:\Users\Abhishek\Downloads


# Overview:
# 
# To complete my Data analyst project I am using TMDB movies dataset.
# 
# This data contains information about many movies collected from the movie dataset,including user rating and revenue.it consists
# of 21 column such as revenue,budget,vote_count,imdb_id etc.
# 
# 
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

# In[ ]:


#importing important package and library which is used 
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
data=pd.read_csv("tmdb-movies.csv")
#data.head()
print(data.dtypes)


# Data Wrangling
# 
# for analysis we will be keeping only relevent data and deleting the unused data so that we can make our calculation easy and understandable.

# In[4]:


data.head(5)


# #### Observation from the data set
# 
# - No unit of currency is mentioned in the dataset.So for my analysis I will take it as dollar as it is the most used
#  international currency.
# - vote_count is different for all the movies, so we cannot directly concluded the popularity of the movies based on the average
# vote count.

# #### Data cleaning (Removing the unused information from the dataset)
# 
# Important observation regarding this process
# 
# - We need to remove unused column such as id,idmb_id,vote_count,production_company,keywords etc.
# - Removing the duplicate rows if it exists.
# - Some movies in the dataset have Zero budget or Zero revenue means their value is not recorded so we will be discarding such 
#   entries. 
# - Changing release date column into date format.
# - Replacing zero with NAN in runtime column. 
# - Changing format of budget and revenue column.
# 

# #### 1.Removing unused columns.
# 
# columns that we need to delete are:- id,imdb_id,popularity,budget_adj,revenue_adj,homepage,keywords,overview,vote_counts,
#     production_companies and vote_average

# In[37]:


#creating a list of column to be deleted
list_del=['id','imdb_id','popularity','homepage','overview','production_companies','vote_count','vote_average','keywords',
          'budget_adj','revenue_adj']
data.drop(list_del,1)
#print(data.dtypes)
#print(data.head(3))


# ####  2.Removing the duplicacy in the rows(if any).

# In[9]:


#Removing the duplicates row
rows,col=data.shape
print("total number of rows and columns are {} and {} respectively in the dataset".format(rows,col))
data.drop_duplicates(keep='first',inplace=True)
rows,col=data.shape
print("After deleting the duplicates rows total number of rows and columns are {} and {} ".format(rows,col))


# #### 3.Removing 0's from budget and the revenue columns

# In[10]:


#Removing 0's from revenue and budget ciloumn

#below two line replace all the 0's of budget and revenue column with NAN value
remove_list=['revenue','budget']
data[remove_list]=data[remove_list].replace(0,np.NAN)
#removing all the rows which contain contain NAN value either in budget or in revenue column 
data.dropna(subset=remove_list,inplace=True)
print(data.shape)


# ####  4.Changing the release date column into standard date format 

# In[12]:


#Changing the release date column into standard date format
data.release_date=pd.to_datetime(data['release_date'])
print(data['release_date'].dtypes)


# ####  5.Replacing zero with NAN in runtime column

# In[38]:


#Replacing 0's value with NAN value from runtime column
data['runtime']=data['runtime'].replace(0,np.NAN)


# In[14]:


#Changing the datatype of revenue and budget column 
print(data.dtypes)
chg_list=['budget','revenue']
data[chg_list]=data[chg_list].applymap(np.int)
print(data.dtypes)


# ### Exploratory Data Analysis
# 
# 
# 1.Calculating the profit of the each movie

# In[15]:


#Inserting a new column profit in this dataset
data.insert(2,'profit',data['revenue']-data['budget'])
#print(data.dtypes)
print(data.head(3))


# In[16]:


print(data['profit'].idxmax())


# #### Research Question 1: Movies which had most and least profit

# In[17]:


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


# In[18]:


#Movies which had most and least profit
calculate('profit')


# Column with id 1386 shows the highest earned profit i.e 2544505847
# 
# Whereas the column with id 2244 shows the lowest earned profit i.e -413912431

# #### Research Question 2: Movies with largest and lowest budgets

# In[19]:


#Movies with largest and lowest budget
calculate('budget')


# Column with id 2244 shows the largest budget  i.e  425000000 dollar
# 
# Whereas the column with id  2618  shows the smallest budget i.e 1 dollar

# #### Research Question 3: Movies with most and least earned revenue

# In[20]:


#Movies with most and least earned revenue
calculate('revenue')


# column with id  1386 shows the largest revenue earned i.e  2781505847 dollar
# 
# Whereas the column with id 5067 shows the smallest revenue earned  i.e 2 dollar

# ####  Research Question 4: Movies with longest and shortest runtime

# In[21]:


#Movies with longest and shortest runtime
calculate('runtime')


# Column with id 2107 shows the longest runtime  i.e 338
# 
# Whereas the column with id  5162 shows the shortest runtime i.e 15 minutes

# #### Research Question 5: Average runtime of the movies

# In[22]:


#Average runtime of the movies
print(data['runtime'].mean())


# So the average runtime a movie is 109.22029060716139 minutes .Lets analyse it in a visual form i.e by grapical approach.

# In[23]:


#Visualising the avg runtime through histogram
plt.figure(figsize=(9,4),dpi=100)
#on X-axis
plt.xlabel('Runtime of the movies',fontsize=20)
plt.ylabel('No of the movies in the Dataset',fontsize=20)
plt.title("Runtime of all the movies")
plt.hist(data['runtime'],rwidth=.8,bins=40)
plt.show()


# The distribution of the above formed graph is positively skewed or right skewed .Most of the movies are timed between 80 to 115
# minutes.Almost 1000 and more no of movies fall in this criteria.

# In[24]:


#The second plot is the plot of points of runtime of movies
plt.figure(figsize=(10,5),dpi=100)
sns.swarmplot(data['runtime'],color='red')
plt.show()


# In[25]:


print(data['runtime'].describe())


# Here the plot generated above give a visual of complete distribution of runtime of movies.
# 
# By looking at both the plot and calculations, we conclude that...
# 
# 1.25% of movies have a runtime of less than than 95 minutes.
# 
# 2.50% of movies have a runtime of less than 106 minutes.
# 
# 3.75% of movies have a runtime of less than 119 minutes.

# #### Research Question 6: Year of release Vs Profitability

# In[26]:


#Year of release Vs profitability
total_profit=data.groupby('release_year')['profit'].sum()
plt.figure(figsize=(9,6),dpi=120)
plt.xlabel('Release year of the movie in the data set',fontsize=15)
plt.ylabel("toal profit earned by movies",fontsize=15)
plt.title("Total profit VS Released Year",fontsize=25)
plt.plot(total_profit)
plt.show()


# In[27]:


#To find which year made the highest profit
print(total_profit.idxmax())


# So we can colclude both grapically as well as by calculations that year 2015 was the year where movies made the highest profit
# 
# We are now done with analysing the given dataset.We will now find characteristics of profitable movies.

# ####  With respect to the profitable movies
# 
# before moving further we need clean our data again.We will be considering only those movies who have earned a significant 
# amount of profit.

# In[28]:


#Here we are considering only those movies who have earned more than $40M
profit_list=data[data['profit']>=40000000]
profit_list.index=profit_list.index+1
profit_list.head(3)


# In[29]:


#counting total number of rows in our new dataset
print(len(profit_list))


# so our dataset reduced to 1493

# ####  Research Question 6: Succesful Genres

# In[30]:


#Q.6 succesful genres
def successful_genres(krishna):
    x=profit_list[krishna].str.cat(sep='|')
    x=pd.Series(x.split('|'))
    count=x.value_counts(ascending=False)
    return(count)


# In[31]:


count=successful_genres('genres')
print(count.head(5))


# Drama Genres is most popular among all Genres

# #### Research Question 7: Most frequent cast

# In[32]:


#Q.7 Most frequent cast
count=successful_genres('cast')
print(count.head(5))


# As expected Tom Cruise is on the top with total 27 cast followed by Tom Hanks with 26 and then Brad pitt 25.

# #### Research Question 8: Average Budget of the movies

# In[33]:


# Function which return avg
def aver(krishna):
    return(profit_list[krishna].mean())


# In[39]:


#Q.8 Average Budget of the movie
print(aver('budget'))


# So the movies having profit of 40 million and more have an average budget of 57 million dollar.

# #### Research question 9: Average Revenue earned by the movies

# In[35]:


#Q.9 Average revenue earned by the movie
print(aver('revenue'))


# So the movies having profit of 40 million dollar and more have an average revenue of 236 million dollar.

# #### Research Question 10: Average duration of the movies 

# In[36]:


#Q.10 average duration of the movie
print(aver('runtime'))


# So the movies having profit of 40 million dollar and more have an average duration of 113 minutes.

# In[ ]:





# In[ ]:




