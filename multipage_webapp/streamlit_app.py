# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 15:46:35 2024

@author: craig
"""

import streamlit as st

resume_page = st.Page(
    page = "pages/resume.py",
    title = "Resume",
    icon=":material/account_circle:",
    default = True,)

housing_page = st.Page(
    page = "pages/housing_project.py",
    title = "Housing Market Analysis",
    icon=":material/house:")

bloomington_page = st.Page(
    page = "pages/Bloomington_Housing.py",
    title = "Affordable Housing in Bloomington",
    icon=":material/house:")

pg = st.navigation(pages=[resume_page, housing_page, bloomington_page])
pg.run()