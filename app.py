from attr import has
import streamlit as st
import matplotlib.pyplot as plt
from sentiment import preprocessing_data, graph_sentiment, analyse_mention, analyse_hashtag, download_data, gen_wordcloud, gen_poswordcloud, gen_neuwordcloud, gen_negwordcloud, subjectivity, countvector


st.set_page_config(
    page_title="Live Twitter Sentiment Analysis",
    page_icon=":bird:",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://github.com/Jassvine',
        'About': "## A Twitter sentiment analysis webappTwitter Sentment Analysis Web App using #Hashtag and username to fetch tweets and tells the sentiment of the perticular #Hashtag or username. "
    }
)


st.title("Sentiment Analysis for Brands ")
st.markdown("Analyse user satisfaction based on twitter interactions to see how well your brand is doing! ")

st.write(" ")
st.write(" ")
st.write(" ")
st.write(" ")

function_option = st.sidebar.selectbox("Select Menu: ", [
                                       "Search By #Tag and Words", "Search By Username"])

if function_option == "Search By #Tag and Words":
    word_query = st.text_input("Enter the Hashtag or any topic")

if function_option == "Search By Username":
    word_query = st.text_input("Enter the Username without @ ")

number_of_tweets = st.slider("How many tweets do you want to collect from {}".format(
    word_query), min_value=100, max_value=10000)
st.info("Waiting period is approximately {} minute(s) for {} Tweets".format(
    round((number_of_tweets*0.05/60), 2), number_of_tweets))

if st.button("Start analysis for {}" .format(word_query)):

    data = preprocessing_data(word_query, number_of_tweets, function_option)
    analyse = graph_sentiment(data)
    mention = analyse_mention(data)
    hashtag = analyse_hashtag(data)
    img = gen_wordcloud(data)
    img1 = gen_poswordcloud(data)
    img2 = gen_neuwordcloud(data)
    img3 = gen_negwordcloud(data)
    subject = subjectivity(data)
    countdf = countvector(data)

    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.title("Extracted & Preprocessed Tweets")
    st.write(data)
    download_data(data, label="Pre-Processed Tweets")
    st.write(" ")

    col1, col2, col3 = st.columns(3)
    with col2:
        st.title("Exploratory Data Analysis (EDA) on the Tweets")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("Top 10 Hashtags used in {} tweets".format(number_of_tweets))
        st.bar_chart(hashtag, width=300, height=500)

    with col2:

        st.markdown("Most used words in the Tweets")
        st.bar_chart(countdf[1:11],width=300, height=500)

    #col3, col4 = st.columns([1.5, 1])
    col3, col4 = st.columns(2)

    with col3:

        st.markdown("Wordcloud for {} tweets".format(number_of_tweets))
        st.image(img)

    with col4:

        st.markdown("Top 10 @Mentions in {} tweets".format(number_of_tweets))
        st.bar_chart(mention)

    col5, col6, col7 = st.columns(3)

    with col5:

        st.markdown("Wordcloud for Positive tweets")
        st.image(img1)
    with col6:
        st.markdown("Wordcloud for Neutral tweets")
        st.image(img2)

    with col7:

        st.markdown("Wordcloud for Negative tweets")
        st.image(img3)



    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.title("Sentiment Analysis")
    st.bar_chart(analyse)

   