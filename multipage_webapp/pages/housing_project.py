# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 15:53:50 2024

@author: craig
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import plotly.express as px

#Note: using anaconda navigator installs packages to a different location than if you had installed without using it. You need to run the terminal through anaconda navigator for this to work. 
#to run this open anaconda, from anaconda navigator menu open powershell prompt, go to folder (cd Documents\Python\Interview_Practice\multipage_webapp), streamlit run streamlit_app.py

# Page Title
st.title("Zillow Housing Market Analysis")

# Introduction Section
st.subheader("Objectives")
st.write(
    """
This research will be investigating the housing market trends in major US cities. For this project, three areas of interest will be investigated: 
housing price changes, available housing inventory, and how long houses stay on the market.
    
Project Focus Areas:
1. Major US city house prices
    * Case-Shiller US National Price Index
    * Zillow House Prices
2. Available Housing Inventory
3. Time Houses Stay on the Market
    """
)

st.subheader("Data Introduction")
st.write(
    """
The data for this project will be obtained from the real-estate marketplace company Zillow. Three tables will be the focus of this analysis (Zillow, 2023): 
1. Median Sale Price of Homes
2. Available For-Sale Inventory
3. Days to Pending 

These datasets were obtained from Zillow at the following link: https://www.zillow.com/research/data/. All datasets will include analysis on all home types 
(single-family, condominium and co-operative homes). The datasets are the raw measurements (not seasonally adjusted). The median sale price dataset contains 
the median price at which homes were sold for each location. The for-sale inventory dataset contains the count of unique houses that were listed for sale 
for each location. The days to pending dataset contains how long it takes homes in a location to change from sale to pending status on Zillow.com.
    """
)

# Major US City House Prices
st.subheader("Major US City House Prices")
st.write(
    """
Before importing and cleaning our dataset, lets look at The case-shiller US national price index. This price index is a widely used benchmark of 
the U.S. housing market and it was developed by economists named Karl Case and Robert Shiller (S&P Global, 2023). The price index is a calculation 
of the monthly changes in US single-family home prices and it is normalized to a value of 100 on January 2000. The Case-Shiller US National Price 
Index can be adjusted to account for inflation by dividing the home index by the consumer price index and multiplying by 100 (S&P/Case-Shiller U.S. 
National Home Price Index/Consumer Price Index for All Urban Consumers: All Items in U.S. City Average*100) (FRED, 2023).  
    """
)

# Case-Shiller US National Price Index
st.subheader("Case-Shiller US National Price Index")
st.write("Read in the Case-Shiller US National Price Index dataset (S&P/case-shiller, 2023).")

# Load and display the dataset
st.code(
    """
# Read in the national price index dataset
index_df = pd.read_csv('CSUSHPINSA.csv')
# Change to date type values
index_df['DATE'] = pd.to_datetime(index_df['DATE'])
index_df.head()
    """,
    language="python",
)

#read in national price index dataset
index_df =pd.read_csv('multipage_webapp/CSUSHPINSA.csv')
#change to date type values
index_df['DATE'] = pd.to_datetime(index_df['DATE'])
st.write(index_df.head())

st.write("Read in the Case-Shiller US nation price index (inflation adjusted) dataset (FRED, 2023)")

st.code(
    """
#read in national price index dataset (inflation adjusted)
inf_df = pd.read_csv('fredgraph.csv')
# Change to date type values
inf_df['DATE'] = pd.to_datetime(inf_df['DATE'])
inf_df.head()
    """,
    language="python",
)

#read in national price index dataset (inflation adjusted)
inf_df = pd.read_csv('multipage_webapp/fredgraph.csv')
#change to date type values
inf_df['DATE'] = pd.to_datetime(inf_df['DATE'])
st.write(inf_df.head())
#Source: https://www.geeksforgeeks.org/python-pandas-to_datetime/#

st.write(
"""
Home Price Index Line Plot:

Plot of Case-Shiller U.S. National Home Price Index and the Index adjusted for inflation. The y-axis is the index value which was normalized by 
setting January 2000 to 100. The x-axis is the date and both datasets range from 1988 to 2023. 

Analysis: 

Overall US home prices have steadily increased from January 2012 to June 2022. The rate of increasing home prices has noticeably accelerated 
recently from March 2020 to June 2022. After adjusting for inflation, recent home prices still have an increasing trend but at a less dramatic 
rate compared to the index without the inflation adjustment. The main point of showing this plot is that we need to keep in mind that the Zillow 
home prices have not been adjusted for inflation. It is still useful to find trends in the data, but US inflation also greatly impacts home pricing. 

The home price index ranges from 1988 to 2023 which gives us valuable insights into the current increasing trend in home prices and how this relates 
to price trends on a much larger time scale. With the zillow housing data, we will only be analyzing home prices from 2008, so it is important to give 
context to long term house pricing trends. 

There was another period of increasing home prices that occurred in the early 2000's. The Subprime Mortgage Crisis occurred from 2007 to 2010 and this 
event led to a significant drop in home prices (Duca, 2013). The recent increase in home prices has surpassed the prior maximum home price in 2006 even 
when accounting for inflation.
""")

st.code(
        """
# Compare the home price index and the home price index (inflation adjusted)
fig, ax = plt.subplots()
#plot Home Price Index
ax.plot('DATE', 'CSUSHPINSA', data=index_df, label ='Home Price Index', color = "#1f77b4")
#Plot Home Price Index (Inflation Adjusted)
ax.plot('DATE', 'CSUSHPISA_CPIAUCSL', data=inf_df, label = 'Home Price Index (Inflation Adjusted)', color ="#ff7f0e")
#Plot Subprime Mortgage Crisis
ax.axvline(x = dt.datetime(2007,1,1), label = "Start of Subprime Mortgage Crisis", linestyle='--', color = 'gray')
#axis labels
ax.set_xlabel("Years")
ax.set_ylabel("Index (Jan 2000 = 100)")
plt.title("Case-Shiller U.S. National Home Price Index")
leg = ax.legend()
plt.show()
        """,
        language="python",
)
    
# Compare the home price index and the home price index (inflation adjusted)
fig, ax = plt.subplots()
#plot Home Price Index
ax.plot('DATE', 'CSUSHPINSA', data=index_df, label ='Home Price Index', color = "#1f77b4")
#Plot Home Price Index (Inflation Adjusted)
ax.plot('DATE', 'CSUSHPISA_CPIAUCSL', data=inf_df, label = 'Home Price Index (Inflation Adjusted)', color ="#ff7f0e")
#Plot Subprime Mortgage Crisis
ax.axvline(x = dt.datetime(2007,1,1), label = "Start of Subprime Mortgage Crisis", linestyle='--', color = 'gray')
#axis labels
ax.set_xlabel("Years")
ax.set_ylabel("Index (Jan 2000 = 100)")
plt.title("Case-Shiller U.S. National Home Price Index")
leg = ax.legend()
st.pyplot(fig)
#Sources: 
#https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.axvline.html
#https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html
        
st.subheader("Zillow Housing Prices - Time Series Plots")

st.write(
    """
    Now, lets read in the housing price time series dataset from Zillow. This will be the first of three Zillow datasets used in this analysis. 
    The median sale price dataset contains the median price at which homes were sold for each location (Zillow, 2023). This dataset contains median 
    home prices for the United States and major cities from 2008 to 2023.
    """)
    
st.code(
        """
#Read in zillow home prices
df=pd.read_csv('Metro_median_sale_price_uc_sfrcondo_month.csv')
df.head()
        """,
        language="python",)

#Read in zillow home prices
df=pd.read_csv('multipage_webapp/Metro_median_sale_price_uc_sfrcondo_month.csv')
st.write(df.head())

st.code(
        """
#Find the number of rows (number of cities + US country) and columns (5 information columns + date columns)
df.shape
        """,
        language="python",)

st.write("dimensions of dataset: \n", df.shape)

st.code(
        """
#Check missing values
df.isna().sum()
        """,
        language="python",)

#Check missing values
st.write("Some cities in this dataset contain missing values: \n", df.isna().sum())

st.code(
        """
# How many States are in the dataset?
n = len(pd.unique(df['StateName']))
        """,
        language="python",)

# How many States are in the dataset?
n = len(pd.unique(df['StateName']))
st.write("Number of unqiue States: ", n)
#Source: https://www.geeksforgeeks.org/how-to-count-distinct-values-of-a-pandas-dataframe-column/

st.write(
    """
Analyze the Time Series Pricing Trends for the United States.

First we will only take the first row with the median prices of the United States. We check for missing values and find that only the StateName 
is missing a value which makes sense. There should not be a StateName value for the United States which is a Country. Then we will convert from 
wide to long format.
    """)
    
st.code(
        """
#Take only the US row
df_us = df.iloc[:1]
#Check missing values
df_us.isna().sum()
        """,
        language="python",)

#Take only the US row
df_us = df.iloc[:1]
#Check missing values
df_us.isna().sum()
st.write(df_us.isna().sum())

st.code(
        """
#Get list of date columns
year_list=list(df_us.columns)
#Convert from wide to long format
df_us_long = pd.melt(df_us, id_vars= ['RegionID', 'SizeRank', 'RegionName', 'RegionType', 'StateName'], value_vars=year_list,value_name='Price', var_name='Date', ignore_index=False)
#Change date to date format
df_us_long['Date']= pd.to_datetime(df_us_long['Date'])
#remove irrelevant columns
df_us_long.drop(['RegionID','SizeRank','RegionName','RegionType','StateName'], axis=1, inplace=True)
#View data
df_us_long.head()
        """,
        language="python",)

#Get list of date columns
year_list=list(df_us.columns)
#Convert from wide to long format
df_us_long = pd.melt(df_us, id_vars= ['RegionID', 'SizeRank', 'RegionName', 'RegionType', 'StateName'], value_vars=year_list,value_name='Price', var_name='Date', ignore_index=False)
#Change date to date format
df_us_long['Date']= pd.to_datetime(df_us_long['Date'])
#remove irrelevant columns
df_us_long.drop(['RegionID','SizeRank','RegionName','RegionType','StateName'], axis=1, inplace=True)
#View data
st.write(df_us_long.head())
#Source:https://towardsdatascience.com/reshaping-a-pandas-dataframe-long-to-wide-and-vice-versa-517c7f0995ad

st.write(
    """
This is version 1 of the time series plot with the Zillow median home prices. Next we will add the home price 
index (inflation adjusted).
    """)
    
st.code(
        """
# Plot time series of US home prices
fig = plt.figure()
ax = fig.add_subplot()
ax.plot('Date', 'Price', data=df_us_long)
ax.set_xlabel("Years")
ax.set_ylabel("Median Home Price")
ax.set_title("US Median Home Prices over Time")
plt.show()
        """,
        language="python",)

# Plot time series of US home prices
fig = plt.figure()
ax = fig.add_subplot()
ax.plot('Date', 'Price', data=df_us_long)
ax.set_xlabel("Years")
ax.set_ylabel("Median Home Price")
ax.set_title("US Median Home Prices over Time")
st.pyplot(fig)

st.subheader("US National Home Price Index (inflation adjusted) and Zillow US House Prices")
st.write(
    """
Now we will plot the Zillow median US Home price data and the Home Price Index (inflation adjusted). This will allow us to observe trends in 
the datasets and it will give context to housing trends after adjusting for inflation.
    """)

st.code(
        """
#Filter the home price index to dates later than march 2008 to match the dates available for the Zillow dataset. 
inf_df_2008 = inf_df[(inf_df['DATE'] >= '2008-02-01')]
        """,
        language="python",)

#Filter the home price index to dates later than march 2008 to match the dates available for the Zillow dataset. 
inf_df_2008 = inf_df[(inf_df['DATE'] >= '2008-02-01')]
st.write(inf_df_2008)
#Source: https://www.geeksforgeeks.org/ways-to-filter-pandas-dataframe-by-column-values/

st.write(
    """
Price Index (inflation adjusted) and Zillow US House Prices Time Series Plot:

Time series plot of the Home Price Index (inflation adjusted) and Zillow house prices. The plot has a dual y-axis with the y-axis on the left 
side as median home price and the right side as the index value which was normalized by setting January 2000 to 100. The x-axis is in years and 
both datasets range from 2008 to 2023.

Analysis:

The US home prices from both Zillow median house prices and the home price index have increased since 2012. The trends for both the index and 
zillow data are very similar. The rates for the datasets are not really comparable because one is based on raw home price data while the other 
is a calculated price index that was normalized, but we can still compare the general trends for this time period. The main point of this plot 
is that even when accounting for inflation there has been an increase in home prices over the last few years.
    """)
    
st.code(
        """
#Plot the zillow median price data and the home price index (inflation adjusted)
fig,ax = plt.subplots()
#Plot Zillow US House Price Dataset
line1 = ax.plot('Date', 'Price', data=df_us_long, color = "#1f77b4", label = "Zillow Median Home Price")
# Create dual y-axes chart
ax2=ax.twinx()
# plot the home index (inflation adjusted)
line2 = ax2.plot('DATE', 'CSUSHPISA_CPIAUCSL', data=inf_df_2008, color ="#ff7f0e", label = "Case-Shiller U.S. National Home Price Index \n (Inflation Adjusted)")
lns = line1+line2
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc=0)
ax.set_xlabel("Years")
ax.set_ylabel("Median Home Price")
ax2.set_ylabel("Index (Jan 2000 = 100)")
plt.show()
""",
        language="python",)

#Plot the zillow median price data and the home price index (inflation adjusted)
fig,ax = plt.subplots()
#Plot Zillow US House Price Dataset
line1 = ax.plot('Date', 'Price', data=df_us_long, color = "#1f77b4", label = "Zillow Median Home Price")
# Create dual y-axes chart
ax2=ax.twinx()
# plot the home index (inflation adjusted)
line2 = ax2.plot('DATE', 'CSUSHPISA_CPIAUCSL', data=inf_df_2008, color ="#ff7f0e", label = "Case-Shiller U.S. National Home Price Index \n (Inflation Adjusted)")
lns = line1+line2
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc=0)
ax.set_xlabel("Years")
ax.set_ylabel("Median Home Price")
ax2.set_ylabel("Index (Jan 2000 = 100)")
st.pyplot(fig)
#Code Source: https://stackoverflow.com/questions/5484922/secondary-axis-with-twinx-how-to-add-to-legend

st.subheader("Time series plot of the top 4 US cities with the highest median house prices")

st.write(
    """
We will sort by home prices on March 31st, 2023 then we will take the top 4 locations. After that we will convert the data into long format 
to make the dates rows instead of columns. Then we need to convert back to wide format, but this time our columns will be the 4 cities.
    """)
    
st.code(
        """
#Sort by the highest price for the most recent date March 31st 2023
df_sort = df.sort_values(by=['3/31/2023'], ascending=False)
df_sort.head()
        """,
        language="python",)

#Sort by the highest price for the most recent date March 31st 2023
df_sort = df.sort_values(by=['3/31/2023'], ascending=False)
st.write(df_sort.head())
    
st.code(
        """
#Sort by the highest price for the most recent date March 31st 2023
df_sort = df.sort_values(by=['3/31/2023'], ascending=False)
df_sort.head()
        """,
        language="python",)

#remove irrelevant columns
df_sort.drop(['RegionID','SizeRank','RegionType','StateName'], axis=1, inplace=True)
#Take top 4 rows
df_sort5 = df_sort.iloc[:4]
st.write(df_sort5.head())

st.code(
        """
# Get list of dates for converting into long format
year_list2=list(df_sort5.columns)
# Convert from wide to long format
df_sort_long = pd.melt(df_sort5, id_vars= ['RegionName'], value_vars=year_list2,value_name='Price', var_name='Date', ignore_index=False)
#Change date to date format
df_sort_long['Date'] = pd.to_datetime(df_sort_long['Date'])
df_sort_long.head()
        """,
        language="python",)

# Get list of dates for converting into long format
year_list2=list(df_sort5.columns)
# Convert from wide to long format
df_sort_long = pd.melt(df_sort5, id_vars= ['RegionName'], value_vars=year_list2,value_name='Price', var_name='Date', ignore_index=False)
#Change date to date format
df_sort_long['Date'] = pd.to_datetime(df_sort_long['Date'])
st.write(df_sort_long.head())
#Source:https://towardsdatascience.com/reshaping-a-pandas-dataframe-long-to-wide-and-vice-versa-517c7f0995ad

st.code(
        """
#convert long to wide format by RegionName
df_sort_wide=pd.pivot(df_sort_long, index=['Date'], columns = 'RegionName',values = 'Price')
df_sort_wide
        """,
        language="python",)

#convert long to wide format by RegionName
df_sort_wide=pd.pivot(df_sort_long, index=['Date'], columns = 'RegionName',values = 'Price')
st.write(df_sort_wide)
#Source: https://towardsdatascience.com/reshaping-a-pandas-dataframe-long-to-wide-and-vice-versa-517c7f0995ad

st.write(
    """
Time Series Plot of Top 4 Locations with Highest Home Prices:

Time series plot of the Top 4 Locations with Highest Home Prices: Edwards, San Francisco, San Jose, and Santa Cruz. The y-axis is the median home 
price and the x-axis is years. 

Analysis:

This time series shows the prices for the top 4 locations with the highest home prices. The four cities with the most expensive home prices in March 
2023 are  Edwards CO, San Francisco CA, San Jose CA and Santa Cruz CA. These locations have gradually increased from around half a million in 2012 
to over 900,000 in 2023. San Jose, CA in particular had a median home value of over 1.2 million in 2023. Three of the locations with the most expensive 
home prices are in California and interestingly all 3 of these cities are within about 70 miles of each other. During our initial data exploration we 
observed that some cities are missing pricing information for some dates. We can see here that San Jose, Ca is missing some pricing information for 2018.    
    """)

st.code(
        """
plt.figure(figsize=(16, 8))
# plot each location
df_sort_wide['Edwards, CO'].plot(label='Edwards, CO')
df_sort_wide['San Francisco, CA'].plot(label='San Francisco, CA')
df_sort_wide['San Jose, CA'].plot(label='San Jose, CA')
df_sort_wide['Santa Cruz, CA'].plot(label='Santa Cruz, CA', color='purple')
plt.title('Top 4 Locations with Highest Home Prices', fontsize=18)
plt.xlabel('Years', fontsize=16)
plt.ylabel('Median Home Prices (Millions)', fontsize=16)
plt.legend(fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
        """,
        language="python",)

plt.figure(figsize=(16, 8))
# plot each location
df_sort_wide['Edwards, CO'].plot(label='Edwards, CO')
df_sort_wide['San Francisco, CA'].plot(label='San Francisco, CA')
df_sort_wide['San Jose, CA'].plot(label='San Jose, CA')
df_sort_wide['Santa Cruz, CA'].plot(label='Santa Cruz, CA', color='purple')
plt.title('Top 4 Locations with Highest Home Prices', fontsize=18)
plt.xlabel('Years', fontsize=16)
plt.ylabel('Median Home Prices (Millions)', fontsize=16)
plt.legend(fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
st.pyplot(plt)
#code source: https://www.geeksforgeeks.org/pandas-plot-multiple-time-series-dataframe-into-a-single-plot/

st.subheader("House Inventory in Major US Cities - Time Series and Bar Plots")

st.write(
    """
Let's analyze the trends of available for-sale inventory in the US. The Zillow for-sale inventory dataset contains the count of unique houses 
that were listed for sale for each major US city (Zillow, 2023).

Let's read in the house inventory time series dataset from Zillow. We will only take the top row that contains data on the United States. 
After that we will convert the data from wide to long format to plot the time series. Then we will merge the inventory data with our median home 
price for the US dataset.
    """)

st.code(
        """
#Read in zillow home inventory dataset
df_invt=pd.read_csv('Metro_invt_fs_uc_sfrcondo_month.csv')
df_invt.head()
        """,
        language="python",)

#Read in zillow home inventory dataset
df_invt=pd.read_csv('multipage_webapp/Metro_invt_fs_uc_sfrcondo_month.csv')
st.write(df_invt.head())

st.code(
        """
#US inventory
df_inv_us = df_invt.iloc[:1]
#Convert from wide to long format
year_list3=list(df_inv_us.columns)
df_inv_us_long = pd.melt(df_inv_us, id_vars= ['RegionID', 'SizeRank', 'RegionName', 'RegionType', 'StateName'], value_vars=year_list3,value_name='Inventory', var_name='Date', ignore_index=False)
df_inv_us_long['Date']= pd.to_datetime(df_inv_us_long['Date'])
# remove irrelevant columns
df_inv_us_long.drop(['RegionID','SizeRank','RegionName','RegionType','StateName'], axis=1, inplace=True)
df_inv_us_long.head()
        """)
        
#US inventory
df_inv_us = df_invt.iloc[:1]
#Convert from wide to long format
year_list3=list(df_inv_us.columns)
df_inv_us_long = pd.melt(df_inv_us, id_vars= ['RegionID', 'SizeRank', 'RegionName', 'RegionType', 'StateName'], value_vars=year_list3,value_name='Inventory', var_name='Date', ignore_index=False)
df_inv_us_long['Date']= pd.to_datetime(df_inv_us_long['Date'])
# remove irrelevant columns
df_inv_us_long.drop(['RegionID','SizeRank','RegionName','RegionType','StateName'], axis=1, inplace=True)
st.write(df_inv_us_long.head())
#Source:https://towardsdatascience.com/reshaping-a-pandas-dataframe-long-to-wide-and-vice-versa-517c7f0995ad

st.code(
        """
#Merge US prices and inventory
#Inner merge to only keep dates in common
us_long_price_inv = df_us_long.merge(df_inv_us_long, how = 'inner', on='Date')
us_long_price_inv.head()
        """,
        language="python")

#Merge US prices and inventory
#Inner merge to only keep dates in common
us_long_price_inv = df_us_long.merge(df_inv_us_long, how = 'inner', on='Date')
st.write(us_long_price_inv.head())
#Source: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html

st.code(
        """
#Check missing values
us_long_price_inv.isna().sum()
#There are no missing values
        """,
        language="python")

#Check missing values
st.write(us_long_price_inv.isna().sum())
#There are no missing values
        
st.write(
    """
Time Series Plot of Median US Home Prices and US Home Inventory:

This is a time series plot of the median US home prices and the available US home inventory. The plot has a dual y-axis with the y-axis on the 
left side as median home price and the right side as available home inventory. The x-axis is the date and both datasets range from 2018 to 2023.

Analysis:

This time series plot shows the decrease in available home inventory from 2020 to 2023 and an increase in home prices from 2018 to 2023. The 
COVID Pandemic began in January 2020 and it could have potentially contributed to these trends. The local peaks and valleys could be caused by 
seasonal variation with peaks typically occurring in the summer (Nadia, 2019). Unfortunately, the Zillow US home inventory data is not available 
prior to 2018, so we cannot view long term home inventory trends. With the information presented, we can form a hypothesis that housing prices were 
stable in 2018 through 2019 then decrease from 2020 to 2023 potentially due to the COVID-19 Pandemic or other unknown factors.
    """)
    
st.code(
        """
#Plot the zillow median price data and the home price index (inflation adjusted)
#increase figure size to fit the color label
fig,ax = plt.subplots(figsize=(8,6))
#Plot Zillow US House Price Dataset
line1 = ax.plot('Date', 'Price', data=us_long_price_inv, color = "#1f77b4", label = "Median Home Price")
# Create dual y-axes chart
ax2=ax.twinx()
# plot home inventory
line2 = ax2.plot('Date', 'Inventory', data=us_long_price_inv, color ="#ff7f0e", label = "US Home Inventory")
lns = line1+line2
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc=9)
ax.set_xlabel("Years")
ax.set_ylabel("Median Home Price")
ax2.set_ylabel("US Home Inventory (Million)")
plt.show()
       """,
       language="python",) 

#Plot the zillow median price data and the home price index (inflation adjusted)
#increase figure size to fit the color label
fig,ax = plt.subplots(figsize=(8,6))
#Plot Zillow US House Price Dataset
line1 = ax.plot('Date', 'Price', data=us_long_price_inv, color = "#1f77b4", label = "Median Home Price")
# Create dual y-axes chart
ax2=ax.twinx()
# plot home inventory
line2 = ax2.plot('Date', 'Inventory', data=us_long_price_inv, color ="#ff7f0e", label = "US Home Inventory")
lns = line1+line2
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc=9)
ax.set_xlabel("Years")
ax.set_ylabel("Median Home Price")
ax2.set_ylabel("US Home Inventory (Million)")
st.pyplot(fig)

st.subheader("Top 10 cities with highest inventory for 2023:")

st.write(
    """
Next we will plot the top 10 major US cities with the highest inventory for 2023. We will use home inventory values from the pre-pandemic date of 
May 2019 and the most recent date of May 2023.
    """)
    
st.code(
        """
#Keep columns with dates of interest
df_inv3 = pd.DataFrame(df_invt[['RegionName','2019-05-31', '2021-05-31','2023-05-31']])
        """,
        language="python")

#Keep columns with dates of interest
df_inv3 = pd.DataFrame(df_invt[['RegionName','2019-05-31', '2021-05-31','2023-05-31']])
        
st.code(
        """
#keep the top 11 values with highest inventory for the date May 2023. 
df_inv_largest = df_inv3.nlargest(n=11, columns=['2023-05-31'])
#Remove the top row which is the US (we only want to include cities in this figure)
df_inv_largest = df_inv_largest.iloc[1:]
        """,
        language="python")

#keep the top 11 values with highest inventory for the date May 2023. 
df_inv_largest = df_inv3.nlargest(n=11, columns=['2023-05-31'])
#Remove the top row which is the US (we only want to include cities in this figure)
df_inv_largest = df_inv_largest.iloc[1:]
#Source: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nlargest.html

st.write(
    """
Bar graph of the top 10 Major US Cities with the highest available home inventory:

This is a bar graph of the top 10 major cities with the highest available home inventory in May 2023. The y-axis is the number of homes for sale. 
The x-axis is 10 US cities: New York City, Miami, Chicago, Dallas, Houston, Atlanta, Phoenix, Los Angeles, Philadelphia, and Cape Coral. The orange 
bars are home inventory from May 2023 and the blue bars are home inventory from May 2019.

Analysis:

This bar graph shows that home inventory as of May 2023 has not recovered to pre-pandemic levels (May 2019) for any of the displayed cities except 
Cape Coral, FL. In addition, these 10 Major US cities have the highest available home inventory for 2023. This shows that even cities with the highest 
currently available inventory have not been able to exceed 2019 inventory. Although this graph is focused on 10 cities, we have seen from the previous 
time series graph that the trends for the US in general also followed this pattern of decreasing inventory from 2019 to 2023. This demonstrates that 
these cities have not been cherry picked, but this seems to be a general trend in the United States.
    """)

st.code(
        """
#Create box plot
df_inv_largest.plot(x='RegionName', y=['2019-05-31', '2023-05-31'], kind="bar", 
                    xlabel = "US Cities", ylabel = "Home Inventory")
        """,
        language="python") 

#Create bar plot
fig, ax = plt.subplots(figsize=(10, 6))
df_inv_largest.plot(x='RegionName', y=['2019-05-31', '2023-05-31'], kind="bar", 
                    xlabel = "US Cities", ylabel = "Home Inventory", ax=ax)
st.pyplot(fig)
#source: https://www.geeksforgeeks.org/plot-multiple-columns-of-pandas-dataframe-on-bar-chart-with-matplotlib/

st.subheader("Time Houses Stay on the Market - Proportional Symbol Map")
st.write(
    """
Let's read in the days to pending dataset from Zillow. The days to pending dataset contains how long it takes homes in a location to change from sale 
to pending status on Zillow.com (Zillow, 2023).
    """)
    
st.code(
        """
df_pending=pd.read_csv('Metro_med_doz_pending_uc_sfrcondo_month.csv')
df_pending.head()
        """,
        language="python") 

df_pending=pd.read_csv('multipage_webapp/Metro_med_doz_pending_uc_sfrcondo_month.csv')
st.write(df_pending.head())

st.write(
    """
In order to make a proportional symbol map we will need the geographic location (longitude and latitude coordinates) for each city. To do this 
we will use the geopy python library. This allows us to enter a city name and find the geographic coordinates for that location. We add error 
handling so that the for loop will continue to the next city when the coordinates cannot be found for one of the cities.
    """)
    
st.code(
        """
# calling the Nominatim tool
loc = Nominatim(user_agent="GetLoc")

#get column length
len_df_pending = df_pending.shape[0]

# add empty columns for coordinates
df_pending['latitude'] = np.nan
df_pending['longitude'] = np.nan

#Get latitude and logitude for each city
for i in range(1, len_df_pending): #start at 1 to skip US Country row
    location = df_pending.at[i,'RegionName']
    try:
        getLoc = loc.geocode(location)
    except:
        print("Error: geocode failed")
        continue
    try:
        lat = getLoc.latitude
    except:
        print("Error: getLoc.latitude failed")
        continue
    try:
        long = getLoc.longitude
    except:
        print("Error: getLoc.longitude failed")
        continue
    df_pending.at[i,'latitude'] = lat
    df_pending.at[i,'longitude'] = long
        """,
        language="python") 
#Code Source: https://www.geeksforgeeks.org/how-to-get-geolocation-in-python/

    
st.code(
        """
#Create csv file so that the previous cell does not need to be re-run. 
#df_pending.to_csv("df_pending_coordinates.csv")
#load in csv file
df_pending=pd.read_csv('df_pending_coordinates.csv')
        """,
        language="python") 

#load in csv file
df_pending=pd.read_csv('multipage_webapp/df_pending_coordinates.csv')
 
st.write(
    """
To clean up the data, we will change the format of the "RegionName" column from "City, State" to "City." Then we reduce the columns down to city, 
date, and coordinates for the map visualization. We also remove the cities that do not have geographic coordinates.
    """)  

st.code(
        """
# Create City and State columns from the RegionName column
df_pending[['City', 'State']] = df_pending['RegionName'].str.split(',', 1, expand=True)
#remove RegionName column
df_pending.drop('RegionName', axis=1, inplace=True) 
#remove State column
#df_pending.drop('State', axis=1, inplace=True) 
#move city column
column_to_move = df_pending.pop('City') 
df_pending.insert(3,'City', column_to_move) 
#Remove unnecessary columns
df_pending = pd.DataFrame(df_pending[['City','2023-05-31', 'latitude', 'longitude', 'State']])
df_pending.head()
        """,
        language="python") 
    
# Create City and State columns from the RegionName column
df_pending[['City', 'State']] = df_pending['RegionName'].str.split(',', expand=True)
#remove RegionName column
df_pending.drop('RegionName', axis=1, inplace=True) 
#remove State column
#df_pending.drop('State', axis=1, inplace=True) 
#move city column
column_to_move = df_pending.pop('City') 
df_pending.insert(3,'City', column_to_move) 
#Remove unnecessary columns
df_pending = pd.DataFrame(df_pending[['City','2023-05-31', 'latitude', 'longitude', 'State']])
st.write(df_pending.head())
#Sources: 
#https://pandas.pydata.org/docs/reference/api/pandas.Series.str.split.html
#https://stackoverflow.com/questions/35321812/move-column-in-pandas-dataframe
    
st.code(
        """
# check for na values
df_pending.isna().sum()
        """,
        language="python") 

# check for na values
st.write(df_pending.isna().sum())

st.code(
        """
# Remove na values
df_pending = df_pending.dropna()
df_pending.isna().sum()
        """,
        language="python") 

# Remove na values
df_pending = df_pending.dropna()
st.write(df_pending.isna().sum())

st.write(
    """
Proportional Symbol Map:
We will create a proportional symbol map that only includes one city per state and the city we pick will have the longest time on the market. 
To accomplish this we will group the dataset by State then we will take the rows with the max May 2023 home inventory for each state. 
This will result in a final dataframe with one city per state with the longest time on the market.
    """) 
    
st.code(
        """
#Get highest inventory city per state
highest_city = df_pending.loc[df_pending.groupby('State')['2023-05-31'].idxmax()]
#rename 2023-05-31 column to days_pending
highest_city.rename(columns={'2023-05-31':'days_pending'}, inplace=True)
#sort by day_pending
highest_city = highest_city.sort_values(by='days_pending', ascending=False)
highest_city.head()
        """,
        language="python") 

#Get highest inventory city per state
highest_city = df_pending.loc[df_pending.groupby('State')['2023-05-31'].idxmax()]
#rename 2023-05-31 column to days_pending
highest_city.rename(columns={'2023-05-31':'days_pending'}, inplace=True)
#sort by day_pending
highest_city = highest_city.sort_values(by='days_pending', ascending=False)
st.write(highest_city.head())
#code source: https://stackoverflow.com/questions/76231438/pandas-dataframe-loc-groupby-idxmax-and-na-values

st.code(
        """
#shortest day pending on the market
shortest_city = highest_city.sort_values(by='days_pending', ascending=True)
shortest_city.head()
        """,
        language="python") 

#shortest day pending on the market
shortest_city = highest_city.sort_values(by='days_pending', ascending=True)
st.write(shortest_city.head())

st.write(
    """
Proportional symbol map of cities with the longest time homes are on the market per state:

This is a proportional symbol map of the top cities per state that have the longest time homes are on the market for May 2023. 
Only one city is represented per state and this city is selected by having the longest time houses are on the market compared to any other city 
in the state. The number of days houses stay on the market is represented through the color of the data point and by the diameter of the circle 
for each data point. The lighter color is less time homes spent on the market and the darker color is longer time on the market. 
In addition, the larger diameter of the data point represents longer time on the market. This is an interactive map that can be zoomed in or moved. 
It also displays key information about each location including days pending and City name by hovering over each data point.

Analysis:

This proportional symbol map shows that the top 3 locations with the longest days houses stay on the market are Hope AR (82 days), 
Clewiston FL (64 days), and Lexington NE (60 days). The cities with the shortest days on the market are Portland ME and Washington DC 
with only 6 days. The States on the West coast and North Eastern US in general have the lowest days on the market.
    """) 
    
st.code(
        """
#City with the longest time home are on the market per state
fig = px.scatter_mapbox(highest_city, lat="latitude", lon="longitude", hover_name="City", hover_data=["State","City"],
                        color="days_pending",
                        size="days_pending", color_continuous_scale=px.colors.sequential.Burg, size_max=40, 
                        zoom=3, height=600, mapbox_style="open-street-map",width=1000, #open-street-map
                       title='Housing Inventory')
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},paper_bgcolor='rgb(248, 248, 255)',
     plot_bgcolor='rgb(248, 248, 255)',)
fig.show()
        """,
        language="python") 

#City with the longest time home are on the market per state
fig = px.scatter_mapbox(highest_city, lat="latitude", lon="longitude", hover_name="City", hover_data=["State","City"],
                        color="days_pending",
                        size="days_pending", color_continuous_scale=px.colors.sequential.Burg, size_max=40, 
                        zoom=3, height=600, mapbox_style="open-street-map",width=1000, #open-street-map
                       title='Housing Inventory')
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},paper_bgcolor='rgb(248, 248, 255)',
     plot_bgcolor='rgb(248, 248, 255)',)
st.plotly_chart(fig, use_container_width=True)
#code source: https://www.kaggle.com/code/aqsasadaf/us-cities-database-with-plotly-mapbox

st.subheader("References:")

st.write(
    """

Zillow Housing Data. Zillow. (2023, April 25). https://www.zillow.com/research/data/ 

S&P Global CoreLogic Case-Shiller Home Price Indices Methodology - S&P Global. (2023, June 27). https://www.spglobal.com/spdji/en/documents/methodologies/methodology-sp-corelogic-cs-home-price-indices.pdf?force_download=true 

S&P/case-shiller U.S. national home price index. FRED. (2023, June 27). https://fred.stlouisfed.org/series/CSUSHPINSA#0 

FRED Federal Reserve Economic Data: Your trusted data source since 1991. FRED. (2023, June 27). https://fred.stlouisfed.org/graph/?g=kYEb 

Duca, J. V. Subprime mortgage crisis. Federal Reserve History. (2013, November 22). https://www.federalreservehistory.org/essays/subprime-mortgage-crisis 

Nadia Evangelou, National Association of Realtors. Seasonality in the housing market. www.nar.realtor. (2019, January 2). https://www.nar.realtor/blogs/economists-outlook/seasonality-in-the-housing-market 
    """) 
