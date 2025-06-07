
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv(r"C:\Users\ydhon\Downloads\DsResearch\Media and Technology\Global YouTube Statistics.csv",encoding='latin1')

#1.	What are the top 10 YouTube channels based on the number of subscribers?

channels=df.sort_values(by='subscribers',ascending=False)
print('channels based on their subscribers',channels[['Youtuber','subscribers']])


#2.	Which category has the highest average number of subscribers?
channels_category=df.groupby('category')['subscribers'].mean() 
print(channels_category)
print('Autos and vehicles category has the highest average number of subscribers')


#3.	How many videos, on average, are uploaded by YouTube channels in each category?
channels_upload=df.groupby('category')['uploads'].mean() 
print('videos uploaded on each category are',channels_upload)


#4.	What are the top 5 countries with the highest number of YouTube channels?

highest_channels=df.groupby('Country')['Youtuber'].count()
print(highest_channels)

print(highest_channels.sort_values(ascending=False).head(5))

#5.	What is the distribution of channel types across different categories?

sns.barplot(x=df['category'],y=df['channel_type'])
plt.xlabel('category')
plt.ylabel('channel_type')
plt.title('channel types across different categories')
plt.show()

#6.	Is there a correlation between the number of subscribers and total video views for YouTube channels?

corelation=df['subscribers'].corr(df['video views']) 
print('corelation between no of subscribers and total views ',corelation)
print('there is positive corelation between subscribers and views')

#7.		How do the monthly earnings vary throughout different categories??
sns.scatterplot(x=df['category'],y=df['lowest_monthly_earnings'])
plt.xlabel('category')
plt.ylabel('monthly earnings')
plt.title(' monthly earnings vs categories')
plt.show()

#8.	What is the overall trend in subscribers gained in the last 30 days across all channels?

sns.histplot(df['subscribers_for_last_30_days'])
plt.xlabel('subscribers')
plt.ylabel('frequency')
plt.title('overall trend in subscribers gained in the last 30 days across all channels')
plt.show()

#9.	Are there any outliers in terms of yearly earnings from YouTube channels

from scipy.stats import zscore

df['z_score']=zscore(df['lowest_yearly_earnings'])


outliers=df[(df['z_score']>3) | (df['z_score']<-3)] 

print('the ouliers are',outliers)

#10.	What is the distribution of channel creation dates? Is there any trend over time?

#11.	Is there a relationship between gross tertiary education enrollment and the number of YouTube channels in a country
sns.scatterplot(x=highest_channels.iloc[0:],y=df['Gross tertiary education enrollment (%)'])
plt.show()

print(highest_channels.iloc[:,0])


print(type(highest_channels))



#12.	How does the unemployment rate vary among the top 10 countries with the highest number of YouTube channels?


highest_channels_new=pd.DataFrame({'country':highest_channels.index,'channel':highest_channels.values})
print(highest_channels_new.columns)
newchannels = highest_channels_new.sort_values(by=('channel'),ascending=False)


print(highest_channels_new)
#qwsu
print(newchannels)

var=newchannels.iloc[:10,0]

sns.barplot(x=var,y=df['Unemployment rate'])

#13.	What is the average urban population percentage in countries with YouTube channels?

avg_population=df.groupby('Country')['Urban_population'].mean()

print('the avg population is',avg_population)



#14.	Are there any patterns in the distribution of YouTube channels based on latitude and longitude coordinates?

sns.barplot(data=df,x='Latitude',y='Longitude',hue=newchannels.iloc[:10,1])
plt.show()

#15.	What is the correlation between the number of subscribers and the population of a country?
corelation_subscribers=df['subscribers'].corr(df['Population'])
print('the corelation is',corelation_subscribers)

#16.	How do the top 10 countries with the highest number of YouTube channels compare in terms of their total population?

sns.barplot(x=var,y=df['Population'])
plt.show()


#               