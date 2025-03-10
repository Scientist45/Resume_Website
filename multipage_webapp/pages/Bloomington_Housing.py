# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 21:40:26 2025

@author: craig
"""

import streamlit as st
import geopandas as gpd
import plotly.express as px
from geopy.geocoders import Nominatim
import pandas as pd
import plotly.graph_objects as go

# Page Title
st.title("City of Bloomington Affordable Housing Project")

st.subheader("Introduction:")

st.write(
    """
This project explores housing affordability in Bloomington, Indiana, by analyzing the 
United States Department of Housing and Urban Development (HUD). 
The dataset provides insights into median household income, 
rent-to-income ratios, and housing costs across various census tracts in Monroe County. Using 
geographic data, the project visualizes these factors on interactive maps, helping to highlight 
areas where residents may face housing challenges, especially in proximity to Indiana University 
Bloomington. The goal is to assess the affordability of housing and identify potential areas of 
financial strain.
   """
)

st.subheader("Data:")

data = gpd.read_file("multipage_webapp/reduced_location_affordability.gpkg")

st.code(
    """
#reproject GeoDataFrame data to the WGS 84 coordinate system (EPSG 4326)
data = data.to_crs(epsg=4326)
    """,
    language="python",
)

#reproject GeoDataFrame data to the WGS 84 coordinate system (EPSG 4326)
data = data.to_crs(epsg=4326)

st.code(
    """
# List of Bloomington census tracts
bloomington_tracts = ["000100", "000201","000202", "000301", "000302", "000401", "000402", 
                      "000501", "000502", "000601", "000602", "000700", "000800", "000901", 
                      "000903", "000904", "001001", "001002", "001101", "001102", "001301", "001600"]

# Create a new column indicating whether each row corresponds to a census tract in Bloomington
data['in_bloomington'] = data['TRACT'].isin(bloomington_tracts)
    """,
    language="python",
)

# List of Bloomington census tracts
bloomington_tracts = ["000100", "000201","000202", "000301", "000302", "000401", "000402", 
                      "000501", "000502", "000601", "000602", "000700", "000800", "000901", 
                      "000903", "000904", "001001", "001002", "001101", "001102", "001301", "001600"]

# Create a new column indicating whether each row corresponds to a census tract in Bloomington
data['in_bloomington'] = data['TRACT'].isin(bloomington_tracts)

st.code(
    """
# Percentage of income spent on housing
data['perc_rent_to_income'] = (data['median_gross_rent'] / ((data['median_hh_income'])/12)) * 100
data
    """,
    language="python",
)

# Percentage of income spent on housing
data['perc_rent_to_income'] = (data['median_gross_rent'] / ((data['median_hh_income'])/12)) * 100
data

st.code(
    """
#Add county names (only adding Counties names that are relevant)

#Create a df of county names
county_name_df = {'county_name': ['Monroe', 'Owen', 'Lawrence', 'Brown', 'Morgan', 'Greene', 'Spencer'],
        'COUNTY': ['105', '119', '093', '013', '109', '055', '147']}
 
#Create DataFrame
county_name_df = pd.DataFrame(county_name_df)
county_name_df
    """,
    language="python",
)

#Add county names (only adding Counties names that are relevant)

#Create a df of county names
county_name_df = {'county_name': ['Monroe', 'Owen', 'Lawrence', 'Brown', 'Morgan', 'Greene', 'Spencer'],
        'COUNTY': ['105', '119', '093', '013', '109', '055', '147']}
 
#Create DataFrame
county_name_df = pd.DataFrame(county_name_df)
county_name_df

st.code(
    """
#merge county names
data = pd.merge(data, county_name_df, on='COUNTY', how='inner')
data
    """,
    language="python",
)

#merge county names
data = pd.merge(data, county_name_df, on='COUNTY', how='inner')
data

st.code(
    """
# List of multiple county codes
county_codes = ['105', '055', '119', '093', '013', '109']
# Filter data for the specified county codes
county_data = data.loc[data['COUNTY'].isin(county_codes)]
county_data.shape
    """,
    language="python",
)

# List of multiple county codes
county_codes = ['105', '055', '119', '093', '013', '109']
# Filter data for the specified county codes
county_data = data.loc[data['COUNTY'].isin(county_codes)]
county_data.shape

st.code(
    """
#Keep important columns
county_data2 = county_data[["COUNTY", "TRACT", "area_median_hh_income", 
                            "median_gross_rent", "median_hh_income", "geometry",
                            "in_bloomington", "perc_rent_to_income", "county_name"]]
county_data2.shape
    """,
    language="python",
)

#Keep important columns
county_data2 = county_data[["COUNTY", "TRACT", "area_median_hh_income", 
                            "median_gross_rent", "median_hh_income", "geometry",
                            "in_bloomington", "perc_rent_to_income", "county_name"]]
county_data2.shape

st.subheader("Only Monroe County")

st.code(
    """
# Filter data for the specified county codes (Monroe)
monroe_codes = ['105']
monroe_data = county_data2.loc[county_data2['COUNTY'].isin(monroe_codes)]
    """,
    language="python",
)

# Filter data for the specified county codes (Monroe)
monroe_codes = ['105']
monroe_data = county_data2.loc[county_data2['COUNTY'].isin(monroe_codes)]

st.code(
    """
#get census tracts that are within Bloomington for map scatterplot
bloomington_tracts_data = monroe_data[monroe_data['in_bloomington'] == True]
    """,
    language="python",
)

#get census tracts that are within Bloomington for map scatterplot
bloomington_tracts_data = monroe_data[monroe_data['in_bloomington'] == True]

st.code(
    """
#find the location of Bloomington to center the plots
address = 'Bloomington, IN'

geolocator = Nominatim(user_agent="CN_explorer")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate of Bloomington are {}, {}.'.format(latitude, longitude))
    """,
    language="python",
)

#find the location of Bloomington to center the plots
address = 'Bloomington, IN'

geolocator = Nominatim(user_agent="CN_explorer")
location = geolocator.geocode(address)
latitude = location.latitude
longitude = location.longitude
print('The geograpical coordinate of Bloomington are {}, {}.'.format(latitude, longitude))

st.subheader("Map of Median Household Income in Monroe County")

st.write(
    """
* The census tract without data is Indiana University Bloomington. 
* The black points represent census tracts that are partially or completely within Bloomington
* Low median household income in census tracts near Bloomington. 
    """
)

st.write(
    """
Census tracts with lowest median household incomes, shown in purple, are located adjacent to Indiana University Bloomington. This could suggest that these areas have a higher proportion of student populations, who often have lower incomes. The presence of a university can influence the median household income statistics, as many students may work part-time or not at all and thus contribute to a lower median household income in census tracts where they reside. As you move away from Indiana University Bloomington, there seems to be more variation in income levels with a mix of lower income and affluent areas.
    """
)

st.code(
    """
#Median Household Income
fig = px.choropleth_mapbox(
    monroe_data,
    geojson=monroe_data.geometry.__geo_interface__,
    locations=monroe_data.index,
    color='median_hh_income',
    color_continuous_scale=px.colors.sequential.Viridis, #px.colors.sequential.Blues,
    opacity=0.7,
    mapbox_style="open-street-map",
    center={"lat": latitude, "lon": longitude},
    zoom=6,
    labels={'median_hh_income': 'Median Household Income'},
    hover_data=["TRACT", "median_hh_income"]
)

# Add scatter plot for Bloomington census tracts
fig.add_trace(
    go.Scattermapbox(
        lat=bloomington_tracts_data.geometry.centroid.y,  # Using the centroid of each census tract
        lon=bloomington_tracts_data.geometry.centroid.x,
        mode='markers',
        marker=dict(
            size=4,
            color='black',
            opacity=0.8,
        ),
        name='Bloomington Census Tracts'
    )
)

fig.show()
    """,
    language="python",
)

#Median Household Income
fig = px.choropleth_mapbox(
    monroe_data,
    #geojson=monroe_data.geometry.__geo_interface__,
    geojson=monroe_data.__geo_interface__,
    locations=monroe_data.index,
    color='median_hh_income',
    color_continuous_scale=px.colors.sequential.Viridis, #px.colors.sequential.Blues,
    opacity=0.7,
    mapbox_style="open-street-map",
    center={"lat": latitude, "lon": longitude},
    zoom=9,
    labels={'median_hh_income': 'Median Household Income'},
    hover_data=["TRACT", "median_hh_income"]
)

# Add scatter plot for Bloomington census tracts
fig.add_trace(
    go.Scattermapbox(
        lat=bloomington_tracts_data.geometry.centroid.y,  # Using the centroid of each census tract
        lon=bloomington_tracts_data.geometry.centroid.x,
        mode='markers',
        marker=dict(
            size=4,
            color='black',
            opacity=0.8,
        ),
        name='Bloomington Census Tracts'
    )
)

st.plotly_chart(fig)

st.subheader("Map of Median Gross Rent in Monroe County")

st.write(
    """
* Rent ranges from 600 to 1200 monthly cost around Bloomington.
* The black points represent census tracts that are partially or completely within Bloomington 
    """
)

st.write(
    """
This figure is a choropleth map that represents the median gross rent within various census tracts of Monroe County. Within Bloomington there is a range of rent from $600 to $1200 which could be impacted by many factors including rent controlled areas, proximity to Indiana University, and housing quality. 
    """
)

st.code(
    """
#median_gross_rent
fig = px.choropleth_mapbox(
    monroe_data,
    geojson=monroe_data.geometry.__geo_interface__,
    locations=monroe_data.index,
    color='median_gross_rent',
    color_continuous_scale=px.colors.sequential.Viridis, #px.colors.sequential.Blues,
    opacity=0.7,
    #mapbox_style='carto-positron',
    mapbox_style="open-street-map",
    center={"lat": latitude, "lon": longitude},
    zoom=6,
    labels={'median_gross_rent': 'Median Gross Rent'}
)

# Add scatter plot for Bloomington census tracts
fig.add_trace(
    go.Scattermapbox(
        lat=bloomington_tracts_data.geometry.centroid.y,  # Using the centroid of each census tract
        lon=bloomington_tracts_data.geometry.centroid.x,
        mode='markers',
        marker=dict(
            size=4,
            color='black',
            opacity=0.8,
        ),
        name='Bloomington Census Tracts'
    )
)

fig.show()
    """,
    language="python",
)

#median_gross_rent
fig = px.choropleth_mapbox(
    monroe_data,
    #geojson=monroe_data.geometry.__geo_interface__,
    geojson=monroe_data.__geo_interface__,
    locations=monroe_data.index,
    color='median_gross_rent',
    color_continuous_scale=px.colors.sequential.Viridis, #px.colors.sequential.Blues,
    opacity=0.7,
    #mapbox_style='carto-positron',
    mapbox_style="open-street-map",
    center={"lat": latitude, "lon": longitude},
    zoom=9,
    labels={'median_gross_rent': 'Median Gross Rent'}
)

# Add scatter plot for Bloomington census tracts
fig.add_trace(
    go.Scattermapbox(
        lat=bloomington_tracts_data.geometry.centroid.y,  # Using the centroid of each census tract
        lon=bloomington_tracts_data.geometry.centroid.x,
        mode='markers',
        marker=dict(
            size=4,
            color='black',
            opacity=0.8,
        ),
        name='Bloomington Census Tracts'
    )
)

st.plotly_chart(fig)

st.subheader("Map of Percent Rent to Income in Monroe County")

st.write(
    """
* Percent rent to income = median gross rent / (median household income/12) x 100
* The highest rent to income census tracts are due to a low household income around Indiana University Bloomington.
* The guideline is to spend less than 30% of your gross income on rent.
* The black points represent census tracts that are partially or completely within Bloomington 
    """
)

st.write(
    """
The rent-to-income ratio is calculated by taking the median gross rent for a census tract, dividing it by the median household income (divided by 12 to get a monthly income), and multiplying by 100 to get a percentage. This metric is a standard way of assessing housing affordability within a region. Areas in green and yellow represent tracts with higher rent-to-income ratios, suggesting that a larger portion of household income is spent on rent. These areas are exceeding the recommended guideline that no more than 30% of gross income should be spent on rent. This suggests that residents in these tracts may be experiencing financial stress due to the high cost of housing relative to their income, particularly around Indiana University Bloomington where student populations may have lower incomes.   
    """
)

st.code(
    """
#Rent to Income Ratio
fig = px.choropleth_mapbox(
    monroe_data,
    geojson=monroe_data.geometry.__geo_interface__,
    locations=monroe_data.index,
    color='perc_rent_to_income',
    color_continuous_scale=px.colors.sequential.Viridis, #px.colors.sequential.Blues,
    opacity=0.7,
    #mapbox_style='carto-positron',
    mapbox_style="open-street-map",
    center={"lat": latitude, "lon": longitude},
    zoom=6, 
    hover_data=["perc_rent_to_income"],
    labels={'perc_rent_to_income': 'Rent to Income (%)'}
)

# Add scatter plot for Bloomington census tracts
fig.add_trace(
    go.Scattermapbox(
        lat=bloomington_tracts_data.geometry.centroid.y,  # Using the centroid of each census tract
        lon=bloomington_tracts_data.geometry.centroid.x,
        mode='markers',
        marker=dict(
            size=4,
            color='black',
            opacity=0.8,
        ),
        name='Bloomington Census Tracts'
    )
)

fig.show()
    """,
    language="python",
)

#Rent to Income Ratio
fig = px.choropleth_mapbox(
    monroe_data,
    #geojson=monroe_data.geometry.__geo_interface__,
    geojson=monroe_data.__geo_interface__,
    locations=monroe_data.index,
    color='perc_rent_to_income',
    color_continuous_scale=px.colors.sequential.Viridis, #px.colors.sequential.Blues,
    opacity=0.7,
    #mapbox_style='carto-positron',
    mapbox_style="open-street-map",
    center={"lat": latitude, "lon": longitude},
    zoom=9, 
    hover_data=["perc_rent_to_income"],
    labels={'perc_rent_to_income': 'Rent to Income (%)'}
)

# Add scatter plot for Bloomington census tracts
fig.add_trace(
    go.Scattermapbox(
        lat=bloomington_tracts_data.geometry.centroid.y,  # Using the centroid of each census tract
        lon=bloomington_tracts_data.geometry.centroid.x,
        mode='markers',
        marker=dict(
            size=4,
            color='black',
            opacity=0.8,
        ),
        name='Bloomington Census Tracts'
    )
)

st.plotly_chart(fig)


