import streamlit as st

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Dashboards", "About Me", "Contact"])

# Home Page
if page == "Home":
    st.title("👋 Hi, I'm Keshav Sarda")
    st.subheader("Data Enthusiast | Transforming Data into Insights")
    st.write("I'm passionate about Data Analytics, Visualization, and Machine Learning.")
    st.image("k1086.jpg", width=200) 

# Projects Page
elif page == "Projects":
    st.title("📊 My Projects")
    st.markdown("### 1. Sales Data Analysis for a Pizza Chain using SQL")
    st.write("Analyzed sales trends, customer segmentation, and profit margins.")
    st.markdown("[🔗 GitHub Repo](https://github.com/dakeshav2028/pizza-sales-analysis-using-sql.git)")

    st.markdown("### 2. Predicting-House-Price-Of-USA ")
    st.write("Predicted house prices of USA using various ML models.")
    st.markdown("[🔗 GitHub Repo](https://github.com/dakeshav2028/Predicting-House-Price-Of-USA.git)")

# Dashboards Page
elif page == "Dashboards":
    st.title("📈 Amazon-Prime-Video-Data-Analysis")
    st.markdown("#### Power BI Dashboard")
    powerbiurl = "https://app.powerbi.com/groups/me/reports/c31aad3b-3c82-4121-ae69-e9c3e5e02083/bb7583fb0d05b7b2c19c?experience=power-bi"
    st.components.v1.iframe(powerbiurl, width=800, height=600)

    st.title("📈 Data Professional Survey Breakdown")
    st.markdown("#### Power BI Dashboard")
    powerbiurl = "https://app.powerbi.com/groups/me/reports/e5d3ad07-14fe-480d-9fc6-0cb73d8b967c/12ff61053de650030d02?experience=power-bi"
    st.components.v1.iframe(powerbiurl, width=800, height=600)

# About Me Page
elif page == "About Me":
    st.title("🙋 About Me")
    st.write("""
    - 🎓 B.Tech CSE (AI-ML), 3rd Year @ JECRC University  
    - 🔍 Passionate about Data Analytics, Machine Learning, and Business Insights  
    - 🛠 Skills: Python, SQL, Excel, Pandas, NumPy, Power BI, Plotly  
    """)

# Contact Page
elif page == "Contact":
    st.title("📬 Contact Me")
    st.write("📧 Email: dakeshav000@gmail.com")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/keshav-sardaofficial/)")
    st.write("💻 [GitHub](https://github.com/dakeshav2028)")
    st.write("📊 [Kaggle](https://www.kaggle.com/keshavsarda123)")
    st.download_button("📄 Download Resume", data=open("resume.pdf", "rb"), file_name="KESHAV SARDA resume.pdf")
