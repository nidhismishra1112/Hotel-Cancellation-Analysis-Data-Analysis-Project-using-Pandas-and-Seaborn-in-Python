#!/usr/bin/env python
# coding: utf-8

# # import libraries
# 

# In[11]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[12]:


df= pd.read_csv(r'C:\Users\Admin\Contacts\Desktop\hotel_bookings 2.csv')


# In[13]:


df


# In[14]:


df.head()


# In[15]:


df.tail(10)


# In[16]:


df.shape


# In[17]:


df.columns


# In[18]:


df.info()


# In[19]:


df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])


# In[20]:


df.info()


# In[21]:


df.describe(include='object')


# In[22]:


for col in df.describe(include='object').columns:
    print(col)
    print(df[col].unique())
    print('-'*50)


# In[23]:


df.isnull().sum()


# In[24]:


df.drop(['company','agent'],axis=1,inplace= True)
df.dropna(inplace=True)


# In[25]:


df.isnull().sum()


# In[26]:


df.describe()


# In[27]:


df['adr'].plot (kind = 'box')


# In[28]:


df=df[df['adr']<5000]


# # DATA ANALYSIS AND VISUALIZATION

# In[29]:


cancelled_perc=df['is_canceled'].value_counts(normalize=True)
print(cancelled_perc)


# In[30]:


cancelled_perc=df['is_canceled'].value_counts(normalize=True)
print(cancelled_perc)

plt.figure(figsize=(5,4))
plt.title('Reservation status count')
plt.bar(['Not Canceled','Canceled'],df['is_canceled'].value_counts(),edgecolor='k',width=0.7)
plt.show()


# In[31]:


plt.figure(figsize=(8,5))
ax1= sns.countplot(x = 'hotel', hue = 'is_canceled', data = df, palette = 'Blues')
legend_labels,_= ax1. get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1,1))
plt.title('Reservation status in different hotels',size=20)
plt.xlabel('hotel')
plt.ylabel('number of reservations')
plt.legend(['not_canceled','canceled'])
plt.show()


# In[33]:


resort_hotel = df[df['hotel']=='Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize = True)


# In[34]:


City_hotel = df[df['hotel']=='City Hotel']
City_hotel['is_canceled'].value_counts(normalize = True)


# In[35]:


resort_hotel = resort_hotel.groupby('reservation_status_date')[['adr']].mean()
City_hotel = City_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[38]:


plt.figure(figsize=(20,8))
plt.title('Average daily rate in city and resort hotel',fontsize=30)
plt.plot(resort_hotel.index, resort_hotel['adr'],label='resort hotel')
plt.plot(City_hotel.index, City_hotel['adr'],label='City hotel')
plt.legend(fontsize=20)
plt.show()


# In[42]:


df['month']=df['reservation_status_date'].dt.month
plt.figure(figsize=(16,8))
ax1= sns.countplot(x = 'month', hue = 'is_canceled', data = df, palette = 'bright')
legend_labels,_= ax1. get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1,1))
plt.title('Reservation status per month',size=20)
plt.xlabel('month')
plt.ylabel('number of reservations')
plt.legend(['not_canceled','canceled'])
plt.show()


# In[48]:


plt.figure(figsize=(15,8))
plt.title('ADR per month',fontsize = 30)
sns.barplot(x= 'month',y= 'adr', data = df[df['is_canceled'] == 1].groupby('month')[['adr']].sum().reset_index())

plt.show()


# In[49]:


cancelled_data=df[df['is_canceled'] == 1]
top_10_country = cancelled_data['country'].value_counts()[:10]
plt.figure(figsize=(8,8))
plt.title('Top 10 Countries with Reservation Cancelled ',fontsize = 30)
plt.pie(top_10_country, autopct = '%.2f', labels = top_10_country.index)
plt.show()


# In[50]:


df['market_segment'].value_counts()


# In[51]:


df['market_segment'].value_counts( normalize = True)


# In[52]:


cancelled_data['market_segment'].value_counts( normalize = True)


# In[55]:


cancelled_df_adr = cancelled_data.groupby('reservation_status_date')[['adr']].mean()
cancelled_df_adr.reset_index(inplace = True)
cancelled_df_adr.sort_values('reservation_status_date', inplace = True)

not_cancelled_data= df[df['is_canceled'] == 0]
not_cancelled_df_adr = not_cancelled_data.groupby('reservation_status_date')[['adr']].mean()
not_cancelled_df_adr.reset_index(inplace = True)
not_cancelled_df_adr.sort_values('reservation_status_date', inplace = True)



plt.figure(figsize=(20,6))
plt.title('Average Daily Rate',fontsize = 30)
plt.plot(not_cancelled_df_adr['reservation_status_date'],not_cancelled_df_adr ['adr'],label = 'not canceled')
plt.plot(cancelled_df_adr['reservation_status_date'],cancelled_df_adr ['adr'],label = 'canceled')
plt.legend()


# In[59]:


cancelled_df_adr = cancelled_df_adr[(cancelled_df_adr['reservation_status_date']>'2016') &
(cancelled_df_adr['reservation_status_date']<'2017-09')]

not_cancelled_df_adr = not_cancelled_df_adr[(not_cancelled_df_adr['reservation_status_date']>'2016') &
(not_cancelled_df_adr['reservation_status_date']<'2017-09')]


# In[61]:


plt.figure(figsize=(20,6))
plt.title('Average Daily Rate',fontsize = 30)
plt.plot(not_cancelled_df_adr['reservation_status_date'],not_cancelled_df_adr ['adr'],label = 'not canceled')
plt.plot(cancelled_df_adr['reservation_status_date'],cancelled_df_adr ['adr'],label = 'canceled')
plt.legend(fontsize = 20)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




