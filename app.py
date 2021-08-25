import streamlit as st

st. title('Search in Pubmed')
st. subheader('Enter a microbiology keyword')
#st. text('select keyword')
#st. text('select abstract')

user_input = st.text_input('Keyword: ', 'Salar') #  single line of text. 2nd is default
