import streamlit as st

# --- Custom CSS for horizontal menu ---
st.markdown(
    """
    <style>
    .horizontal-bar {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-bottom: 20px;
    }
    .horizontal-bar label {
        font-weight: bold;
        cursor: pointer;
        padding: 8px 16px;
        border-radius: 8px;
        background-color: #f0f2f6;
        transition: all 0.3s;
    }
    .horizontal-bar label:hover {
        background-color: #4CAF50;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Navigation Menu ---
menu = st.radio(
    "Navigation", 
    ["Home", "Projects", "Dashboards", "About Me", "Certifications", "Internship", "Contact"], 
    horizontal=True,
    label_visibility="collapsed"   # hides the "Navigation" label
)

# --- Pages ---
if menu == "Home":
    st.title("👋 Hi, I'm Keshav Sarda")
    st.subheader("Data Enthusiast | Transforming Data into Insights")
    st.write("I'm passionate about Data Analytics, Visualization, and Machine Learning.")
    st.image("k1086.jpg", width=200)

elif menu == "Projects":
    st.title("📊 My Projects")
    st.markdown("### 1. Sales Data Analysis for a Pizza Chain using SQL")
    st.write("Analyzed sales trends, customer segmentation, and profit margins.")
    st.markdown("[🔗 GitHub Repo](https://github.com/dakeshav2028/pizza-sales-analysis-using-sql.git)")
    # ... (rest of your projects here)

elif menu == "Dashboards":
    st.title("📈 Dashboards")
    st.markdown("#### Amazon Prime Video Data Analysis (Power BI)")
    st.components.v1.iframe("https://app.powerbi.com/view?r=YOUR_EMBED_LINK", width=800, height=600)

elif menu == "About Me":
    st.title("🙋 About Me")
    st.write("""
    - 🎓 B.Tech CSE (AI-ML), 3rd Year @ JECRC University  
    - 🔍 Passionate about Data Analytics, Machine Learning, and Business Insights  
    - 🛠 Skills: Python, SQL, Excel, Pandas, NumPy, Power BI, Plotly  
    """)

elif menu == "Certifications":
    st.title("📜 Certificates")
    st.write("[Tata - Data Visualisation](https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/ifobHAoMjQs9s6bKS/...)")
    # ... (rest of certifications)

elif menu == "Internship":
    st.title("💼 Internship")
    with open("Keshav Sarda (2).pdf", "rb") as f:
        st.download_button("Download Data Science Intern (CodVeda Technologies)", f, "CodVeda_Internship.pdf")

elif menu == "Contact":
    st.title("📬 Contact Me")
    st.write("📧 Email: dakeshav000@gmail.com")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/keshav-sardaofficial/)")
    st.write("💻 [GitHub](https://github.com/dakeshav2028)")
    st.write("📊 [Kaggle](https://www.kaggle.com/keshavsarda123)")
    with open("resume.pdf", "rb") as f:
        st.download_button("📄 Download Resume", f, "Keshav_Sarda_Resume.pdf")
