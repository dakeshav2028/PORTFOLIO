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
    st.markdown("[🔗 LinkedIn Post](https://www.linkedin.com/posts/keshav-sardaofficial_datascience-machinelearning-python-activity-7357710707989131264-4n2T?utm_source=share&utm_medium=member_desktop&rcm=ACoAAER9uc4B7yd9IoNsokiJHNOWQx2ibt3TM7E)")

    st.markdown("### 3. Google-Play-Store-Review-Analytics ")
    st.write("Created data visualization using google play store review datasets")
    st.markdown("[🔗 GitHub Repo](https://github.com/dakeshav2028/Keshav_google-play-store-review-analytics.git)")
    st.markdown("[🔗 LinkedIn Post](https://www.linkedin.com/posts/keshav-sardaofficial_dataanalytics-python-googleplaystore-activity-7291171445638893568-Zn7F?utm_source=share&utm_medium=member_desktop&rcm=ACoAAER9uc4B7yd9IoNsokiJHNOWQx2ibt3TM7E)")
    
    st.markdown("### 4. Predicting-Graduate-School-Admissions")
    st.write("Predicted-Graduate-School-Admissions using various ML models.")
    st.markdown("[🔗 GitHub Repo](https://github.com/dakeshav2028/Predicting-Graduate-School-Admissions.git)")
    st.markdown("[🔗 LinkedIn Post](https://www.linkedin.com/posts/keshav-sardaofficial_kaggle-machinelearning-datascience-activity-7352415913716965376-QGPD?utm_source=share&utm_medium=member_desktop&rcm=ACoAAER9uc4B7yd9IoNsokiJHNOWQx2ibt3TM7E)")

# Dashboards Page
elif page == "Dashboards":
    st.title("📈 Amazon-Prime-Video-Data-Analysis")
    st.markdown("#### Power BI Dashboard")
    powerbiurl = "my2nddash.pbix"
    st.components.v1.iframe(powerbiurl, width=800, height=600)

    st.title("📈 Data Professional Survey Breakdown")
    st.markdown("#### Power BI Dashboard")
    powerbiurl = "my3rddash.pbix"
    st.components.v1.iframe(powerbiurl, width=800, height=600)

# About Me Page
elif page == "About Me":
    st.title("🙋 About Me")
    st.write("""
    - 🎓 B.Tech CSE (AI-ML), 3rd Year @ JECRC University  
    - 🔍 Passionate about Data Analytics, Machine Learning, and Business Insights  
    - 🛠 Skills: Python, SQL, Excel, Pandas, NumPy, Power BI, Plotly  
    """)
# Certifications
elif page == "Certifications":
    st.title("📜📜 Certificates")
    st.write("[Tata - Data Visualisation](https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/ifobHAoMjQs9s6bKS/MyXvBcppsW2FkNYCX_ifobHAoMjQs9s6bKS_WSHeaWFR25fPK2ywp_1751211372883_completion_certificate.pdf)")
    st.write("🔗 [Deloitte Australia - Data Analytics Job Simulation](https://forage-uploads-prod.s3.amazonaws.com/completion-certificates/9PBTqmSxAf6zZTseP/io9DzWKe3PTsiS6GG_9PBTqmSxAf6zZTseP_WSHeaWFR25fPK2ywp_1739816223784_completion_certificate.pdf)")
    st.write("💻 [Data Analysis Using Python – Samatrix.io](https://verify.netcredential.com/roy8pgLIPV)")
    st.write("📊 [SQL (Intermediate)](https://www.hackerrank.com/certificates/iframe/9e897c730e8e)")
    st.write("📊 [NASA International Space Apps Challenge  Global Nominee](https://www.linkedin.com/posts/keshav-sardaofficial_nasa-international-space-apps-challenge-2024-activity-7248592852018970624-_XCk?utm_source=share&utm_medium=member_desktop&rcm=ACoAAER9uc4B7yd9IoNsokiJHNOWQx2ibt3TM7E)")
#Internship
elif page == "Internship":
    st.title("Internship")
    st.write("💻 [Data Science Intern– CodVeda Technologies]()")
    st.write("💻 [Data Analyst Intern– Samatrix.io]()")
    st.write("📊 [Data Science Intern-NullClass)](https://www.nullclass.com/certificates/67a0683c6055f48cf895b518)")
# Contact Page
elif page == "Contact":
    st.title("📬 Contact Me")
    st.write("📧 Email: dakeshav000@gmail.com")
    st.write("🔗 [LinkedIn](https://www.linkedin.com/in/keshav-sardaofficial/)")
    st.write("💻 [GitHub](https://github.com/dakeshav2028)")
    st.write("📊 [Kaggle](https://www.kaggle.com/keshavsarda123)")
    st.download_button("📄 Download Resume", data=open("resume.pdf", "rb"), file_name="KESHAV SARDA resume.pdf")




