import streamlit as st
import pandas as pd
import pymysql
from query import *

# MySQL database connection establish
my_connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'nasa_neo_tracking'
)

# creating pandas dataframe using MySQL query
def data_frame(que):
    df = pd.read_sql_query(que, my_connection)
    return df

st.title("hello.world!")

query_options = ["1. Count how many times each asteroid has approached Earth",
                 "2. Average velocity of each asteroid over multiple approaches",
                 "3. List top 10 fastest asteroids",
                 "4. Find potentially hazardous asteroids that have approached Earth more than 3 times",
                 "5. Find the month with the most asteroid approaches",
                 "6. Get the asteroid with the fastest ever approach speed",
                 "7. Sort asteroids by maximum estimated diameter (descending)",
                 "8. An asteroid whose closest approach is getting nearer over time",
                 "9. Display the name of each asteroid along with the date and miss distance of its closest approach to Earth",
                 "10. List names of asteroids that approached Earth with velocity > 50,000 km/h",
                 "11. Count how many approaches happened per month",
                 "12. Find asteroid with the highest brightness",
                 "13. Get number of hazardous vs non-hazardous asteroids",
                 "14. Find asteroids that passed closer than the Moon (lesser than 1 LD), along with their close approach date and distance.",
                 "15. Find asteroids that came within 0.05 AU(astronomical distance)",
                 "16. List all unique orbiting bodies",
                 "17. Count total number of asteroids",
                 "18. Find the average estimated diameter (min and max) of all asteroids",
                 "19. List asteroids with estimated max diameter over 1 km",
                 "20. Find the total number of close approaches",
                 "21. Show all asteroid names that are potentially hazardous",
                 "22. List the first 10 close approach records by date",
                 "23. Count how many different asteroids approached Earth",
                 "24. Show all asteroid names and their absolute magnitudes",
                 "25. Get the earliest and latest close approach dates"]

select_query = st.selectbox("Select the query", query_options)

if select_query == query_options[0]:
    st.dataframe(data_frame(query_1))

elif select_query == query_options[1]:
    st.dataframe(data_frame(query_2))

elif select_query == query_options[2]:
    st.dataframe(data_frame(query_3))

elif select_query == query_options[3]:
    st.dataframe(data_frame(query_4))

elif select_query == query_options[4]:
    st.dataframe(data_frame(query_5))

elif select_query == query_options[5]:
    st.dataframe(data_frame(query_6))

elif select_query == query_options[6]:
    st.dataframe(data_frame(query_7))

elif select_query == query_options[7]:
    st.dataframe(data_frame(query_8))

elif select_query == query_options[8]:
    st.dataframe(data_frame(query_9))

elif select_query == query_options[9]:
    st.dataframe(data_frame(query_10))

elif select_query == query_options[10]:
    st.dataframe(data_frame(query_11))

elif select_query == query_options[11]:
    st.dataframe(data_frame(query_12))

elif select_query == query_options[12]:
    st.dataframe(data_frame(query_13))

elif select_query == query_options[13]:
    st.dataframe(data_frame(query_14))

elif select_query == query_options[14]:
    st.dataframe(data_frame(query_15))

elif select_query == query_options[15]:
    st.dataframe(data_frame(query_16))

elif select_query == query_options[16]:
    st.dataframe(data_frame(query_17))

elif select_query == query_options[17]:
    st.dataframe(data_frame(query_18))

elif select_query == query_options[18]:
    st.dataframe(data_frame(query_19))

elif select_query == query_options[19]:
    st.dataframe(data_frame(query_20))

elif select_query == query_options[20]:
    st.dataframe(data_frame(query_21))

elif select_query == query_options[21]:
    st.dataframe(data_frame(query_22))

elif select_query == query_options[22]:
    st.dataframe(data_frame(query_23))

elif select_query == query_options[23]:
    st.dataframe(data_frame(query_24))

elif select_query == query_options[24]:
    st.dataframe(data_frame(query_25))




