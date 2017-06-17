
# coding: utf-8

# In[5]:

path_to_zip_file = "datasets.zip"
directory_to_extract_to = ""

import zipfile
zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
zip_ref.extractall(directory_to_extract_to)
zip_ref.close()


# In[6]:

import pandas as pd

Location = "datasets/axisdata.csv"
df= pd.read_csv(Location, header=None)


# In[7]:

df.head()


# In[8]:

df.columns = ['First','Last', 'Gender', 'HoursWorked', 'SalesTraining','YearsExperience','CarsSold']


# In[9]:

df.head()


# In[10]:

# Drop Duplicates

df.drop_duplicates()


# In[11]:

# remove outliers

import pandas as pd

Location = "datasets/axisdata.csv"
df = pd.read_csv(Location)

meanhours = df['Hours Worked'].mean()
sthours = df['Hours Worked'].std()
toprange = meanhours + sthours*1.96
botrange = meanhours +sthours*1.96

copydf = df
copydf = copydf.drop(copydf[copydf['Hours Worked'] > toprange].index)
copydf = copydf.drop(copydf[copydf['Hours Worked'] < botrange].index)
copydf


# In[12]:

df.columns = ['First','Last', 'Gender', 'HoursWorked', 'SalesTraining','YearsExperience','CarsSold']


# In[13]:

# Average Cars Sold 

df['CarsSold'].mean()


# In[14]:

# max cars sold per month

df['CarsSold'].max()


# In[15]:

# min cars sold per month

df['CarsSold'].min()


# In[16]:

# average cars sold per month by gender (F)

female = df['Gender'] =='F'
df[female]['CarsSold'].mean()



# In[17]:

# average cars sold per month by gender (F)

male = df['Gender'] =='M'
df[male]['CarsSold'].mean()


# In[18]:

# average hours worked by people selling > 3 cars per month

hivol = df['CarsSold']>=3

df[hivol]['HoursWorked'].mean()


# In[19]:

# average years of experience

df['YearsExperience'].mean()


# In[20]:

# average years of experience for people selling > 3 cars per month

hivol = df['CarsSold']>=3

df[hivol]['YearsExperience'].mean()


# In[21]:

# average cars sold by training status 

pd.pivot_table(df, index=['SalesTraining'])


# In[ ]:

# Sales training is the best indicator of car sales

