# <==== Importing Dependencies ====>

import os
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import webbrowser
import base64


# <==== Code starts here ====>

courses_list = pickle.load(open('courses.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
link_list = pickle.load(open('links.pkl','rb'))

def recommend(course):
    index = courses_list[courses_list['course_name'] == course].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_course_names = []
    for i in distances[1:7]:
        course_name = courses_list.iloc[i[0]].course_name
        course_rating = link_list.iloc[i[0]].course_rating
        difficulty_level = link_list.iloc[i[0]].difficulty_level
        link = link_list.iloc[i[0]].course_url
        if course_name not in recommended_course_names:
            link = '[Click Here]({})'.format(link)
            with st.expander(course_name, expanded=False):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.caption("Course Rating")
                    st.markdown("{}⭐".format(course_rating))
                with col2:
                    st.caption("Difficulty")
                    st.markdown(difficulty_level)
                with col3:
                    st.caption("Link")
                    st.markdown(link)


        recommended_course_names.append(course_name)


# def getRating(course):
#     index = n_d[n_d['course_rating'] == course]
#     return index       
         
# def getLink(course):
#     index = link_list[link_list['course_name'] == course]
#     return index

# def getDifficulty(course):
#     index = n_d[n_d['difficulty_level'] == course]
#     return index
# st.image('coursera.png')
st.markdown("<h2 style='text-align: center; color: black;'>Course Recommendation System</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #b3b3ff;'>Find similar courses from a dataset of over 3,000 courses from Coursera!</h4>", unsafe_allow_html=True)


course_list = courses_list['course_name'].values
selected_course = st.selectbox(
    "Type or select a course you like :",
    courses_list
)

if st.button('Show Recommended Courses'):
    st.markdown("<h5 style=''>Recommended Courses based on your interests are :</h5>",unsafe_allow_html=True)
    recommend(selected_course)

    

# def get_base64(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()

# def set_background(png_file):
#     bin_str = get_base64(png_file)
#     page_bg_img = '''
#   <style>
# .stApp {
#   background-image: url("data:image/png;base64,%s");
#   background-size: cover;
# }
# </style>
#     ''' % bin_str
#     st.markdown(page_bg_img, unsafe_allow_html=True)

# set_background('lap.png')
st.subheader('Done by:💻')

st.markdown("[<p style='text-align: center; color: #777;'>P.Vishnu Vardhan(18311A05A6)</p>](https://github.com/vivavishnu)", unsafe_allow_html=True)
st.markdown("[<p style='text-align: center; color: #777;'>Thatikonda Nandini(18311A05B5)</p>](https://github.com/ThatikondaNandini)", unsafe_allow_html=True)
st.markdown("[<p style='text-align: center; color: #777;'>Neha Farath(18311A05A3)</p>](https://github.com/ThatikondaNandini)", unsafe_allow_html=True)