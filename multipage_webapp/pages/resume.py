# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 15:02:45 2025

@author: craig
"""

import streamlit as st

st.title("Kelly Craig")
#st.write("Data Scientist, assisting enterprises by supporting data-driven decision-making.")
st.markdown("---") 

# --- PROFESSIONAL SUMMARY ---
st.write("\n")
st.subheader("PROFESSIONAL SUMMARY", anchor=False)
st.write(
    """
Data scientist with 3+ years of industry experience with a proficiency in Python and R, adept at 
developing predictive models, and skilled in data visualization techniques. Formally trained with a 
Master’s degree in data science with projects involving cheminformatics model development, large 
language model application development, and data visualizations to support government initiatives 
around sustainable development. Eager to apply my expertise in solving complex problems and driving 
innovation in a collaborative team environment.

    """
)
st.markdown("---") 

# --- WORK EXPERIENCE  ---
st.subheader("WORK EXPERIENCE", anchor=False)
# EPA Entry
col1, col2 = st.columns([3, 2])  
with col1:
    st.write("**U.S. Environmental Protection Agency**  \nData Scientist") #needs a double space before \n
with col2:
    st.write("**Durham, NC**  \n_August 2022–Present_")

st.write("""
- Designed and deployed machine-learning models with R to predict toxicity of new chemicals for the Toxic Substance Control Act.  
- Collected and processed large datasets using a variety of tools including APIs, web interfaces, and SQL queries.  
- Publishing a paper showcasing novel machine-learning findings and rigorous experimentation.
""")

st.write("\n")  # Adds space between entries

# AgBiome Entry
col1, col2 = st.columns([3, 2])  
with col1:
    st.write("**AgBiome**  \nResearch Scientist") #needs a double space before \n
with col2:
    st.write("**Durham, NC**  \n_May 2015 – May 2022_")
st.write("""
- Automated data manipulation and visualization with Python and R.  
- Conducted assay development, robotic automation, and data analysis for an in vitro soluble phosphate quantification assay.  
- Developed a patented screening platform to discover direct fed microbials for swine health.  
- Screened and expanded AgBiome’s microbial collection of over 50,000 microbes including AAFCO Bacillus targeted isolations and anaerobic isolations using an anaerobic chamber.
""")

st.write("\n")

# DuPont Entry
col1, col2 = st.columns([3, 2])  
with col1:
    st.write("**DuPont**  \nStatistics Intern") #needs a double space before \n
with col2:
    st.write("**Durham, NC**  \n_May-August: 2011, 2012, 2013_")
st.write("""
- Researched and designed a method to create smaller and more compact semiconductor chips.  
- Analyzed data statistically using Excel to find the processing effects on microcircuit paste resistivity.
""")
st.markdown("---") 

# --- EDUCATION ---
st.subheader("EDUCATION", anchor=False)

# Indiana University
col1, col2 = st.columns([3, 2])
with col1:
    st.write("**Indiana University**  \nM.S. Data Science  \nGPA: 4.0")
with col2:
    st.write("**Bloomington, IN**  \n_July 2024_")

st.write("\n")  # Add space between entries

# North Carolina State University (M.S.)
col1, col2 = st.columns([3, 2])
with col1:
    st.write("**North Carolina State University**  \nM.S. Microbiology  \nGPA: 3.8")
with col2:
    st.write("**Raleigh, NC**  \n _May 2021_")

st.write("\n")

# North Carolina State University (B.S.)
col1, col2 = st.columns([3, 2])
with col1:
    st.write("**North Carolina State University**  \nB.S. Agricultural and Environmental Technologies")
with col2:
    st.write("**Raleigh, NC**  \n_May 2015_")
st.markdown("---")

# --- RELEVANT COURSEWORK ---
st.subheader("RELEVANT COURSEWORK", anchor=False)

# Indiana University
col1, col2 = st.columns([3, 3])
with col1:
    st.write("Applied Machine Learning (R/Python)  \nApplied Database Systems (SQL)  \nData Visualization (Tableau)")
with col2:
    st.write("Cloud Computing (AWS)  \nBusiness Analytics (Excel)  \nWeb Scraping (Beautiful Soup/Scrapy)")
st.markdown("---") 

# --- PUBLICATIONS & PATENTS ---
st.write("\n")
st.subheader("PUBLICATIONS", anchor=False)
st.write(
    """
- **Kelly Craig**, Richard Judson, Charles Lowe. (2025). Structure-based QSAR Models to Predict Toxicity 
Points of Departure. In progress.  
- **Kelly Craig**, Brant Johnson, Amy Grunden. (2021). Leveraging Pseudomonas Stress Response 
Mechanisms for Industrial Applications. Frontiers in Microbiology. doi: https://doi.org/10.3389/fmicb.2021.660134
- Matthew Biggs, James Kremer, **Kelly Craig**, Vadim Beilinson (2020). Compositions and Methods for 
Controlling Undesirable Microbes and Improving Animal Health. U.S. Provisional Application Number 
63/094,023. Washington, DC: U.S. Patent and Trademark Office.      
- Matthew Biggs, **Kelly Craig**, Esther Gachango, David Ingham, Mathias Twizeyimana. (2020). 
Genomics-accelerated discovery of diverse fungicidal bacteria. bioRxiv 2020.10.16.343004; doi: 
https://doi.org/10.1101/2020.10.16.343004
    """
)
