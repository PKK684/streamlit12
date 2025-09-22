import streamlit as st

# Set page config
st.set_page_config(page_title="My Bio", page_icon="👤", layout="centered")

# Title
st.title("👤 Prem Kumar k ")

# Personal Information
st.header("Personal Information")
st.write("""
- **Name:** Prem Kumar  
- **Age:** 20  
- **Gender:** Male  
- **Email:** premkumar@example.com  
- **Phone:** +91 9876543210  
- **Address:** Chennai , India
""")

# Education
st.header("🎓 Education")
st.write("""
- **BCA in Computer application ** – peri institue (2022 - 2025)   
- **High School** – SRM matric hr sec  School (2019 - 2020)  
""")

# Skills
st.header("💡 Skills")
skills = ["Python", "Java", "C++",  "Web Development"]
st.write(", ".join(skills))



# Hobbies
st.header("🎯 Hobbies")
st.write("""
- Reading Tech Blogs  
- Playing Chess  
- Exploring AI/ML   
- Coding Challenges  
""")

#
# Footer
st.markdown("---")
st.markdown("✅ *Made with ❤️ using Streamlit*")
