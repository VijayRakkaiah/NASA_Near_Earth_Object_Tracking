import streamlit as st
import pandas as pd
import pymysql

my_connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'nasa_neo_tracking'
)

query_1 = """
SELECT neo_reference_id, COUNT(*) AS approach_count
FROM close_approach
WHERE orbiting_body = 'Earth'
GROUP BY neo_reference_id
ORDER BY approach_count DESC
"""
df_1 = pd.read_sql_query(query_1, my_connection)

st.title("hello.world!")
st.dataframe(df_1)