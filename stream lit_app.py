import streamlit as st
import pandas as pd
from datetime import datetime

# page config
st.set_page_config(
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

# Sidebar
st.sidebar.title('👔 Navigation')
page = st.sidebar.radio('Go to' ,
                        ['.🛖 Home',  '🙋‍♂️ About', '💼 Projects', '🛠 Skills' ,'📝 Resume', '📩 Contact' ])

# Home Page
if page == '🛖 Home':
  st.markdown('<p class="main-header">David Reid</p>', unsafe_allow_html=True)
  st.markdown('<p class="sub-header">David Reid Student | Medgar Evers College</p>', unsafe_allow_html=True)

# Three Columns for stats
col1, col2, col3 = st.columns(3)

with col1:
   st.metric('GPA', '3.8', '📔')
with col2:
   st.metric('Projects', '5', '🖥️')
with col3:
   st.metric('Skills', '10+', '👔')

st.write('---')

# Introduction with columns
col1, col2, = st.columns([2,1])
with col1:
  st.subheader('Welcome to my digital space!🛜')
  st.write('''
                I am a Computer Information Systems student passionate about web development and emerging technologies like Ai. Currently learning
                HTML, CSS, JavaScript, and Python to build innovative solutions.
                 
                 👌 **Current Focus:** Building interactive web applications with Streamlit
            
                📔 **Currently Learning:** Internet and Emerging Technologies (CIS 211)
            
                🤹‍♂️ **Fun Fact:** I love learning about different Ai and using them
            ''')
  with col2:
    # Placeholder for image
    st.image('https://raw.githubusercontent.com/DavidReid248/class-work1/refs/heads/main/dog.jpg', use_column_width=True)

# About Page
  elif page =='🙋‍♂️ About':
   st.title('About Me')

  # Timeline of Professional Journey 
  st.subheader('My journey 🗾') 
  
    
  
