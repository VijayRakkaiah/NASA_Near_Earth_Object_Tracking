import streamlit as st
import pymysql
import pandas as pd
from datetime import date

my_connection = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='nasa_neo_tracking'
)

st.markdown(
    """
    <style>
    .custom-title {
        font-family: 'Comic Sans MS', cursive, sans-serif;
        font-size: 40px;
        color: #1E90FF;
        text-align: center;
    }
    </style>
    <div class="custom-title">NASA Near-Earth Object Tracker</div>
    """,
    unsafe_allow_html=True
)

st.markdown('---')
#st.sidebar.success("success")

min_date = date(2024, 1, 1)
max_date = date(2025, 4, 13)

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    min_mag = st.slider("Minimum Magnitude", 13.80, 32.61, 30.0)
    relative_velocity = st.slider("Relative velocity (km/h)", 1418.21, 173071.83, 100000.00)
    hazard = st.selectbox("Show only potentially hazardous", [0, 1])

with col2:
    min_est_dia = st.slider("Min Estimated Diameter (km)", 0.0, 4.62, 4.0)
    astronomical = st.slider("Astronomical Unit", 0.0, 0.50, 0.25)
    start_date = st.date_input("Start Date", value=min_date, min_value=min_date, max_value=max_date, key="start_date_input")

with col3:
    max_est_dia = st.slider("Max Estimated Diameter (km)", 0.00, 10.33, 5.0)
    lunar_distance = st.slider("Lunar Distance", 0.02009, 194.481, 97.0)
    end_date = st.date_input("End Date", value=max_date, min_value=min_date, max_value=max_date, key="end_date_input")

st.markdown("""
    <style>
        div.stButton > button {
            width: 100%;
            height: 45px;
            font-size: 18px;
            font-weight: bold;
            background-color: #44aac7;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

with st.container():
    filter_clicked = st.button("🔍 Filter")

if filter_clicked:
    query = """
    SELECT a.id, a.name, a.absolute_magnitude_h, a.estimated_diameter_min_km, a.estimated_diameter_max_km,
           a.is_potentially_hazardous_asteroid, ca.close_approach_date, ca.relative_velocity_kmph,
           ca.miss_distance_lunar, ca.astronomical
    FROM asteroids a
    JOIN close_approach ca 
        ON ca.neo_reference_id = a.id
    WHERE 
        a.absolute_magnitude_h <= %(min_magnitude)s
        AND a.estimated_diameter_min_km <= %(min_estimated_dia)s
        AND a.estimated_diameter_max_km <= %(max_estimated_dia)s
        AND ca.relative_velocity_kmph <= %(relative_velocity)s
        AND ca.astronomical <= %(astronomical_unit)s
        AND ca.miss_distance_lunar <= %(lunar_distance)s
        AND ca.close_approach_date BETWEEN %(start_date)s AND %(end_date)s
    """

    if hazard == 1:
        query += " AND a.is_potentially_hazardous_asteroid = 1"
    elif hazard == 0:
        query += " AND a.is_potentially_hazardous_asteroid = 0"

    params = {
        "min_magnitude": min_mag,
        "min_estimated_dia": min_est_dia,
        "max_estimated_dia": max_est_dia,
        "relative_velocity": relative_velocity,
        "astronomical_unit": astronomical,
        "lunar_distance": lunar_distance,
        "start_date": start_date,
        "end_date": end_date
    }

    df = pd.read_sql(query, my_connection, params=params)

    if df.empty:
        st.warning("No asteroids match the selected criteria.")
    else:
        st.dataframe(df)