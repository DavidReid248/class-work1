import streamlit as st
import pandas as pd
from datetime import datetime

# page config
st.set_up_config(
  page_title='David Reid | portfolio', 
  page_icon='👌',
  layout = 'wide'
)

# Custom CSS (optional - for styling )
st.markdown('''
               <style>
                .main-header {font-size: 42px; font-weight: bold; text-align:center;}
                .sub-header {font-size: 24px; text-align:center; color #700
              </style>
          ''', unsafe_allow_html = True)
