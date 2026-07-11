
import streamlit as st
import pandas as pd 
import numpy as np
import pickle

df = pd.read_csv("Cleaned_data.csv")

st.markdown(""" <style>
    .stApp{
        background: linear-gradient(to top, #000000, #161C47);
            }


    /* BANNER */
    .banner {
        width: 100px;
        height: 50px;
        background-image: url("https://wallpapercave.com/wp/wp12313149.jpg");
        margin-top:5px;
        background-position: center;
        border-radius: 15px;
        margin: 10px auto 6px auto;  /* reduced bottom gap */
        box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
    }
            
    div[data-testid="stSelectbox"] label {
    color: white !important;
    font-weight: bold;
    font-size: 16px;
    margin-top : 25px;
}
            
  div.stButton > button {
    background-color: #04082B;
    color: white;
    font-size: 20px;
    font-weight: bold;
    width: 140px;
    height: 45px;
    border-radius: 10px;
    border: 2px double white;
    margin-top : 10px;
    margin-bottom : 10px;
}
            </style>
""",unsafe_allow_html=True)



st.markdown("""
<style>
div[data-testid="stSelectbox"] label {
    color: grey !important;
    font-size: 20px !important;
    font-weight: bold !important;
}
</style>
""", unsafe_allow_html=True)



st.markdown("""
<style>
[data-testid="stSidebar"] {
    background-color: #06081F;
    color:white;
            
}       


</style>
""", unsafe_allow_html=True)

st.markdown(""" 
    <h2 style="color:white; font-size:35px; margin-bottom:22px; align-text:center;"><b>🎌 Anime Recommendation System</b></h2>
            """,unsafe_allow_html=True)


st.markdown(
    "<h5 style='color:grey; margin-bottom:5px; align-text:center;'><u>Discover Your Next Favorite Anime</u> </h5>",
    unsafe_allow_html=True)


# Page Configuration
st.set_page_config(
    page_title="Anime Recommendation System",
    page_icon="🎌",
    layout="wide"
)
st.divider()

st.image("https://wallpapercave.com/wp/wp12313149.jpg", use_container_width=True)

st.divider()

st.markdown(
    "<h4 style='color:white; '><b>Search Anime</b></h4>",
    unsafe_allow_html=True)




st.sidebar.title("-- AnimeVerse --")
st.sidebar.markdown(""" <h5><u>Today's Anime </u></h5>""",unsafe_allow_html=True)
st.sidebar.markdown(""" <h6>    🎬 Spirited Away  - ⭐ 9.90</h6>""",unsafe_allow_html=True)
st.sidebar.markdown(""" <h5>👩‍💻 Developer</h5>""",unsafe_allow_html=True)
st.sidebar.markdown(""" <h6> Vishakha Nikam</h6>""",unsafe_allow_html=True)


st.sidebar.markdown(""" <h5>✨ Quote </h5>""",unsafe_allow_html=True)

st.sidebar.info("Every anime tells a story")



movie = st.selectbox("Enter the name of anime movie",sorted(df["name"]))





if st.button("Recommend"):

    if movie.strip() == "":
        st.warning("Please enter an anime name.")

    else:
        # Store movie name
        st.session_state["movie"] = movie

        # Open recommendation page
        st.switch_page("pages/button.py")

    

        

st.divider()

st.markdown(
    "<h4 style='color:white;  '><b>🔥 Popular Anime</b></h4>",
    unsafe_allow_html=True)






st.markdown("""
    <style>
    [data-testid="stCaptionContainer"] p {
    color: white !important;
    font-size: 14px !important;
    }
    </style>
    """, unsafe_allow_html=True)



col1, col2, col3, col4 = st.columns(4)

with col1:
        st.caption("Paprika")
        st.image("https://tse2.mm.bing.net/th/id/OIP.z_QkohBrY5FXB-TJN73I5AHaKi?r=0&rs=1&pid=ImgDetMain&o=7&rm=3")
        

with col2:
        st.caption("Chainsaw Maid")
        st.image("https://i.etsystatic.com/41225381/r/il/8cf97f/6086126767/il_1080xN.6086126767_2bvq.jpg")
        

with col3:
        st.caption("Karakuri Zoushi Ayatsuri Sakon")
        st.image("https://image.tmdb.org/t/p/original/bL5wwWByI1n0frVAReM6dVO4Gu3.jpg")
        

with col4:
        st.caption("Magic Kaito")
        st.image("https://tse1.mm.bing.net/th/id/OIP.umlQT3zMPLk6o8HJMYKBwgHaKx?r=0&rs=1&pid=ImgDetMain&o=7&rm=3")
        


col1, col2, col3, col4 = st.columns(4)

with col1:
        st.caption("Clannad")
        st.image("https://i.pinimg.com/736x/ab/44/01/ab4401c1268ff875130278cd5e2cdd2d.jpg")
        

with col2:
        st.caption("Alignment You You The Animation")
        st.image("https://cdn.myanimelist.net/r/180x280/images/anime/10/70015.jpg?s=889060472f8ea10fb0a99f3381b9741a")
        

with col3:
        st.caption("Suzumiya Haruhi no Shoushitsu")
        st.image("https://tse2.mm.bing.net/th/id/OIP.hWdl7gTLMsmPfod5tZ9iSgDaEe?r=0&rs=1&pid=ImgDetMain&o=7&rm=3")
        

with col4:
        st.caption("ReKan")
        st.image("https://tse3.mm.bing.net/th/id/OIP.rbUz2bh1jr-uHrNoZBhEgQHaKj?r=0&rs=1&pid=ImgDetMain&o=7&rm=3")
        

st.markdown(""" <h4 style="color:white; margin-top: 45px; margin-bottom: 20px;">⭐ Top Rated  </h4>""",unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
        st.caption("Spirited Away")
        st.image("https://tse3.mm.bing.net/th/id/OIP.LXuLXupOTAlf7535sYvgIgHaLH?r=0&rs=1&pid=ImgDetMain&o=7&rm=3")
        st.caption("Rating - ⭐ 9.90")

with col2:
        st.caption("Your Name")
        st.image("https://wallpapercave.com/wp/wp1937325.jpg")
        st.caption("Rating - ⭐ 9.00")

with col3:
        st.caption("Akira")
        st.image("https://alternativemovieposters.com/wp-content/uploads/2022/12/Chris-Towner_Akira.jpg")
        st.caption("Rating - ⭐ 8.90")

with col4:
        st.caption("Princess Mononoke")
        st.image("https://static1.cbrimages.com/wordpress/wp-content/uploads/sharedimages/2024/04/princess-mononoke-movie-poster.jpg")
        st.caption("Rating - ⭐ 8.50")
