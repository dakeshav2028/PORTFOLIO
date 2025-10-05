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
# Home Page
if menu == "Home":
    st.title("👋 Hi, I'm Keshav Sarda")
    st.subheader("Data Enthusiast | Transforming Data into Insights")
    st.write("I'm passionate about Data Analytics, Visualization, and Machine Learning.")
    st.image("k1086.jpg", width=200)

# Projects Page
elif menu == "Projects":
    st.title("📊 My Projects")

    st.markdown("### 1. Sales Data Analysis for a Pizza Chain using SQL")
    st.write("Analyzed sales trends, customer segmentation, and profit margins.")
    st.markdown("[🔗 GitHub Repo](https://github.com/dakeshav2028/pizza-sales-analysis-using-sql.git)")

    st.markdown("### 2. Predicting House Price Of USA")
    st.write("Predicted house prices of USA using various ML models.")
    st.markdown("[🔗 GitHub Repo](https://github.com/dakeshav2028/Predicting-House-Price-Of-USA.git)")
    st.markdown("[🔗 LinkedIn Post](https://www.linkedin.com/posts/keshav-sardaofficial_datascience-machinelearning-python-activity-7357710707989131264-4n2T)")

    st.markdown("### 3. Google Play Store Review Analytics")
    st.write("Created data visualization using Google Play Store review datasets")
    st.markdown("[🔗 GitHub Repo](https://github.com/dakeshav2028/Keshav_google-play-store-review-analytics.git)")
    st.markdown("[🔗 LinkedIn Post](https://www.linkedin.com/posts/keshav-sardaofficial_dataanalytics-python-googleplaystore-activity-7291171445638893568-Zn7F)")

    st.markdown("### 4. Predicting Graduate School Admissions")
    st.write("Predicted Graduate School Admissions using various ML models.")
    st.markdown("[🔗 GitHub Repo](https://github.com/dakeshav2028/Predicting-Graduate-School-Admissions.git)")
    st.markdown("[🔗 LinkedIn Post](https://www.linkedin.com/posts/keshav-sardaofficial_kaggle-machinelearning-datascience-activity-7352415913716965376-QGPD)")

# Dashboards Page
elif menu == "Dashboards":
    st.title("📈 Dashboards")

    st.markdown("#### Amazon Prime Video Data Analysis (Power BI)")
    uploaded_file = st.file_uploader("my2nddash", type=["pbix"])
    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        st.write(f"File name: {uploaded_file.name}")
   
    st.markdown("#### Data Professional Survey Breakdown (Power BI)")
    uploaded_file = st.file_uploader("my3rddash", type=["pbix"])
    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        st.write(f"File name: {uploaded_file.name}")
# About Me Page
elif menu == "About Me":
    st.title("🙋 About Me")
    st.write("""
    - 🎓 B.Tech CSE (AI-ML), 3rd Year @ JECRC University  
    - 🔍 Passionate about Data Analytics, Machine Learning, and Business Insights  
    - 🛠 Skills: Python, SQL, Excel, Pandas, NumPy, Power BI, Plotly  
    """)

# Certifications Page
elif menu == "Certifications":
    st.title("📜 Certificates")
    st.write("[Tata - Data Visualisation](https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/ifobHAoMjQs9s6bKS/MyXvBcppsW2FkNYCX_ifobHAoMjQs9s6bKS_WSHeaWFR25fPK2ywp_1751211372883_completion_certificate.pdf)")
    st.write("[Deloitte Australia - Data Analytics Job Simulation](https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/9PBTqmSxAf6zZTseP/io9DzWKe3PTsiS6GG_9PBTqmSxAf6zZTseP_WSHeaWFR25fPK2ywp_1739816223784_completion_certificate.pdf)")
    st.write("[Data Analysis Using Python – Samatrix.io](https://verify.netcredential.com/roy8pgLIPV)")
    st.write("[SQL (Intermediate) - HackerRank](https://www.hackerrank.com/certificates/iframe/9e897c730e8e)")
    st.write("[NASA Space Apps Challenge Global Nominee](https://www.linkedin.com/posts/keshav-sardaofficial_nasa-international-space-apps-challenge-2024-activity-7248592852018970624-_XCk)")

# Internship Page
elif menu == "Internship":
    st.title("💼 Internship")
    with open("Keshav Sarda (2).pdf", "rb") as f:
        st.download_button("Download Data Science Intern (CodVeda Technologies)", f, "CodVeda_Internship.pdf")
    with open("1754331037168.pdf", "rb") as f:
        st.download_button("Download Data Analyst Intern (Samatrix.io)", f, "Samatrix_Internship.pdf")
    st.write("[Data Science Intern - NullClass](https://www.nullclass.com/certificates/67a0683c6055f48cf895b518)")

# Contact Page
elif menu == "Contact":
    st.title("📬 Contact Me")
    st.write("📧 Email: dakeshav000@gmail.com")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/keshav-sardaofficial/)")
    st.write("💻 [GitHub](https://github.com/dakeshav2028)")
    st.write("📊 [Kaggle](https://www.kaggle.com/keshavsarda123)")
    with open("Keshav Sarda resume.pdf", "rb") as f:
        st.download_button("📄 Download Resume", f, "Keshav Sarda resume.pdf")


