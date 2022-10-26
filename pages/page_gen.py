import pandas as pd
import pandas_profiling
import streamlit as st

from streamlit_pandas_profiling import st_profile_report


st.title('general report')


#create file uploader



upload_file=st.file_uploader('Upload a csv here')

class StreamlitApp:
    def construct_app(self):
        df=pd.read_csv(upload_file)
        pr = df.profile_report()
        st_profile_report(pr)
   
if upload_file is not None:
    sa = StreamlitApp()
    sa.construct_app()
