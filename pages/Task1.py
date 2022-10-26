import streamlit as st

st.markdown("# Task 1 ❄️")
st.sidebar.markdown("# Task 1 ❄️")
# Using object notation
questions=["RQ1","RQ2","RQ3","RQ4","RQ5"]
    
choice=st.sidebar.selectbox("Select questions",questions)


import pandas as pd
st.title('DeinHaus Data Explorer')
st.text('This is a web app to allow exploration of deinhaus data')

#cretae file uploader

upload_file=st.file_uploader('Upload a csv here')
if upload_file is not None:
    df=pd.read_csv(upload_file)
    
    if choice=='RQ1':
        st.title('RQ1')
        st.text('Can statements be made about data quality?')
        # Create a section for the dataframe statistics
        st.header('Statistics of Dataframe')
        st.write(df.describe())
        # Create a section for the dataframe header
        st.header('Header of Dataframe')
        st.write(df.head())
       
    elif choice=='RQ2':
        st.header('research 2')        
