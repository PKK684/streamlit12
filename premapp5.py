import streamlit as st

# Set page config
st.set_page_config(page_title="My Bio", page_icon="👤", layout="centered")

# Title
st.title("👤 Prem Kumar - Biodata")

# Personal Information
st.header("Personal Information")
st.write("""
- **Name:** Prem Kumar  
- **Age:** 22  
- **Gender:** Male  
- **Email:** premkumar@example.com  
- **Phone:** +91 9876543210  
- **Address:** Your City, India
""")

# Education
st.header("🎓 Education")
st.write("""
- **B.Tech in Computer Science** – XYZ University (2021 - 2025)  
- **Intermediate** – ABC Junior College (2019 - 2021)  
- **High School** – DEF School (2018 - 2019)  
""")

# Skills
st.header("💡 Skills")
skills = ["Python", "Java", "C++", "Machine Learning", "Data Analysis", "Web Development"]
st.write(", ".join(skills))

# Projects
st.header("📂 Projects")
st.write("""
1. **Library Management System** – A Java project using MySQL database.  
2. **Online Voting System** – Web-based project using JSP & Servlet.  
3. **ML Project: Pirated Software Detection** – Built a classifier to detect pirated software.  
""")

# Hobbies
st.header("🎯 Hobbies")
st.write("""
- Reading Tech Blogs  
- Playing Chess  
- Exploring AI/ML Projects  
- Coding Challenges  
""")

# Resume Viewer
st.header("📄 My Resume")
with open("premkumar_resume.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="📥 Download Resume",
                   data=PDFbyte,
                   file_name="PremKumar_Resume.pdf",
                   mime="application/pdf")

st.write("### Preview:")
st.download_button("Click here to download", PDFbyte, "premkumar_resume.pdf")

# Embed resume inside app
st.components.v1.html(f"""
<iframe src="data:application/pdf;base64,{PDFbyte.encode('base64').decode()}" 
width="700" height="500" type="application/pdf"></iframe>
""", height=600)

# Footer
st.markdown("---")
st.markdown("✅ *Made with ❤️ using Streamlit*")
