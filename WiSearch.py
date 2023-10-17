import streamlit as st


st.markdown("<h1 style='text-align: center;'>WiSearch</h1>", unsafe_allow_html=True)
st.warning("Welcome! this simple webapp aims to educate job seekers and non-tech peoples about the importance of Google Dorking by making their job search easier.")
st.warning("Fill The Following Details and Please Avoid Spell Mistakes")
# User inputs
job_title = st.text_input("Job Title")
skills = st.text_input("Skills: communication, python, java, presentation...")
location = st.text_input("Location (City/Country)")
job_board_options = ["linkedin.com", "indeed.com", "naukri.com", "Not Specific"]
job_board = st.selectbox("Job Board", job_board_options)
fresher_options = ['Fresher','Experienced']
fresher = st.selectbox("fresher", fresher_options)


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
            query += 'site:"{job_board}" '

        elif job_board == "Not Specific":
            query += 'inurl:"careers" OR inurl:"jobs" '

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
        st.write("**All The Best, Thankyou for using my Webapp**")
    else:
        st.warning("Please provide at least one input.")

    

st.markdown("Follow on [GitHub](https://github.com/Tri-nadh/WiSearch)")
st.markdown("Google Dorking is a search technique that uses Google operators to find specific information on the internet. "
            "You can use this app to generate Google Dorking queries for job searches.")
st.markdown('Learn more about [Google Dorking](https://en.wikipedia.org/wiki/Google_hacking)')

