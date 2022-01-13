import pandas as pd
import streamlit as st
import numpy as np
from PIL import Image
import pickle
import model

pc_df = pd.read_csv(f"files/post_code_list.csv")
lgb_model = pickle.load(open("files/lgbmmodel.pkl", "rb"))


codes_available = pc_df['post_code'].drop_duplicates().to_list()

col1, col2 = st.columns(2)

type = st.sidebar.selectbox("Type", ["Flat","Terraced","Semi-Detached","Detached"], index=0)
post_code = st.sidebar.selectbox("Post Code District", codes_available, index=0)
station = st.sidebar.number_input("Distance to train station", min_value=0.0, max_value=5.0,value=0.5)
beds = st.sidebar.number_input("Bedrooms", min_value=0, max_value=5,value=3)
baths = st.sidebar.number_input("Bathrooms", min_value=0, max_value=5,value=2)
receptions = st.sidebar.number_input("Receptions", min_value=0, max_value=5,value=1)

if st.sidebar.button("Check estimation", key=None, help=None, on_click=None, args=None, kwargs=None):
    price = model.get_price(lgb_model,type.lower(),float(station),int(beds),int(baths),int(receptions),post_code,pc_df)
    format_price = "{:,}".format(round(price))
    st.header(f"Estimation - £{format_price}")