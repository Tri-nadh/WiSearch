import streamlit as st
from datetime import datetime, timedelta

st.markdown("<h1 style='text-align: center;'>WiSearch</h1>", unsafe_allow_html=True)
st.write("Welcome! WiSearch is a simple tool that aims to educate job seekers and non-tech peoples about the importance of Google Dorking by making their job search easier.")
st.warning("1. Fill The Following Details \n 2. Please Avoid Spell Mistakes \n 3. Bookmark this tool for better access")
st.header("Internet Search", divider='rainbow')

# User inputs
job_title = st.text_input("Job Title")
skills = st.text_input("Skills: communication, python, java, presentation...")
location = st.text_input("Location (City/Country)")
job_board_options = ["Not Specific", "linkedin.com", "indeed.com", "naukri.com", "lever.co", "greenhouse.io"]
job_board = st.selectbox("Job Board", job_board_options)
fresher_options = ['Fresher','Experienced']
fresher = st.selectbox("fresher", fresher_options)
time_range = st.selectbox("Select Time Range", ["All Time", "Today", "This Week", "This Month"])

# Dorking
if st.button("Search"):
    query = ""

    if job_title:
        query += f'intitle:"{job_title}" '

    if skills:
        query += f'intext:"{skills}" '


    if location:
        query += f'intext:"{location}" '

    if job_board:
        if job_board == 'linkedin.com':
            query += f'site:"{job_board}"  '

        elif job_board == 'indeed.com':
            query += f'site:"{job_board}" '

        elif job_board == 'naukri.com':
            query += f'site:"{job_board}" '

        elif job_board == "Not Specific":
            query += 'inurl:"careers" OR inurl:"jobs" '

        elif job_board == 'lever.co':
            query += f'site:"{job_board}" '

        elif job_board == 'greenhouse.io':
            query += f'site:"{job_board}" '

    if time_range:
        today = datetime.today().date()
        if time_range == "Today":
            today = datetime.today().date()
            today_date = today.strftime("%Y-%m-%d")
            query += f'daterange:{today_date} '
        if time_range == "This Week":
            week_date = today - timedelta(days=7)
            today_date = today.strftime("%Y-%m-%d")
            query += f'after:{week_date} '
        if time_range == "This Month":
            month_date = today - timedelta(days=30)
            today_date = today.strftime("%Y-%m-%d")
            query += f'after:{month_date} '

    if fresher:
        if fresher == 'Fresher':
            query += 'intext:"Entry level" OR "fresher" OR "Early careers" OR "0 -"'

    if query:
        #st.subheader("Copy paste this query on Google:")
        #st.warning(query)
        #st.subheader("OR")

        
        # Create a clickable link to search on Google
        st.subheader("Here we are")
        query = query.replace(' ', '+')
        google_search_url = f"https://www.google.com/search?q={query}"
        st.markdown(f"[**Click Here to Go**]({google_search_url})")
        st.write("**All The Best, Thank you for using WiSearch**")
    else:
        st.warning("Please provide at least one input.")
st.markdown("Follow on [GitHub](https://github.com/Tri-nadh/WiSearch)")
    
st.header("Linkedin Posts Search", divider='rainbow')
post = st.text_input("Enter One Skill You are looking for")
query_post = f'intext:{post} inurl:activity intext:"hiring for" OR intext:"Job Openings" site:linkedin.com'
if st.button("Get Query"):
    st.subheader("Here we are")
    query_post = query_post.replace(' ', '+')
    google_search_url = f"https://www.google.com/search?q={query_post}"
    st.markdown(f"[**Click Here to Go**]({google_search_url})")
    st.write("**All The Best, Thankyou for using my Webapp**")

