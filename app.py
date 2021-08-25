import streamlit as st
import pandas as pd

header = st.container()
dataset = st.container()

with header :
    st. title('Search in Pubmed')
    #st. subheader('Enter a microbiology keyword')
    #st. text('Enter a microbiology keyword')
    #st. text('select abstract')

    
# Input box
user_input = st.text_input('Keyword: ', 'Salar') #  single line of text. 2nd is default





# hide footer
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

