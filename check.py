import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.figure_factory as ff



data = pd.read_csv("out1.csv") 




st.title("VISUALIZATION")

placeholder = st.empty()
with placeholder.container():

    
    club_1, club_2, club_3,fest_1,fest_2= st.columns(5)

   
    club_1.metric(
        label="CLUB_1 COUNT",
        value=round(334),
      
    )

    club_2.metric(
        label="CLUB_2 COUNT",
        value=int(335),
       
    )
    
    club_3.metric(
        label="CLUB_3 COUNT",
        value=int(407),
        
    )

    fest_1.metric(
        label="FEST_1 organizers",
        value=int(375),
        

       
    )
    
    fest_2.metric(
        label="FEST_2 COUNT",
        value=int(400),
        
    )

df = pd.DataFrame
df = data.sum()
df.drop(['Name','ID',"Unnamed: 0"],axis=0,inplace=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("### Count of Participants")
    st.write(df)


with col2:
    st.markdown("### Detailed Data View")
    st.dataframe(data)




fig_col1, fig_col2 = st.columns(2)

grap = pd.DataFrame
grap = pd.read_csv("count.csv")
    
with fig_col1:
        st.markdown("### Analysis using Plotly dash")
        fig = px.density_heatmap(
            data_frame=grap, y="count", x="columns",
        )
        st.write(fig)



       
        

