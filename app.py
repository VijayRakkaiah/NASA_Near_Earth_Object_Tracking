import streamlit as st

st.set_page_config(
    page_title="NASA NEO Tracker",
    page_icon="assets/logo.png",
    layout="centered",                  # Options: "centered" (default), "wide"
    initial_sidebar_state="expanded"    # Options: "expanded" or "collapsed"
)

about_page = st.Page(
    page="pages/about.py",
    title='About',
    icon="ℹ",
    default=True
)

filter_page = st.Page(
    page="pages/filter.py",
    title='Filter Asteroids',
    icon="🔎"
)

query_page = st.Page(
    page="pages/faq.py",
    title="Queries",
    icon="❔"
)

pg = st.navigation(
    {
        "Info": [about_page],
        "NASA NEO Tracker Pages": [filter_page, query_page]
    }
)
st.logo("assets/nasa_guvi.png", size="large")
st.sidebar.text("Watching space rocks to keep Earth safe")

pg.run()
