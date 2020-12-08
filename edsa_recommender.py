"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Changing the background
import base64

@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('resources/imgs/Back8.jpg')

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    st.sidebar.title("Pages")
    page_options = ["Home","Exploratory Data Analysis(EDA)","Recommender System","Solution Overview","About"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        title_SO = """
	    <div style="background-color:#464e5f00;padding:10px;border-radius:10px;margin:10px;border-style:solid; border-color:#000000; padding: 1em;">
	    <h1 style="color:black;text-align:center;">Solution Overview</h1>
        """
        st.markdown(title_SO, unsafe_allow_html=True)
        #st.title("Solution Overview")
        st.image('resources/imgs/sol.jpeg',use_column_width=True)
        st.write("Describe your winning approach on this page")

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.

    # Home
    if page_selection == "Home":
        st.image('resources/imgs/EDSA_logo.png',use_column_width=True)

        html_temp = """
	    <div style="background-color:{};padding:10px;border-radius:10px;margin:10px;border:3px; border-style:solid; border-color:#000000; padding: 1em;">
	    <h1 style="color:{};text-align:center;">UNSUPERVISED PREDICT</h1>
	    </div>
	    """
        
        title_temp = """
	    <div style="background-color:#464e5f00;padding:10px;border-radius:10px;margin:10px;border-style:solid; border-color:#000000; padding: 1em;">
	    <h1 style="color:black;text-align:center;">Recommender System</h1>
	    <h2 style="color:black;text-align:center;">Team:3</h2>
	    <h2 style="color:black;text-align:center;">July 2020</h3>
	    </div>
	    """
        st.markdown(html_temp.format('#D2691E00','black'), unsafe_allow_html=True)
        st.markdown(title_temp, unsafe_allow_html=True)
    

    # EDA
    if page_selection == "Exploratory Data Analysis(EDA)":
        title_eda = """
	    <div style="background-color:#464e5f00;padding:10px;border-radius:10px;margin:10px;border-style:solid; border-color:#000000; padding: 1em;">
	    <h1 style="color:black;text-align:center;">Exploratory Data Analysis(EDA)</h1>
        """
        st.markdown(title_eda, unsafe_allow_html=True)

        st.image('resources/imgs/EDA6.png',use_column_width=True)
    
    #About
    if page_selection == "About":
        title_about = """
	    <div style="background-color:#464e5f00;padding:10px;border-radius:10px;margin:10px;">
	    <h1 style="color:black;text-align:center;"> - The Team -</h1>
        <h3 style="color:black;text-align:right;">We are a team of data science students from Explore Data Science Academy. This is our project for the 2020 July unsupervised sprint.</h3>
        """
        mission = """
	    <div style="background-color:#464e5f00;padding:10px;border-radius:10px;margin:10px;">
	    <h1 style="color:black;text-align:center;"> - Our Mission - </h1>
        <h3 style="color:black;text-align:center;">To keep you entertained by helping you find movies you're most likely to enjoy&#128515</h3>
        """
        contributors = """
        <div style="background-color:#464e5f00;padding:10px;border-radius:10px;margin:10px;">
	    <h1 style="color:black;text-align:center;"> - Contributors -</h1>
        <h3 style="color:black;text-align:center;">Thapelo Mojela</h3>
        <h3 style="color:black;text-align:center;">Presca Mashamaite</h3>
        <h3 style="color:black;text-align:center;">Mpho Mokhokane</h3>
        <h3 style="color:black;text-align:center;">Josias Sekhebesa</h3>
        <h3 style="color:black;text-align:center;">Bukelwa Mqhamane</h3>
        """
        st.markdown(title_about, unsafe_allow_html=True)
        st.markdown(mission, unsafe_allow_html=True)
        st.markdown(contributors, unsafe_allow_html=True)



if __name__ == '__main__':
    main()
