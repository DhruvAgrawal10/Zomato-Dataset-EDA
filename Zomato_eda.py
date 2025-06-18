

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r"C:\Users\User\.vscode\PYTHON PRACTICE\EDA\ZOMATO_EDA\Zomatodataset\zomato.csv",encoding="latin-1")
df.head()

df.columns

df.info()

df.describe()

# #Analysis

df.isnull().sum()

[features for features in df.columns if df[features].isnull().sum()>0]

plt.figure(figsize=(12,6))
sns.heatmap(df.isnull(),yticklabels='auto',cbar=False,cmap='viridis')

df_country=pd.read_excel(r"C:\Users\User\.vscode\PYTHON PRACTICE\EDA\ZOMATO_EDA\Zomatodataset\Country-Code.xlsx")
df_country


finaldf=pd.merge(df,df_country,on='Country Code',how='left')

#Pie chart for TOP 3 country distribution
country_names=finaldf.Country.value_counts().index
country_values=finaldf.Country.value_counts().values
plt.pie(x=country_values[:3],labels=country_names[:3],autopct='%1.2f%%')
plt.show()

finaldf.columns

ratings=finaldf.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index().rename(columns={0: 'Rating Count'})
ratings

# # Observations
# * 0 is Unrated
# * 1.8-2.4 is Poor
# * 2.5-3.4 is Average
# * 3.5-3.9 is Good
# * 4-4.4 is Very Good
# * 4.5-4.9 is Excelent
# 

ratings.head()

plt.figure(figsize=(12, 6))
sns.barplot(x="Aggregate rating", y="Rating Count", data=ratings,hue='Rating color',palette=['gray','red','orange','yellow','green','green','dark green'])


#Count Plot
sns.countplot(x="Rating color",data=ratings, hue='Rating color',palette=['gray','red','orange','yellow','green','dark green'])

finaldf[(finaldf['Rating color']=='White') & (finaldf['Aggregate rating']==0) ].groupby('Country').size().reset_index(name="Count")


finaldf[["Country","Currency"]].groupby(["Country","Currency"]).size().reset_index()

finaldf[finaldf['Has Online delivery']=="Yes"].groupby('Country').size().reset_index()

finaldf[['Has Online delivery', 'Country']].groupby(['Has Online delivery', 'Country']).size().reset_index(name='Count')

city_name=finaldf.City.value_counts().index
city_values=finaldf.City.value_counts().values
plt.pie(x=city_values[:4],labels=city_name[:4],autopct='%1.1f%%')
plt.show()

#Top 10 Cuisine 
cuisine_name=finaldf.Cuisines.value_counts().index
cuisine_values=finaldf.Cuisines.value_counts().values
plt.pie(cuisine_values[:10],labels=cuisine_name[:10],autopct='%1.1f%%')
plt.show()

finaldf


