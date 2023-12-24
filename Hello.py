import streamlit as st
st.write('ئادەم')
genre = st.radio(
    "What's your favorite Music? Listen music for free!",
    [":rainbow[A]", ":rainbow[B]", ":rainbow[C]:movie_camera:"],
    captions = ["a", "b", "c"])
import streamlit as st

#st.link_button("Go to gallery", "https://streamlit.io/gallery")
if genre == ':rainbow[A]':
    st.write('You selected A type of music')
    st.link_button("click the URL" ,"https://tool.liumingye.cn/music/#/search/M/song/Merry%20Christmas%20Mr.Lawrence%20(圣诞快乐,劳伦斯先生)")
if genre== ':rainbow[B]':
    st.write('You selected B type of music')
    st.link_button("click the URL", "https://tool.liumingye.cn/music/#/explore/artist")
if genre== ':rainbow[C]:movie_camera:':
    st.write('You Selected C type of music')
    st.link_button("click the URL" , "https://tool.liumingye.cn/music/#/explore/artist")
# else:
#     st.write("You didn\'t select")

st.balloons()
