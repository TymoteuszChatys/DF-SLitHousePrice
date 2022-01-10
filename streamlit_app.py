import pandas as pd
import streamlit as st
import numpy as np
import model
from PIL import Image



question = st.selectbox("Question", ["How much is my house worth?"], index=0)