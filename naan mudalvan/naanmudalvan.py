#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import random as rd
import matplotlib.pyplot as plt
from math import sqrt


# In[4]:


import pandas as pd
df= pd.read_csv("Downloads\houseprice.csv")
df.head()


# In[5]:


df.dtypes


# In[7]:


df.lot_area_renov.mean()


# In[8]:


df.lot_area_renov.median()


# In[9]:


df.describe()


# In[17]:


import pandas as pd
df= pd.read_csv("Downloads\houseprice.csv")
df.head()


# In[19]:


#frequency
count = df.groupby(['lot_area_renov']).count()
print(count)


# In[12]:


#univariate 
sns.histplot(data = df, x = "lot_area_renov", color = "black")


# In[14]:


import numpy as np

np.random.seed(1983)

norm = pd.Series(np.random.randn(1000))

sns.histplot(x = norm, color = "black", bins = 8)


# In[16]:


norm.describe()


# In[17]:


df.lot_area_renov.skew()


# In[18]:


norm.skew()


# In[19]:


df.lot_area_renov.kurtosis()


# In[20]:


norm.kurtosis()


# In[21]:


sns.kdeplot(data = df, x = "lot_area_renov")


# In[22]:


sns.kdeplot(data = df, x = "lot_area_renov", shade = True, color = "green")


# In[25]:


sns.displot(data = df, x = "lot_area_renov", bins = 10, kde = True)


# In[26]:


sns.boxplot(data = df, y = "lot_area_renov")


# In[27]:


sns.boxplot(data = df, x = "lot_area_renov")


# In[28]:


sns.violinplot(data = df, x = "lot_area_renov")


# In[29]:


sns.violinplot(data = df, y = "lot_area_renov")


# In[ ]:





# In[34]:


import pandas as pd
import seaborn as sns
df = pd.read_csv('Downloads\houseprice.csv')
print(df.head())


# In[35]:


sns.histplot(data['Lattitude'])


# In[36]:


sns.countplot(data['number of bedrooms'])


# In[37]:


#piechart


# In[38]:


x = data['number of bedrooms'].value_counts()
plt.pie(x.values,
        labels=x.index,
        autopct='%1.1f%%')
plt.show()


# In[1]:


#bivariate


# In[5]:


import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import seaborn as sns
df = pd.read_csv('Downloads\houseprice.csv')
print(df.head())


# In[67]:


sns.scatterplot(x= data['Lattitude'],
                y= data['Longitude'])


# In[7]:


import matplotlib.pyplot as plt
data=df
plt.figure(figsize=(15, 5))
sns.barplot(x=data['lot area'], y=data['Postal Code'])
plt.xticks(rotation='90')


# In[22]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import scale
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from scipy import stats


# In[27]:


data = pd.read_csv("Downloads\houseprice.csv")
primary_results = pd.read_csv("Downloads\houseprice.csv")
data.loc[:, "Date":"Built Year"].describe()


# In[28]:


from IPython.display import display, HTML

# figures inline in notebook
get_ipython().run_line_magic('matplotlib', 'inline')

np.set_printoptions(suppress=False)

DISPLAY_MAX_ROWS = 20  # number of max rows to print for a DataFrame
pd.set_option('display.max_rows', DISPLAY_MAX_ROWS)


# In[32]:


pd.plotting.scatter_matrix(data.loc[:, "Date":"Built Year"], diagonal="kde")
plt.tight_layout()
plt.show()


# In[34]:


pd.plotting.scatter_matrix(data.loc[:, "Number of schools nearby":"Distance from the airport"], diagonal="kde")
plt.show()


# In[35]:


sns.lmplot("Price", "Postal Code", data, hue="Built Year", fit_reg=False);


# In[36]:


ax = data.loc[:, "Number of schools nearby":"Distance from the airport"].plot()
ax.legend(loc='center right', bbox_to_anchor=(1, 0.5));


# In[37]:


#descriptive statistics


# In[44]:


df = pd.read_csv("Downloads\houseprice.csv")
df.sum(1)


# In[45]:


df.mean()


# In[46]:


df.median()


# In[47]:


df.std()


# In[48]:


df.describe()


# In[ ]:


#handle missing values

