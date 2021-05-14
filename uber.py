import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import time
import requests
import json

st.title('My first ap1p')
DATE_COLUMN = 'date/time'
DATA_URL = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

browser_header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id={}&date={}".format("199","15-05-2021")
response = requests.get(URL, headers=browser_header)
if (response.ok) and ('centers' in json.loads(response.text)):
    st.write(response.text)
    resp_json = json.loads(response.text)['centers']
    st.json(resp_json)

# # Create a text element and let the reader know the data is loading.
# data_load_state = st.text('Loading data...')
# # Load 10,000 rows of data into the dataframe.
# data = load_data(1000)
# # Notify the reader that the data was successfully loaded.
# data_load_state.text('Loading data...done!')
# st.subheader('Raw data')
# hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
# st.write(data[DATE_COLUMN].dt.hour == hour_to_filter)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
# st.subheader(f'Map of all pickups at {hour_to_filter}:00')
# st.map(filtered_data)
# st.latex(r'''
#         a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
#         \sum_{k=0}^{n-1} ar^k =
#         a \left(\frac{1-r^{n}}{1-r}\right)
#         ''')
