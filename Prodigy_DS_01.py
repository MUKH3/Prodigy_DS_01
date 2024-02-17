#!/usr/bin/env python
# coding: utf-8

# In[69]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[74]:


# Loading the dataset
df = pd.read_csv("C:/Users/Trishit/Documents/Prodigy Infotech/Data Science/Task 1/flavors_of_cacao.csv", encoding = 'latin1')


# In[75]:


# Printing the dataest
df


# Here we see that the column-names have not been properly specified, so, we rename the column-names of the dataset as follows.

# In[76]:


# Rename columns
df.columns = ['Company', 'Specific Bean Origin', 'REF', 'Review Date',
              'Cocoa Percent', 'Company Location', 'Rating', 'Bean Type', 'Broad Bean Origin']


# In[77]:


# Printing the dataset
df


# In[78]:


# Structure of the dataset
df.shape


# In[79]:


# Check for null values
df.isnull().sum()


# Since we see that we have two null values, we drop the null values. There is no other option than dropping the null values as the information that is missing cannot be logically replaced by any values.

# In[80]:


# Remove null values
df.dropna(inplace=True)


# In[81]:


# Printing the dataset
df


# In[82]:


# Check for null values
df.isnull().sum()


# In[83]:


# Structure of the dataset
df.shape


# Since there are no more null values, we move ahead

# In[84]:


# Preprocessing - Convert Cocoa Percent to numeric
df['Cocoa Percent'] = df['Cocoa Percent'].str.rstrip('%').astype('float') / 100


# In[85]:


# Summary statistics
df.describe()


# Now, we are going to analyse using the graphical methods.

# In[86]:


# Plot bar chart for frequency of cocoa products based on ratings
ratings_range = [i / 2 for i in range(1, 11)]  # Generate ratings from 0.5 to 5.0
plt.figure(figsize=(12, 6))
df['Rating'].value_counts().reindex(ratings_range, fill_value=0).sort_index().plot(kind='bar', color='skyblue')
plt.title('Frequency of Cocoa Products by Ratings')
plt.xlabel('Ratings')
plt.ylabel('Frequency')
plt.xticks(rotation=0)  # Rotate x-axis labels
# Add text annotations on top of each bar
for i, count in enumerate(ratings_counts):
    plt.text(i, count, str(count), ha='center', va='bottom')
plt.show()


# Based on the ratings, we can say that the majority of the cocoa products(392) have received a rating of 3.5

# In[95]:


# Plot bar chart for frequency of cocoa products based on countries
plt.figure(figsize=(20, 8))
country_counts = df['Company Location'].value_counts()
country_counts.plot(kind='bar', color='salmon')
plt.title('Frequency of Cocoa Products by Country')
plt.xlabel('Country')
plt.ylabel('Frequency')
plt.xticks(rotation=90)  # Rotate x-axis labels 

# Add text annotations on top of each bar
for i, count in enumerate(country_counts):
    plt.text(i, count, str(count), ha='center', va='bottom')

plt.show()


# Based on the graph it is very evident that most of the companies(763) are located in the USA.

# In[88]:


# Plot bar chart for frequency of cocoa products based on bean type
plt.figure(figsize=(18, 6))
bean_counts = df['Bean Type'].value_counts()
bean_counts.plot(kind='bar', color='green')
plt.title('Frequency of Cocoa Products by Bean Type')
plt.xlabel('Bean Type')
plt.ylabel('Frequency')
plt.xticks(rotation=90)  # Rotate x-axis labels

# Add text annotations on top of each bar with custom color
for i, count in enumerate(bean_counts):
    plt.text(i, count, str(count), ha='center', va='bottom')

plt.show()


# Based on the graph, it can be interpreted that Bean type A is the widely used cocoa.

# In[94]:


# Define custom colors
bar_color = 'orange'
text_color = 'black'

# Plot bar chart for frequency of cocoa products based on broad bean origin
plt.figure(figsize=(30, 10))
broad_bean_counts = df['Broad Bean Origin'].value_counts()
broad_bean_counts.plot(kind='bar', color=bar_color)
plt.title('Frequency of Cocoa Products by Broad Bean Origin')
plt.xlabel('Broad Bean Origin')
plt.ylabel('Frequency')
plt.xticks(rotation=90)  # Rotate x-axis labels 

# Add text annotations on top of each bar with custom color
for i, count in enumerate(broad_bean_counts):
    plt.text(i, count, str(count), ha='center', va='bottom', color=text_color)

plt.show()


# Based on the graph it can be interpreted that mostly the South American countries like Venezuela(214), Ecuador(193), Peru(165) are top countries from where the majority of the beans have been obtained.

# In[103]:


# Plot histogram for review date of cocoa products
plt.figure(figsize=(18, 6))
plt.hist(df['Review Date'], bins=10, color='lightblue', edgecolor='black')
plt.title('Histogram of Review Dates')
plt.xlabel('Review Date')
plt.ylabel('Frequency')
plt.show()


# As per the histogram, it can be concluded that the majority of the products have been reviewed 2014-2015.

# In[ ]:




