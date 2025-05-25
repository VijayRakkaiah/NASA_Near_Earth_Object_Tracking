import streamlit as st


# Title section
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
    <div class="custom-title">🪐 About This Project 🚀</div>
    """,
    unsafe_allow_html=True
)

# Project description
st.markdown("""
<div style="text-align: justify; font-size: 16px;">
This project is built to <strong>track Near-Earth Objects (NEOs)</strong> using NASA data.  
NEOs are asteroids or comets that come close to Earth’s orbit and could impact our planet.  
By analyzing their size, speed, and approach dates, we can better understand potential risks and learn more about these space objects.
</div>
""", unsafe_allow_html=True)

# Features
st.markdown("""
---

### 🌍 What You Can Do:
- 🔎 **Filter asteroids** by size, speed, and close approach date  
- 💡 **Explore fun facts** and insights using pre-built queries

---

### 🔧 Tools & Tech Stack:
- 🐍 **Python**
- 🖥️ **Streamlit** (for building interactive web apps)
- 🗄️ **MySQL** (to store/query asteroid data)
- 📊 **Pandas** (to show data in table format)
- 🔌 **PyMySQL** (to connect Python & MySQL)
- 🎨 **HTML/CSS** (for styling and layout)

---

### 👨‍💻 About Me
Hi! I'm **Vijay Rakkaiah**, a data science and software development enthusiast.  
I created this project to explore NASA’s asteroid data in an interactive, user-friendly way.

📫 **Contact Me**  
✉️ Email: [vijay.rakkaiah@gmail.com](mailto:vijay.rakkaiah@gmail.com)

🔗 **Connect With Me**  
[GitHub](https://github.com/VijayRakkaiah) | [LinkedIn](https://www.linkedin.com/in/vijay-rakkaiah-79a8b21b1/)

---

<div style="text-align: center;">
  ✨ <i>Thanks for checking out my project!</i> ✨<br>
  <i>Feel free to reach out with questions or collaboration ideas.</i>
</div>

""", unsafe_allow_html=True)
