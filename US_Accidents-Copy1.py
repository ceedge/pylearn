#!/usr/bin/env python
# coding: utf-8

# In[1]:


from statistics import mean
import pandas as pd
import wget
import numpy as np
import warnings
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import calendar
import os
from datetime import datetime


# In[ ]:





# In[ ]:





# In[2]:


os.getcwd()


# In[3]:


path='E:\\US_Accidents_Dec21_updated.csv'


# In[4]:


df=pd.read_csv(path)


# In[5]:


df


# In[6]:


month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct', 'Nov','Dec']


# In[7]:


df.head()


# In[8]:


df2=pd.read_csv(path,usecols=['End_Time'])


# In[ ]:





# In[9]:


df2
df2.dtypes


# In[10]:


df2['End_Time']=pd.to_datetime(df['End_Time'], format='%Y-%m-%d %H:%M:%S')


# In[11]:


df2.dtypes


# In[12]:


df2['Year']= df2['End_Time'].dt.year


# In[13]:


df2


# In[14]:


df2['Quarter']= df2['End_Time'].dt.quarter


# In[15]:


df2


# In[16]:


df2['Month']= df2['End_Time'].dt.month


# In[17]:


df2['Day']= df2['End_Time'].dt.day


# In[18]:


df2['Hour']= df2['End_Time'].dt.hour


# In[19]:


df2['DayofWeek']= df2['End_Time'].dt.dayofweek


# In[20]:


df2['DayofYear']= df2['End_Time'].dt.dayofyear


# In[21]:


df2['MonthName']= df2['End_Time'].dt.strftime("%B")


# In[22]:


df2['MonthNameAbb']= df2['End_Time'].dt.strftime("%b")


# In[23]:


df2


# In[24]:


df2['DayName']= df2['End_Time'].dt.strftime("%A")
df2['DayNameAbb']= df2['End_Time'].dt.strftime("%a")


# In[25]:


x=df2.groupby(['Year', 'Month'])['Month'].count().reset_index(name='Count')
x=pd.DataFrame(x)
x


# In[26]:


x['Count'].max()


# In[27]:


x['CountHunderds']=round(x['Count']/100,0)


# In[28]:


x.Year.value_counts()


# In[29]:


x.dtypes


# In[30]:


x['CountHunderds']=x['CountHunderds'].astype('int')


# In[31]:


x[(x['Month']==12)&(x['Year']==2021)]


# In[32]:


plt.figure(figsize=(18,10))

plt.scatter(x['Month'], x['Year'], marker='8',cmap='viridis', c=x['CountHunderds'], s=x['CountHunderds'],edgecolors='green')
plt.title('Accidents by Year and Month', fontsize=20)
plt.xlabel("Month", fontsize=18)
plt.ylabel("Year",fontsize=18)
cbar=plt.colorbar()
cbar.set_label('Number of Accidents',rotation=270, fontsize=18, color='black',labelpad=30)
ticks=[*range(100,int(x["CountHunderds"].max()),100)]
cb_tick=[*range(10000,int(x['Count'].max()),10000)]
cb_tick=['{:,}'.format(each) for each in cb_tick]
cbar.set_ticks(ticks)
cbar.set_ticklabels(cb_tick)
my_x_tick=[*range(x['Month'].min(),x['Month'].max()+1, 1)]
plt.xticks(my_x_tick, fontsize=14, color='black' )

my_y_tick=[*range(x['Year'].min(),x['Year'].max()+1, 1)]
plt.yticks(my_y_tick, fontsize=14, color='black' )
plt.show()


# In[33]:


df3=pd.read_csv(path, usecols=['State', 'Severity','End_Time'])


# In[34]:


df3


# In[35]:


df3.dtypes


# In[36]:


df3.isna().sum()


# In[37]:


df3['End_Time']=pd.to_datetime(df3['End_Time'], format='%Y-%m-%d %H:%M:%S')


# In[38]:


df3


# In[39]:


df3.dtypes


# In[40]:


df3['Hour']=df3.End_Time.dt.hour
df3['Day']=df3.End_Time.dt.day
df3['Month']=df3.End_Time.dt.month
df3['Year']=df3.End_Time.dt.year
df3['WeekDay']=df3.End_Time.dt.strftime('%a')
df3['MonthName']=df3.End_Time.dt.strftime('%b')


# In[41]:


df3


# In[42]:


y=df3.groupby(['State']).agg({'State':['count'],'Severity':['sum','mean']}).reset_index()
y


# In[43]:


y.columns=['State','Count','TotalSeverity', 'AverSeverity']


# In[44]:


y


# In[45]:


y=y.sort_values('Count', ascending=False)


# In[46]:


y


# In[47]:


y.reset_index(inplace=True, drop=True)
y


# In[48]:


plt.figure(figsize=(15,12))
plt.bar(y.loc[0:48,'State'],y.loc[0:48,'Count'], label='Accident Count')
plt.legend(loc='upper right', fontsize=14)
plt.tick_params(axis='y',labelsize=12)
plt.tick_params(axis='x',labelsize=12)
plt.title('States with Accident Counts',size=20,fontweight='bold')
plt.xticks(rotation=90)
plt.xlabel('States',fontsize=18)
plt.ylabel('Accidents',fontsize=18)
current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])

plt.show()


# In[49]:


def pick_color_to_mean(x):
    colors=[]
    avg=x.Count.mean()
    for each in x.Count:
        if each>avg*1.01:
            colors.append('pink')
        elif each<avg*.99:
            colors.append('green')
        else:
            colors.append('gray')
    return colors


# In[50]:


# remove CA because it is a extreme outlier
#severity is from 1 to 4
bottom1=1
top1=20
d1=y.loc[bottom1:top1]
mycol=pick_color_to_mean(d1)

Above=mpatches.Patch(color='pink', label='Above Average')
At=mpatches.Patch(color='gray', label='Within 1% of the Average')
Below=mpatches.Patch(color='green', label='Below Average')
fig=plt.figure(figsize=(15,20))
ax1=fig.add_subplot(2,1,1)
ax1.bar(d1.State,d1.Count, label='Count',color=mycol)
ax1.legend(handles=[Above,At,Below],fontsize=10)
plt.axhline(d1.Count.mean(),color='black', linestyle='dashed')
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.set_title('Top '+str(top1)+' States with Accident',size=20,fontweight='bold')
ax1.text(top1-3,d1.Count.mean()+3,"Mean = "+ str(d1.Count.mean()),rotation=0,fontsize=15)
ax1.tick_params(axis='y',labelsize=14)
ax1.tick_params(axis='x',labelsize=14)
ax1.set_xlabel('States',fontsize=18)
ax1.set_ylabel('Count of Accidents',fontsize=18,labelpad=20)

current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])

plt.show()



# In[51]:


def autolabel(these_bars, this_ax, place_of_decimals,symbol):
    for each_bar in these_bars:
        height=each_bar.get_height()
        this_ax.text(each_bar.get_x()+each_bar.get_width()/2,height*1.01,symbol+format(height,place_of_decimals),
                    fontsize=8,color='black',ha="center",va='bottom')


# In[52]:


def autolabel2(these_bars, this_ax, place_of_decimals,symbol):
    for each_bar in these_bars:
        height=each_bar.get_height()
        this_ax.text(each_bar.get_x()+each_bar.get_width()/2,height*1.08,symbol+format(height,place_of_decimals),
                    fontsize=8,color='black',ha="center",va='bottom')


# In[53]:


fig=plt.figure(figsize=(10,10))
ax2=fig.add_subplot(1,1,1)
ax3=ax2.twinx()
bar_width=.4
stacked=True
x_pos=np.arange(20)
count_bars=ax2.bar(x_pos-(.5*bar_width),d1.Count, bar_width,color='gray', edgecolor='black',label='Accident Count')
aver_sevr_bars=ax3.bar(x_pos+(.5*bar_width),d1.AverSeverity, bar_width, color='pink',edgecolor='black',label='AverageServerity')


ax2.set_xlabel('States', fontsize=18)
ax2.set_ylabel('Count of Accidents',fontsize=18,labelpad=20)

ax3.set_ylabel('Average Severity', fontsize=18, rotation=270, labelpad=20)
ax2.tick_params(axis='y',labelsize=14)
ax3.tick_params(axis='y',labelsize=14)
plt.title('Accident Count and Average Severity \n Top 20 Most States with Accidents',fontsize=20,fontweight='bold')
ax2.set_xticks(x_pos)
ax2.set_xticklabels(d1.State,fontsize=14)
ax2.tick_params(axis='y',labelsize=14)

cnt_color,cnt_label= ax2.get_legend_handles_labels()
sev_color,sev_label= ax3.get_legend_handles_labels()
legend=ax2.legend(cnt_color+sev_color,cnt_label+sev_label, loc='upper left', frameon=True,ncol=1,shadow=True,
                 borderpad=1,fontsize=14)

ax2.set_yticklabels
ax2.set_ylim(20000,d1.Count.max()*1.5)
ax3.set_ylim(1,d1.AverSeverity.max()*3)
ax2.set_yticklabels(['{:,.0f}'.format(x) for x in ax2.get_yticks()])

#autolabel2(count_bars,ax2,',.0f','')
#autolabel(aver_sevr_bars,ax3,'.2f','')

plt.show()


# In[55]:


df2


# In[62]:


hr=df2.groupby(['Hour', 'DayName'])['DayName'].count().reset_index(name='Totalacc')


# In[63]:


hr


# In[64]:


hr[hr.DayName=="Friday"]


# In[66]:


fig=plt.figure(figsize=(18,10))
ax=fig.add_subplot(1,1,1)
MyColor={''}
for key,grp in hr.groupby(['DayName']):
    grp.plot(ax=ax, kind='line',x='Hour', y='Totalacc', color='blue',label=key,marker='8')
    
plt.show


# In[ ]:




