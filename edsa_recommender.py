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

set_png_as_page_bg('resources/imgs/Back7.jpg')

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    st.sidebar.title("Pages")
    page_options = ["Home","Exploratory Data Analysis(EDA)","Recommender System","Solution Overview","Business Pitch","About"]

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
        st.write("Our objective was to construct a recommendation algorithm based on the content or collaborative filtering, capable of accurately predicting how a user will rate a movie they have not yet viewed based on their historical preferences. We used a special version of the MovieLens dataset. Below is a description of the dataset we used")
        st.write("genome_scores - a score mapping the strength between movies and tag-related properties")
        st.write("genome_tags - user assigned tags for genome-related scores")
        st.write("imdb_data - Additional movie metadata scraped from IMDB using the links.csv file")
        st.write("links - File providing a mapping between a MovieLens ID and associated IMDB and TMDB IDs")
        st.write("tags - User assigned for the movies within the dataset")
        st.write("test - The test split of the dataset. Contains user and movie IDs with no rating data")
        st.write("train - The training split of the dataset. Contains user and movie IDs with associated rating data")
        st.write("The initial step was the data preprocessing and we looked for missing values. We discovered that there are missing values in three of the eight datasets we have.")

        imdb = """
	    <div style="background-color:#464e5f00;padding:10px;border-radius:10px;margin:10px;">
	    <h3 style="color:black;text-align:left;">Cleaning the imdb_data dataset</h3>
        """
        st.markdown(imdb, unsafe_allow_html=True)
        st.write('We imputed the runtime with the mean runtime\n\nCreated a list plot keywords for each movie.\n\nCreated a list of title casts for each movie.')

        movies = """
	    <div style="background-color:#464e5f00;padding:10px;border-radius:10px;margin:10px;">
	    <h3 style="color:black;text-align:left;">Cleaning the movies dataset</h3>
        """
        st.markdown(movies, unsafe_allow_html=True)
        st.write('Created a list of genres in every movie in the movies column\n\nAdded the releasea_year column.')

        st.write('After cleaning the data, we then merged the data')
        st.write('We proceeded to the second step, the EDA. We constructed various plots using our data and gathered insights from our data, these are well documented on our Exploratory Data Analysis(EDA) page.')

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
    
        #options = ["Ratings","Movies","Directors","Genres","Title Cast"]

        sys_eda = st.radio("Choose an EDA section",
        ('Ratings','Movies','Directors','Genres','Title Cast'))

        #option_selection = st.selectbox("Choose Option", options)
        if sys_eda == "Ratings":
        #if option_selection == "Ratings":
            #options_ratings = ["Top 10 users by number of ratings","Top 10 users by number of ratings(No outlier)","Rating distribution"]
            #rating_option = st.selectbox("Choose Option", options_ratings)

            op_ratings = st.radio("Choose",("Top 10 users by number of ratings","Top 10 users by number of ratings(No outlier)","Rating distribution"))

            if op_ratings == "Top 10 users by number of ratings":
                #if rating_option == "Top 10 users by number of ratings":
                st.image('resources/imgs/Top 10 users by number of rating.png',use_column_width=True)
                st.write('visualizing the top 10 users by number of ratins we see that user 72315 is an outlier in the sense he/she has rated an extreme number of movies compared to the rest of the users, there being a difference of 9272 ratings betwen user 12952 and user 80974 , This means that our system "better knows" user 72315 and his/her preferences and as such it would be easy for our recommeder system to recommend movies they would enjoy.')
            if op_ratings == "Top 10 users by number of ratings(No outlier)":
            #if rating_option == "Top 10 users by number of ratings(No outlier)":
                st.image('resources/imgs/rating_no_outlier.png',use_column_width=True)
                st.write("Removing the outlier user 72315 we see that the rest of users have not rated an extreme number of movies comapred to each other.Now that we've looked into the number of ratings for each user, we can now investigate the distribution of ratings")
                st.write("Most review sites use a 1 to 5 star rating system, with")
                st.write("5 star : Excellent\n\n4.0 – 5.0 stars : Positive Reviews\n\n3.0 - 3.9 stars : Neutral Reviews\n\n1.0 - 2.9 star : Negative Reviews")
            if op_ratings == "Rating distribution":
            #if rating_option == "Rating distribution":
                st.image('resources/imgs/rating_dist.png',use_column_width=True)
                st.write("Checking the distribution of ratings we see that rating of 4.0 is the most popular rating accounting for 27% of the ratings which suggests that most users have found most movies to be good but not not excellent, then again no movie can truly be excellent, the second most popular rating is 3.0 which suggests that quite a number of users found the movies they've seen to be neutral.")
                st.write("An Interesting note here is that the ratings are left skewed as see more ratings on the right side of the bargraph, this could be the result of the behaviour that people only tend to rate movies they like werease if they don't like a movie they would watch it till the end, let alone rate it")
                st.write("we see that average movie rating is 3.5 which suggest that we have more neutral and positive reviews seen by the skewed distribution")

        if sys_eda == "Movies":
        #if option_selection == "Movies":
            op_movies = st.radio("Choose",("Top 25 most rated movies of all time","25  most rated movies of the 21st century","Top 10 best and worst rated movies with over 10000 ratings","Total movies released per year"))
            #option_movie = ["Top 25 most rated movies of all time","25  most rated movies of the 21st century","Top 10 best and worst rated movies with over 10000 ratings","Total movies released per year"]
            #movie_option = st.selectbox("Choose Option", option_movie)
            if op_movies == "Top 25 most rated movies of all time":
            #if movie_option == "Top 25 most rated movies of all time":
                st.image('resources/imgs/25_most_1.png',use_column_width=True)
                st.write("Unsurprisingly the most rated movie of all time is Shawshank Redemption which is a 1994 American drama film written and directed by Frank Darabont, based on the 1982 Stephen King novella Rita Hayworth and Shawshank Redemption, we also see timeless classics like The Matrix which didn't only win 41 awards but also shaped the making of action movies in the 21st century.\n\nThe Matrix changed the way action sequences were handled by Hollywood, popularising the special effect known as bullet time. The most iconic scene in the film uses this technique, leaving us stunned as Neo dodges an enemy's gunfire, weaving his body around the bullets.\n\nAn interesting point to note here is that 21 of the 25 or 84% of 25 most rated movies of all time were released before the year 2000, could this mean people don't rate movies anymore or could it this be attributed to the fact these movies were released a long time ago and rating counts have accumulated over the years?\n\nSeing that 84% of the movies in our 25 most rated movies were released before 2000, sparks the curiosty to find the most rated movies of the 21st century")
            if op_movies == "25  most rated movies of the 21st century":
            #if movie_option == "25  most rated movies of the 21st century":
                st.image('resources/imgs/25_most_2.png',use_column_width=True)
                st.write("Looking at 25 most rated movies of the 21st century we see that another timeless classic the Lord of the rings trilogy tops the chart.\n\nThe Lord of the Rings is a film series of three epic fantasy adventure films directed by Peter Jackson, based on the novel written by J. R. R. Tolkien. This film series is about a young hobbit, Frodo, who has found the One Ring that belongs to the Dark Lord Sauron, begins his journey with eight companions to Mount Doom, the only place where it can be destroyed.\n\nIt is said that the reason this trilogy was so succesful is that the writter included so much detail and crafted such a wonderful and interesting story that it was still well loved when released in cinemas 50 years later. And there's no reason to think anything will change in another 50 years. The story features a number of diversions and twists, If you haven't seen it before and you love adventure films i'm sure our recommendation model which we will build later on will lead you to this trilogy🙂\n\nWe also see some of the best movies based DC comic books(my personal favourite kind of literature) two of which are from the Dark Knight trilogy which are The Dark Knight and Batman begins, we also see Spiderman which was written by the Legendary Marvel comic book superheros creator Stan Lee.\n\nSomething worth noting here again is the trend we saw ealier that as most recent movies don't really have that higher number of ratings as we see that 25 most rated movies of the 21st centure were all released before 2010.\n\n\n\nNow that we have have seen which movies were most rated we can now investigate the best and worst rated movies on average, one thing we have to be aware of here is the is that when calculating the average best and worst rated movies, if a movie is rated by one user and that user gave it 5 star then it will top the chart which would be misleading as such to avoid this we will develop a threshold for number of ratings that a movie should have before we can include its average rating.\n\n\From the two bar plots above we see that alot of movies have recieve over 10 000 ratings and as such we will make this our threshold")
            if op_movies == "Top 10 best and worst rated movies with over 10000 ratings":
            #if movie_option == "Top 10 best and worst rated movies with over 10000 ratings":
                st.image('resources/imgs/10_best_3.png',use_column_width=True)
                st.image('resources/imgs/10_worst_4.png',use_column_width=True)
                st.write("Unsurprisingly the most rated movie, Shawkshank Redemption is also the best rated movie with over 10000 ratings with an average rating of 4.4176, with this, would it be totally unjustified to say Shawshank Redemption is the best movie of all time? Shawshank Redemption is followed by another popularly known and loved movie The Godfather which is a 1972 American crime film directed by Francis Ford Coppola who co-wrote the screenplay with Mario Puzo, based on Puzo's best-selling 1969 novel of the same name, the sequel of The Godfather, The Godfather: Part II also made it to the top 10 best rated movies, coming in at position 4. The Godfather and its sequel revieved an average rating of4.3114 and 4.2741 respectively, Bottom of the list is Pulp Fiction with 4.1951 average rating.\n\n\n\nan interesting note here is that even though we have ##### movies released in the 21st century that have over 10 000 ratings, none of them made it to the top 10 best rated movies of all time since.\n\n\n\nNow turning our attention to worst rated movies with over 10000 ratings, it it worth noting that these are not at all lowest rated movies of all time but, they are however the lowest rated movies with over 10000 ratings, we do have lowest rated movies of all time but for the context of this notebook we will focus on those that have more that 10000 ratings.\n\nLooking at the lowest rated movies we see Waterworld coming in last with an average rating of 2.8830, we also see popular movies by Jim Carrey like Dumb and Dumber and Mask, as also see Home Alone which is a very popular christmas movie.")
            if op_movies == "Total movies released per year":
            #if movie_option == "Total movies released per year":
                st.image('resources/imgs/Total_5.png',use_column_width=True)
                st.write("We see that the year 2015 saw the highest number of movies released topping the chart with 2513 movies released in that year and the year 2016 coming in second with 2488 released movies.\n\n\n\nThere has been a steep increase in the movies of movies release per year in the 21st century")

        if sys_eda == "Directors":
        #if option_selection == "Directors":
            st.info("We start off with directors, A film director controls a film's artistic and dramatic aspects and visualizes the screenplay (or script) while guiding the technical crew and actors in the fulfilment of that vision. The director has a key role in choosing the cast members, production design and all the creative aspects of filmmaking\n\n\n\nEven though most people don't into finding our who director what movie to decide whether its going to be a good watch or not, there is a proportion of people that either watch the credits at the end of the movie or do research of each movie before they watch it, for these people director of a movie plays an import role in decided whether or not to watch a movie, for me personally I watch mroe series's than movies and but I know that if a series is directed by Chuck Lorre than I will definately love it.\n\nlet's start by finding our which directors have recieved the most number of ratings for their collective movies")
            
            op_director = st.radio("Choose",("Top 25 most rated directors","Top 25 directors with most number of movies","10 highest rated director with over 10000 ratings","10 worst rated directors with over 10000 ratings"))
            #option_directors = ["Top 25 most rated directors","Top 25 directors with most number of movies","10 highest rated director with over 10000 ratings","10 worst rated directors with over 10000 ratings"]
            #director_option = st.selectbox("Choose option", option_directors)
            if op_director == "Top 25 most rated directors":
            #if director_option == "Top 25 most rated directors":
                st.image('resources/imgs/top_25_most_D1.png',use_column_width=True)
                st.write("Topping the chart bar far we see Quentin Tarantino who has directed a total of 10 movies is an American film director, screenwriter, producer, and actor. His films are characterized by nonlinear storylines, aestheticization of violence, extended scenes of dialogue, ensemble casts, references to popular culture and a wide variety of other films, soundtracks primarily containing songs and score pieces from the 1960s to the 1980s, alternate history, and features of neo-noir film, One of Quentin Tarantino's highest rated movie Pulp fiction appreard in the top 10 best rated movies we saw ealier.\n\nwe also see familiar names like Stephen King who is also an author of horror, supernatural fiction, suspense, crime, science-fiction, and fantasy novels and directed a total of 23 movies among these movies is the movie we ponded a question of whether we can consider it as the best movie of all time, since it appeared top of the chart on both the Top 25 most rated movies of all time and Top 10 best rated movies of all time, Shawshank Redemption was based on Stephen King's novel.\n\n\n\nAfter seein the total number of ratings for each director its only natural that one wonders how many movies did each of these directors release, as this would contribute to the total number of ratings they have recieved, so lets find out which directors have released the most number of movies.")
            if op_director == "Top 25 directors with most number of movies":
            #if director_option == "Top 25 directors with most number of movies":
                st.image('resources/imgs/Top_25_directors_D2.png',use_column_width=True)
                st.write("We see a tie for the number spot between Luc Besson and Woody Allen, each having released an equal number of 26 movies. followed Stephen King This time coming at number 2 with a total of 23 movies. we also see some popularly names like that of William Shakespeare who was an English playwright, poet, and actor, widely regarded as the greatest writer in the English language and the world's greatest dramatist. as well Tyler Perry, a world-renowned producer, director, actor, screenwriter, playwright, author, songwriter, entrepreneur, and philanthropist, whos most successful movies series is the the Madea series which he doesnt only direct but also plays 3 roles in.\n\n\n\nKey obseravtion. Most of the movies that were produced by the directors in the about bar plot have the genres Drama and Romance or a mixture of those two gernes popularly known as romantic comedies, whether or not these two genres are the most succesful generes of highest rated genres is still to be investigated.\n\n\n\nWe have seen some of the most rated directors and dicectors with the most number of movies, now we turn our attention to finding out which directors have recieved the bests rating on average, this can help us guage if whether a movie will be worth watching or not, since we can check the average rating the director of that movie\n\n\n\ncontinuing with the trend we will only consider directors that have atleast 10000 ratings")
            if op_director == "10 highest and worst rated director with over 10000 ratings":
            #if director_option == "10 highest and worst rated director with over 10000 ratings":
                st.image('resources/imgs/10_highest_rated_D3.png',use_column_width=True)
                st.image('resources/imgs/10_worst_directors_D4.png',use_column_width=True)
                st.write("Toping the chart of the best rated directors is Chuck Palahniuk, the director of Fight Club that recieved an average rating of 4.22 which had Action, Crime, Drama and thriller genres. The second spot is held by Christopher McQuarrie recieving an average rating of 4.19 for three movies he has directed namely Usual suspects, Way of the gun and Edge of Tomorrow with mix of genres Action, Crime and Thriller, this this shares some light on the question we posed earlier of whether people the most succesful genres were a mix of Drama, Romance or Comedy, as we see that our two best rated directors create blockbusters with mix of genres action and thriller. We will investigated these genres thoroughly at a later stage.\n\n\Looking at the worst rated directed we see that the lowest rated director is Jack Bernstein with an average rating of 2.84\n\n\n\nWe now move to the next factor that influences the perfrance of of viewers that is the genre of the movie.\n\n")
        
        
        if sys_eda == "Genres":
        #if option_selection == "Genres":
            op_genre = st.radio("Choose",("Treemap of movie genres","Genre average rating over the years","Word cloud of movie genres"))
            #options_genres = ["Treemap of movie genres","Genre average rating over the years","Word cloud of movie genres"]
            #genre_options = st.selectbox('Choose option', options_genres)
            if op_genre == "Treemap of movie genres":
            #if genre_options == "Treemap of movie genres":
                st.image('resources/imgs/Treemap_G1.png',use_column_width=True)
                st.write("The genre treemap shows that Drama is the most popular genre with a genre count of 25606 followed by comedy with a count of 16870 as we initially suspected, We also see that Thriller and Romance follow suit. IMAX is by far the least popular genres with a count of 195 with Film-Noir following with a count of 353.\n\n\n\nWe have now seen the the most popular and least popular genres, lets now dig a little deeper into the genres and find out if whether the genre preference has changed throughout the years, to investigate this let's created an animated bar plot.")
            if op_genre == "Genre average rating over the years":
            #if genre_options == "Genre average rating over the years":
                st.video('resources/imgs/download.mp4')
                st.write("Right off the bat of the bet, the bar charr race shows us that there has been a change in genre preferences over the years")
                st.write("Stangely Animation was the best rated genre in 1995.\n\n\n\nIn 1996 Animation dropped to the 8th position and the Documentary became the most rated genre\n\n\n\n1997 Animation toped the char again and the following year Documentaty took over, seems between those 4 years the most prefered genres where Animation and Documentary, Strange times indeed...\n\n\n\nIn 1999 Crime movies started being popular and became the highest rated genre that year\n\n\n\nDrame took over the top spot in the year 2000\n\n\n\n2001 We see Fantasy, Crime and Drama taking the 1st. 2nd and 3rd spots respectively and we see these genres taking turns over the next couple of years until 2013 when Romance takes the lead and Documentaries become more popular and toping the chart in 2015.")
            if op_genre == "Word cloud of movie genres":
            #if genre_options == "Word cloud of movie genres":
                st.image('resources/imgs/Wordcloud_G3.png',use_column_width=True)

        if sys_eda == "Title Cast":
        #if option_selection == "Title Cast":
            st.image('resources/imgs/title_cast_1.png',use_column_width=True)
            st.write("The likes of Samuel L. Jackson ,steve Buscemi ans Keith David are the most popular cast members according to the graph above.")


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

    if page_selection == "Business Pitch":
        st.image('resources/imgs/BV_1.jpg',use_column_width=True)
        st.write("Some of the biggest companies in the world invested in streaming entertainment in the 21st century. The investment in streaming entertainment gave us platforms such as Netflix, Apple TV,, Disney Plus, Amazon prime and many more. These platforms are racking up millions of subscribers as the entire world is now streaming more than ever.")
        st.write("You may be wondering why these streaming platforms are attracting millions of subscribers, there are several reasons why people are leaning more towards streaming platforms. Streaming platforms have a lot of diverse content that can be consumed anywhere, anytime, and the subscribers are in total control of the rate at which they consume the content.")
        st.image('resources/imgs/BV_2.jpg',use_column_width=True)
        st.write("Another thing that is a major contributor in the rise and success of streaming platforms is their ability to recommend content that their users are most likely to watch and enjoy. They achieve this through the use of recommender algorithms. These algorithms ensure that each user is exposed to what they like.")
        st.image('resources/imgs/increasing.jpg',use_column_width=True)
        st.write("When doing exploratory data analysis we saw that the number of movies released increases exponentially each year. The exponential increase in the number of movies released means that streaming platforms need an excellent recommender algorithm to ensure that the movies reach the right audience.")
        st.image('resources/imgs/BV_L.jpg',use_column_width=True)
        st.write("This is where our recommender algorithm comes in. Our recommender algorithm will help with user retention by making tailored recommendations for each user. The user retention will ultimately result in a growth of the platform.")




if __name__ == '__main__':
    main()
