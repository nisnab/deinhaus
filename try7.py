import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title('DeinHaus Data Explorer')
st.text('This is a web app to allow exploration of deinhaus data')

#cretae file uploader

upload_file=st.file_uploader('Upload a csv here')
if upload_file is not None:
    df=pd.read_csv(upload_file)
    # Create a section for the dataframe statistics
    st.header('Statistics of Dataframe')
    st.write(df.describe())
    # Create a section for the dataframe header
    st.header('Header of Dataframe')
    st.write(df.head())
    # Create a section for matplotlib figure
    # Create a section for matplotlib figure
    st.header('Plot of Data')
    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['Depth'], y=df['Magnitude'])
    ax.set_xlabel('Depth')
    ax.set_ylabel('Magnitude')
    st.pyplot(fig)