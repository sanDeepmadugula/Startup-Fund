#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
import dateutil
import squarify


# In[4]:


import os
os.chdir('C:\\Analytics\\MachineLearning\\Indian startup analysis')


# In[5]:


fund_data = pd.read_csv('startup_funding.csv')


# In[6]:


fund_data.columns


# In[7]:


fund_data.head()


# In[8]:


fund_data.shape


# In[9]:


fund_data.info()


# In[10]:


fund_data.isnull().sum().sort_values(ascending=False)


# In[11]:


# Percentage of missing
missing = fund_data.isnull().sum().sort_values(ascending=False)
percentage = (missing/fund_data.isnull().count())*100
percentage


# In[12]:


fund_data.drop(['Remarks'],axis=1,inplace=True)


# In[14]:


# Some adjustments
fund_data['Date'] = fund_data['Date'].replace({'12/05.2015':'12/05/2015'})
fund_data['Date'] = fund_data['Date'].replace({'13/04.2015':'13/04/2015'})
fund_data['Date'] = fund_data['Date'].replace({'15/01.2015':'15/01/2015'})
fund_data['Date'] = fund_data['Date'].replace({'22/01//2015':'22/01/2015'})

fund_data['StartupName'] = fund_data['StartupName'].replace({'Flipkart.com':'Flipkart'})
fund_data['IndustryVertical'] = fund_data['IndustryVertical'].replace({'ECommerce':'eCommerce'})
fund_data['IndustryVertical'] = fund_data['IndustryVertical'].replace({'ecommerce':'eCommerce'})
fund_data['IndustryVertical']=fund_data['IndustryVertical'].replace({"Ecommerce":"eCommerce"})
fund_data['InvestmentType']=fund_data['InvestmentType'].replace({"Crowd funding":"Crowd Funding"})
fund_data['InvestmentType']=fund_data['InvestmentType'].replace({"SeedFunding":"Seed Funding"})
fund_data['InvestmentType']=fund_data['InvestmentType'].replace({"PrivateEquity":"Private Equity"})
fund_data['StartupName']=fund_data['StartupName'].replace({"practo":"Practo"})
fund_data['StartupName']=fund_data['StartupName'].replace({"couponmachine.in":"Couponmachine"})
fund_data['StartupName']=fund_data['StartupName'].replace({"Olacabs":"Ola Cabs"})
fund_data['StartupName']=fund_data['StartupName'].replace({"Ola":"Ola Cabs"})


# In[15]:


# Replace in ',' to '' in AmountInUSD
fund_data['AmountInUSD'] = fund_data['AmountInUSD'].apply(lambda x:float(str(x).replace(",","")))


# In[16]:


print('Minimum Investment')
fund_data['AmountInUSD'].min()


# In[17]:


fund_data[fund_data['AmountInUSD']==16000.0]


# In[18]:


print('Maximum Invetstment')
fund_data['AmountInUSD'].max()


# In[19]:


fund_data[fund_data.AmountInUSD == 1400000000.0]


# Hence Flipkart and Paytm were the statups that had the maximum investment

# In[20]:


fund_data[fund_data['StartupName']=='Flipkart']


# In[21]:


fund_data[fund_data['StartupName']=='Paytm']


# In[22]:


fund_data['AmountInUSD'].mean()


# In[23]:


# Total investment
fund_data['AmountInUSD'].sum()


# Lets see number of investment per month

# In[24]:


fund_data.columns


# In[26]:


fund_data["yearmonth"] = (pd.to_datetime(fund_data['Date'],format='%d/%m/%Y').dt.year*100)+(pd.to_datetime(fund_data['Date'],format='%d/%m/%Y').dt.month)
temp = fund_data['yearmonth'].value_counts().sort_values(ascending = False)
print("Number of funding per month in decreasing order (Funding Wise)\n\n",temp)
year_month = fund_data['yearmonth'].value_counts()


# In[27]:


# funding distribution
plt.figure(figsize=(15,8))
sns.barplot(year_month.index, year_month.values,alpha=.9)
plt.xticks(rotation='vertical')
plt.xlabel('Year-Month of transaction',fontsize=12)
plt.ylabel('Number of funding made',fontsize=12)
plt.title('Year-Month- Number of Funding disribution',fontsize=16)
plt.show()


# From above
# 1. 2015 July and August had the highest inverstment because of 
#    Digital India Campaign by Govt Of India
# 2. Jan 2016 had highest inverstment because of 'Startup India Initiative'
# 3. Due demonetization the investment had lowered from Nov 2016 to july 2017
# 

# In[28]:


# Year-month-Amount of Funding distribution
plt.figure(figsize=(15,8))
sns.barplot(fund_data['yearmonth'],fund_data['AmountInUSD'],alpha=0.9)
plt.xticks(rotation='vertical')
plt.xlabel('YearMonth', fontsize=12)
plt.ylabel('Amount Of Investments', fontsize=12)
plt.title('YearMonth - Number of fundings distribution', fontsize=16)
plt.show()


# March 17 and May 17 had the maximum inverstment bcz Flipkart and Paytm were founded then

# In[29]:


# Total number of statrtups
len(fund_data['StartupName'])


# In[30]:


#unique startups
len(fund_data['StartupName'].unique())


# In[31]:


# startups got funding more than one times
tot = (fund_data['StartupName'].value_counts()).values
c = 0
for i in tot:
    if i>1:
        c = c+1
print('Startups that got funding more than 1 times=',c)


# In[32]:


fund_count = fund_data['StartupName'].value_counts()
fund_count = fund_count.head(15)
print(fund_count)


# In[33]:


# top 15 companies that secured 4 or more than 4 fundins in vizualization
plt.figure(figsize=(15,8))
sns.barplot(fund_count.index, fund_count.values,alpha=0.9)
plt.xticks(rotation='vertical')
plt.xlabel('Startups', fontsize=12)
plt.ylabel('Number of fundings made',fontsize=12)
plt.title('Startups-Number of fundings distribution',fontsize=16)
plt.show()


# In[34]:


# talk about Industry verticals
len(fund_data['IndustryVertical'].unique())


# In[35]:


IndustryVert = fund_data['IndustryVertical'].value_counts().head(20)
print(IndustryVert)


# In[36]:


plt.figure(figsize=(15,8))
sns.barplot(IndustryVert.index,IndustryVert.values,alpha=0.9)
plt.xticks(rotation='vertical')
plt.xlabel('Industry Verticals', fontsize=12)
plt.ylabel('Number of fundings made', fontsize=12)
plt.title("Industry Verticals-Number of fundings distribution", fontsize=16)
plt.show()


# It shows Consumer Internet startups are the most

# In[43]:


# talking about subvertical
sub_vertical = fund_data['SubVertical']
print('Total number of subverticals:',len(sub_vertical.unique()))


# In[44]:


sub_vertical=sub_vertical.value_counts().head(25)
print(sub_vertical)


# In[45]:


plt.figure(figsize=(15,8))
sns.barplot(sub_vertical.index, sub_vertical.values, alpha=0.9)
plt.xticks(rotation='vertical')
plt.xlabel('Industry Sub Verticals', fontsize=12)
plt.ylabel('Number of fundings made', fontsize=12)
plt.title("Industry Sub Verticals-Number of fundings distribution", fontsize=16)
plt.show()


# Online Pharmacy leads the way with 9 investments

# In[46]:


# Investment Types
Investment_Types = fund_data['InvestmentType'].value_counts()
print(Investment_Types)


# In[48]:


plt.figure(figsize=(12,5))
sns.barplot(Investment_Types.index, Investment_Types.values, alpha=0.9)
plt.xticks(rotation='vertical')
plt.xlabel('Investment Type', fontsize=12)
plt.ylabel('Number of fundings made', fontsize=12)
plt.title("Investment Type - Number of fundings distribution", fontsize=16)
plt.show()


# Seed funding and Private equity is the most preffered way of inverstments by investors

# In[49]:


# Cities
len(fund_data['CityLocation'].unique())


# In[50]:


fund_data['CityLocation'].value_counts().head(10)


# In[52]:


fund_city = fund_data['CityLocation'].value_counts()
plt.figure(figsize=(16,9))
sns.barplot(fund_city.index, fund_city.values, alpha=0.9)
plt.xticks(rotation='vertical')
plt.xlabel('City', fontsize=12)
plt.ylabel('Number of fundings made', fontsize=24)
plt.title("City - Number of fundings distribution", fontsize=28)
plt.show()


# bangalore is the most attract for investors
# 

# In[53]:


fund_data['InvestorsName'] = fund_data['InvestorsName'].fillna('No info Available')
names = fund_data['InvestorsName'][~pd.isnull(fund_data['InvestorsName'])]
print(names.head())


# In[54]:


Inverstor_list = fund_data['InvestorsName'].str.split(',').apply(pd.Seriesries)


# In[55]:


Inverstor_list.head()


# In[56]:


print('Combining all columns into one')
df = Inverstor_list.stack(dropna=False).reset_index(drop=True).to_frame('newinvest')
print(df.head(10))


# In[57]:


InvestorsName = df.dropna(axis=0,how='all')


# In[59]:


# Correcting typos
InvestorsName=InvestorsName.replace({" Sequoia Capital":"Sequoia Capital"})
InvestorsName=InvestorsName.replace({"Undisclosed investors":"Undisclosed Investors"})
InvestorsName=InvestorsName.replace({"undisclosed investors":"Undisclosed Investors"})
InvestorsName=InvestorsName.replace({"undisclosed Investors":"Undisclosed Investors"})
InvestorsName=InvestorsName.replace({"Undisclosed":"Undisclosed Investors"})
InvestorsName=InvestorsName.replace({"Undisclosed Investor":"Undisclosed Investors"})
InvestorsName=InvestorsName.replace({" Accel Partners":"Accel Partners"})
InvestorsName=InvestorsName.replace({" Blume Ventures":"Blume Ventures"})
InvestorsName=InvestorsName.replace({" SAIF Partners":"SAIF Partners"})
InvestorsName=InvestorsName.replace({" Kalaari Capital":"Kalaari Capital"})


# In[60]:


# total investments
len(InvestorsName['newinvest'])


# In[61]:


InvestorsName.head(10)


# In[62]:


# unique investors
InvestorsName['newinvest'] = InvestorsName['newinvest'].str.strip()
print(len(InvestorsName['newinvest'].unique()))


# In[63]:


Investors_top50 = InvestorsName['newinvest'].value_counts().head(50)
print(Investors_top50)


# In[68]:


# Plot for investors
sns.barplot(Investors_top50.index, Investors_top50.values, alpha=0.9)
plt.xticks(rotation='vertical')
plt.xlabel('Investors', fontsize=12)
plt.ylabel('Number of Startups Invested In', fontsize=16)
plt.title("Investors - Investment distribution", fontsize=30)
plt.show()


# In[69]:


# Squarify plot for inverstors
plt.figure(figsize=(16,9))
squarify.plot(sizes=Investors_top50.values,label=Investors_top50.index, value=Investors_top50.values,color=["#FF6138","#FFFF9D","#BEEB9F", "#79BD8F","#684656","#E7EFF3"], alpha=0.6)
plt.title('Distribution of Investors and Investments Done')


# From above
# 
# The plot shows that Undisclosed Investors have done the most investments.
# Followed by Sequoia Capitals with 64 Investments
# Individuals like Ratan Tata( Former chairman of Tata Sons) and Rajan Anandan( VP,Google SE Asia and India) have invested in 30 and 25 companies respectively, most by any individuals

# In[ ]:




