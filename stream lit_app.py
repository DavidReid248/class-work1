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
                .main-header 
