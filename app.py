
import streamlit as st
import pandas as pd 
import numpy as np
import pickle

df = pd.read_csv("Cleaned_data.csv")

model = pickle.load(open("pickle.pkl", "rb"))


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


def get_name_by_index (i):
    if i<=len(df) and i>0:
        return df.loc[i,"name"]
    return ""

def get_index_by_name(name):
    user_name = name.strip().lower().replace(" ","").replace("-","")
    match = df[df["name"].str.lower().str.replace(" ","").str.replace("-","") == user_name]
    if not match.empty:
        return match.index[0]
    return -1


movie = st.selectbox("Enter the name of anime movie",sorted(df["name"]))
        
movie_info = {
        "Arve Rezzle Kikaijikake no Youseitachi": {
            "image": "https://www.madinfinite.com/static/images_itens/big/10/arve-rezzle-kikaijikake-no-yousei-tachi-cover-009458.webp"
        },
        "FateZero 2nd Season": {
            "image": "https://cdn.myanimelist.net/images/anime/1522/117645l.jpg"
        },
        "Chainsaw Maid": {
            "image": "https://i.etsystatic.com/41225381/r/il/8cf97f/6086126767/il_1080xN.6086126767_2bvq.jpg"
        },
        "Karakuri Zoushi Ayatsuri Sakon": {
            "image": "https://image.tmdb.org/t/p/original/bL5wwWByI1n0frVAReM6dVO4Gu3.jpg"
        },
        "Paprika": {
            "image": "https://tse2.mm.bing.net/th/id/OIP.z_QkohBrY5FXB-TJN73I5AHaKi?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
        },
        "Higurashi no Naku Koro ni": {
            "image": "https://tse4.mm.bing.net/th/id/OIP.bCjOeooI88tuD8gOEIxCCgHaKi?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
        },
        "Karakuri Zoushi Ayatsuri Sakon": {
            "image": "https://tse1.mm.bing.net/th/id/OIP.bzxo7qRiTkKRugmCZisHWgHaKL?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
        },
        "Kagewani Shou": {
            "image": "https://tse3.mm.bing.net/th/id/OIP.VKiii67uVcCNit1e_4eumgAAAA?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
        },
        "Danganronpa Kibou no Gakuen to Zetsubou no Koukousei The Animation": {
            "image": "https://www.animeclick.it/immagini/manga/Danganronpa_Kibou_no_Gakuen_to_Zetsubou_Koukousei_The_Animation/gallery_original/Danganronpa_Kibou_no_Gakuen_to_Zetsubou_Koukousei_The_Animation-57b09b6216fb0.jpg"
        },
        "Arve Rezzle Kikaijikake no Youseitachi": {
            "image": "https://tse1.mm.bing.net/th/id/OIP.SmDve2tI5LtqG5XsdbdJFAAAAA?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
        },
        "Qui Shui Yi Yun": {
            "image": "https://i.pinimg.com/originals/a3/93/27/a39327538e70ddfadb46e3852dc72e7c.jpg"
        },
        "Kara no Kyoukai 7 Satsujin Kousatsu Kou": {
            "image": "https://myhotposters.com/cdn/shop/products/mL0598_1024x1024.jpg?v=1748537777"
        },
        "FateZero 2nd Season": {
            "image": "https://cdn.myanimelist.net/images/anime/3/40741l.jpg"
        },
        "Kaibutsu Oujo Konsui Oujo": {
            "image": "https://tse1.mm.bing.net/th/id/OIP.M-7PhlqX13CXK5Mfd2zZKgAAAA?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
        },
        "CLAY": {
            "image": "https://cdn.anisearch.com/images/character/cover/128/128675_400.webp"
        },
        "GaRei Zero": {
            "image": "https://tse4.mm.bing.net/th/id/OIP.5dtFT7P7ytZuuU95cV6jqwHaLH?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
        },
        "Mahou Shoujo Ai": {
            "image": "https://tse4.mm.bing.net/th/id/OIP.OwBJSowOpqBimNWdmdE2yQHaKe?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
        },
        "Toilet no Hanakosan": {
            "image": "https://m.media-amazon.com/images/M/MV5BM2MzMGRlN2QtM2FhMS00Y2FhLWE4MTEtMGNiZTU5YTdiY2JiXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg"
        },
        "Highschool of the Dead": {
            "image": "https://tse1.mm.bing.net/th/id/OIP.dJCbEuXkvGeDvUOkhiq6DgAAAA?r=0&w=390&h=554&rs=1&pid=ImgDetMain&o=7&rm=3"
        },
        "Biohazard 4 Incubate": {
            "image": "https://www.themoviedb.org/t/p/original/cQCESygsQePaNtl8xSOlkOF3rgc.jpg"
        },
        "Kakurenbo": {
            "image": "https://tse4.mm.bing.net/th/id/OIP.xHu4RbNFlKcTE8jr1QoDugHaKX?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
        },
        "Shinsekai yori": {
            "image": "https://tse1.mm.bing.net/th/id/OIP.elkns_qA2clmMTAbedcS5QHaKi?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
        },
        "Maou Dante": {
            "image": "https://cdn.myanimelist.net/images/anime/1038/98765.jpg"
        },
        "Corpse Party Missing Footage": {
            "image": "https://media.fstatic.com/C4idH4n8Bcf-5GYLrFNfxltc2ag=/322x478/smart/filters:format(webp)/media/movies/covers/2014/08/corpse-party-missing-footage_t84612.png"
        },
        "Jigoku Sensei Nube Gozen 0 toki Nube Shisu": {
            "image": "https://tse1.mm.bing.net/th/id/OIP.iTLJ-JkDaQNpDwob6d40sAHaKc?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
        },
        "BloodC": {
            "image": "https://i.pinimg.com/736x/7e/be/83/7ebe833898146267b649a688a3ee9a20.jpg"
        },
        "Gegege no Kitarou Jigokuhen": {
            "image": "https://cdn.myanimelist.net/images/anime/1554/99658l.jpg"
        },
        "Moyashimon": {
            "image": "https://image.tmdb.org/t/p/original/A8swodH66BGLr8vLRFdZ4mQQvEN.jpg"
        },
        "Gegege no Kitarou Daikaijuu": {
            "image": "https://tse4.mm.bing.net/th/id/OIP.VOx1YjcIXbxPn3s6T_yw4wAAAA?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
        },
        "Akumakun": {
            "image": "https://cdn.wallpapersafari.com/94/12/P9dzvH.jpg"
        },
        "Inyouchuu The Animation": {
            "image": "https://image.cdn2.seaart.me/temp-convert-webp/highwebp/static/images/20250825/e8face3c6b75dd5e23d59fcf2b581f16_low.webp"
        },
        "Inyouchuu Etsu Special": {
            "image": "https://i.pinimg.com/736x/09/79/ed/0979edb72b9f1a2a03c7423a12711691.jpg"
        },
        "Kannagi Moshimo Kannagi ga Attara": {
            "image": "https://cdn.animeschedule.net/production/assets/public/img/anime/jpg/default/kannagi-7dbf2c2538.jpg"
        },
        "SteinsGate": {
            "image": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/5be4724c-3360-457c-948f-d56a86849b97/dbyuckf-b36bbc0b-c73b-4e18-b11d-a6ab28fcc432.png/v1/fill/w_1024,h_1451,q_80,strp/steins_gate_by_lucentfong_dbyuckf-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTQ1MSIsInBhdGgiOiJcL2ZcLzViZTQ3MjRjLTMzNjAtNDU3Yy05NDhmLWQ1NmE4Njg0OWI5N1wvZGJ5dWNrZi1iMzZiYmMwYi1jNzNiLTRlMTgtYjExZC1hNmFiMjhmY2M0MzIucG5nIiwid2lkdGgiOiI8PTEwMjQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.Q3_XWnaLKxQu87mww-OjmMUAHeTjaK_j8gwagXTTGyQ"
        },
        "Ushiro no Hyakutarou": {
            "image": "https://cdn.myanimelist.net/images/manga/2/266402.jpg"
        }
        
        
}



if st.button("Recommend"):
    
    index = get_index_by_name(movie)

    if index != -1:

        similarity_indexes = sorted(
        enumerate(model[index]),
        key=lambda x: x[1],
        reverse=True
        )

    

        for row in range(4):     # 4 rows

            cols = st.columns(5)

            for col in range(5):

                i = row * 5 + col + 1

                movie_id = similarity_indexes[i][0]
                name = get_name_by_index(movie_id)

                with cols[col]:

                    if name in movie_info:

                        st.markdown(
                        f"<center><span style='color:white; margin-bottom:20px;'>{name}</span></center>",
                    unsafe_allow_html=True
                        )

                        st.image(
                    movie_info[name]["image"],
                    width=150
                        )

                    else:

                        st.write(name)
                        st.caption("Image not available.")
    

        

    
    

        

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
