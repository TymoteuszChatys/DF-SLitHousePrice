import pandas as pd
import streamlit as st
import numpy as np
from PIL import Image
import pickle
import model

pc_df = pd.read_csv(f"files/post_code_list.csv")
lgb_model = pickle.load(open("files/lgbmmodel.pkl", "rb"))


codes_available = pc_df['post_code'].drop_duplicates().to_list()
codes_available = sorted(codes_available)

col1, col2 = st.columns(2)

type = st.sidebar.selectbox("Type", ["Flat","Terraced","Semi-Detached","Detached"], index=0)
post_code = st.sidebar.selectbox("Post Code District", codes_available, index=161)
station = st.sidebar.number_input("Distance to train station (miles)", min_value=0.0, max_value=5.0,value=0.9)
beds = st.sidebar.number_input("Bedrooms", min_value=0, max_value=5,value=2)
baths = st.sidebar.number_input("Bathrooms", min_value=0, max_value=5,value=1)
receptions = st.sidebar.number_input("Receptions", min_value=0, max_value=5,value=1)

if st.sidebar.button("Check estimation", key=None, help=None, on_click=None, args=None, kwargs=None):
    price = model.get_price(lgb_model,type.lower(),float(station),int(beds),int(baths),int(receptions),post_code,pc_df)
    percentage = 0.2*price
    lower_bound = price - percentage
    upper_bound = price + percentage
    lower_bound = "{:,}".format(round(lower_bound/1000))
    upper_bound = "{:,}".format(round(upper_bound/1000))
    st.header(f"Estimated     £{lower_bound}k - £{upper_bound}k")