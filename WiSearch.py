import streamlit as st
from datetime import datetime, timedelta


st.markdown("<h1 style='text-align: center;'>WiSearch</h1>", unsafe_allow_html=True)
st.write("Welcome! WiSearch is a simple tool that aims to educate job seekers and non-tech peoples about the importance of Google Dorking by making their job search easier.")
st.warning("Fill The Following Details and Please Avoid Spell Mistakes")
# User inputs
job_title = st.text_input("Job Title")
skills = st.text_input("Skills: communication, python, java, presentation...")
location = st.text_input("Location (City/Country)")
job_board_options = ["Not Specific", "linkedin.com", "indeed.com", "naukri.com"]
job_board = st.selectbox("Job Board", job_board_options)
fresher_options = ['Fresher','Experienced']
fresher = st.selectbox("fresher", fresher_options)
time_range = st.selectbox("Select Time Range", ["All Time", "Today", "This Week", "This Month"])


# Dorking
if st.button("Generate Query"):
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

    if time_range:
        today = datetime.today().date()
        if time_range == "Today":
            today = datetime.today().date()
            today_date = today.strftime("%Y-%m-%d")
            query += f'daterange:{today_date} '
        elif time_range == "This Week":
            week_date = today - timedelta(days=7)
            today_date = today.strftime("%Y-%m-%d")
            query += f'after:{week_date} '
        elif time_range == "This Month":
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
    
st.subheader("What is Google Dorking")
st.markdown("Google Dorking is a technique of using specialized search operators to find advanced search results. It can be used for job search by using keywords related to the job title, location, company, and other relevant factors. Google Dorking can be a powerful tool for job seekers, but it is important to use it ethically and responsibly.")
st.markdown('Learn more about [Google Dorking](https://en.wikipedia.org/wiki/Google_hacking)')

