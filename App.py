from pathlib import Path

import streamlit as st
from PIL import Image

##---PATH SETTINGS ---

current_dir = Path(_file_).parent if "_file_" in locals() else Path.cwd()
css_file = current_dir / "Styles" / "main.css"
resume_file = current_dir / "Assets" / "CV.pdf"
profile_pic = current_dir / "Assets" / "ProfilePic.jpeg"



#---GENERAL SETTINGS --

PAGE_TITLE = "Digital Resume| Kevin Juma"
PAGE_ICON = ":wave:"
NAME = "Kevin Juma"
DESCRIPTION = """
Data Analyst III - CENTENE CORPORATION
"""
EMAIL = "kipischesis@gmail.com"

SOCIAL_MEDIA = {
"Youtube": "https://www.youtube.com/channel/UCMxArhFtxZp6c0j3kTft_UA",
"LinkedIn": "https://www.linkedin.com/in/kevin-juma-95782885/",
"Github": "https://github.com"
}

PROJECTS = {
}

st.set_page_config(page_title = PAGE_TITLE, page_icon = PAGE_ICON)

# ----LOAD CSS, PDF & PROFILE PIC ---

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html = True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    profile_pic = Image.open(profile_pic)


#---HERO SECTION ---
col1,col2 = st.columns(2, gap = "small")
with col1:
    st.image(profile_pic, width = 230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label ="📄 Download Resume",
        data = PDFbyte,
        file_name = resume_file.name,
        mime = "application/octet-stream",
        )
    st.write("🏠 670 Materdie Lane Florissant MO 63031")
    st.write(EMAIL)
    st.write("☎️ 314-480-2753")

#  ---  SOCIAL LINKS --

st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")
    


# ---EXPERIENCE & QUALIFICATIONS --

st.write("#")
st.subheader("Profile Summary")
st.write(
    """

- ✅ Possess more than 4 years of hands-on experience in cleaning, analyzing, and presenting insights derived from both structured and unstructured data.
- ✅ Proficient in utilizing Excel, SQL, Power BI, Python, and R for data manipulation and analysis.
- ✅ Certified as a Microsoft Power BI Data Analyst Associate, showcasing expertise in leveraging Power BI for comprehensive data analytics.
- ✅ Demonstrate strong teamwork skills and a proactive approach to task execution, contributing effectively within a collaborative environment.

    """    
)

# ---skills --

st.write("#")
st.subheader("Hard Skills")
st.write(
    """

- 💻 Programming: SQL, Python, R & VBA
- 📊 Data Visualization: Power BI, Excel
- 📚 Modeling: Regression, Decision Tree, Factor Analysis, PCA
- 📄 Databases: Teradata, MySQL, Snowflake
    """    
)


# --WORK HISTORY ---

st.write("#")
st.subheader("Experience")
st.write("---")

# ---JOB 1

st.write("**Data Analyst III | Centene Corporation**")
st.write("***04/2023 - Present***")
st.write(
    """
- Build Power BI dashboards by leveraging Power platform capabilities to improve Report delivery. Month-end close issues have reduced by over 80% with the incorporation of Power BI.
- Identify and perform root cause analysis of Data irregularities and Present findings as well as proposed Solutions to Management and IT team for Implementation. This has saved the company over $4 Million in possible sanctions by Medicaid States.
- Develop, maintain and troubleshoot complex SQL codes used to analyze data from multiple sources including Claims, Provider, Member and Encounter data. I have become Subject matter expert and involved in training and onboarding of new analyst.
""")

# ---JOB 2

st.write("**Data Analyst II | Centene Corporation**")
st.write("***08/2021 - 04/2023***")
st.write(
    """
- Responsible for creating, validating and reporting on Wellcare and Medicare Lags Month-end Financial Close Lags. Using Power Query, Python and Power BI has reduced validation process to under 2 hours.
- Designing and developing effective Power BI reports and dashboards to support Business needs and Month-end reporting.
- Work closely with IT partners to ensure timely implementation of Agile Jira Tickets based on requirements from Stakeholders on data needs and report specifications.
- Identify and perform root cause analysis of Data irregularities and Present findings as well as proposed Solutions to Management and IT team for Implementation.
- Develop, maintain and troubleshoot complex SQL codes used to analyze data from multiple sources including Claims, Provider, Member and Encounter data.
- Staying up-to-date with industry trends and best practices related to Power BI and Data visualization

""")

# ---JOB 3

st.write("**Data Analyst I | Centene Corporation**")
st.write("***07/2020 - 07/2021***")
st.write(
    """
- Resposible for creating and producing Monthly lags, Quarterly and Monthly State Reports for Four different Health Plans.
- Involved in Wellcare Data implementation in the EDW by ensuring Accuracy and Integrity of the data. Wellcare Excelys Plans have since received sign off and can now be booked by Accounting and Reporting Purposes.
- Identify and perform root cause analysis of Data irregularities and Present findings as well as proposed Solutions to Management and IT team for Implementation.
- Develop, maintain and troubleshoot complex SQL codes used to analyze data from multiple sources including Claims, Provider, Member and Encounter data.
- Assist in creating reports for multiple Ad hoc Requests from Healthplans as well as KPMG Audit requests .


""")

# ---JOB 4

st.write("**Business Analyst I | Centene Corporation**")
st.write("***01/2020 - 07/2020***")
st.write(
    """
- Manage the end-to-end enrollment process to ensure accurate and timely setup for claims payment, member assignment and directory display.
- Created reports in SQL and MicroStrategy on claims that were aging, those that are paying with incorrect information and those that came to our team’s inventory more than five times.
- Worked with the Provider Data Management team to create a two-way match and three-way match affiliations needed to pay claims. We managed to bring down the average age of claims from 30 days to 15 days.
- Worked on escalated claims to ensure that certain provider’s and practitioner’s claims are correctly entered In the Oracle database PORTICO and AMISYS.
- Monitoring performance to ensure established credentialing and provider data quality benchmarks are met.


""")

# ---JOB 5

st.write("**Graduate Teaching Assistant | Southern Illinois University Edwardsville**")
st.write("***01/2017 - 12/2019***")
st.write(
    """
- Taught Data Management , Probability Simulations and Hypothesis testing Analysis in R and MINITAB.
- Guided students to make technical presentations of the data collected and the subsequent analysis.
- Earned positive verbal/written feedback from students regarding classroom instruction and learning success.
- Hold responsibility in grading quizzes and tests, as well as leading discussion of course contents every week.
- Facilitate review section prior to examinations and provided feedback on student practice presentations.


""")
