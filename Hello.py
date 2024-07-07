import streamlit as st

import datetime
st.markdown('# page one 🐈')#☠ 😹 🥷 ️ ⛹️‍♂️ 🧞‍♂️  👶  ☠ 💦

#st.set_page_config(layout='wide')

over_theme = {'txc_inactive': '#FFFFFF'}

st.write(menu_id)
st.sidebar.markdown("# 🦸‍♂ ")
st.write('# 📚 🎶 🧛 🤖 🔍 💦') #如果前面加了这个符号就是#大写了。
genre = st.radio(
    "# ",
    [":rainbow[e-books1]",":rainbow[e-books2]", ":rainbow[music🎶]", ":rainbow[anime🧞]" ,
     ":rainbow[coding🤖]", ":rainbow[research🔍]" ,":rainbow[cracks detection🚧]", ":rainbow[free magazine]"],
    captions = ["📚", "🎶","🎶", "🧛","🤖" ,"🔍","🚧" ,"📰"])
import streamlit as st

#st.link_button("Go to gallery", "https://streamlit.io/gallery")
if genre == ':rainbow[e-books1]':
    st.write('You selected 📚')
    st.link_button("click the URL" ,"https://sobooks.net/")
if genre == ':rainbow[e-books2]':
    st.write('You selected 📚')
    st.link_button("click the URL" ,"https://z-library.se/")
if genre== ':rainbow[music🎶]':
    st.write('You selected 🎶')
    st.link_button("click the URL", "https://tool.liumingye.cn/music/#/")
if genre== ':rainbow[anime🧞]':
    st.write('You selected 🧞')
    st.link_button("click the URL" , "https://m.dilidiliw.com/")
#编程网站
if genre== ':rainbow[coding🤖]':
    st.write('You selected 🤖')
    st.link_button("click the URL" , "https://www.runoob.com/")

#文献搜索网站
if genre== ':rainbow[research🔍]':
    st.write('You selected 🔍')
    st.link_button("click the URL" , "https://scholar.chongbuluo.com/")
#路面病害检测
if genre== ':rainbow[cracks detection🚧]':
    st.write('You selected 🚧')
    st.link_button("click the URL" , "https://binghaijiancexitong.streamlit.app/")

#free magazine
if genre== ':rainbow[free magazine]':
    st.write('You selected 📰')
    st.link_button("click the URL" , "https://freemagazines.top/")

# else:
#     st.write("You didn\'t select")


#st.image('c.jpg', caption='Sunrise by the mountains')
#st.image('b.jpg', caption='Sunrise by the mountains')
#st.image('d.jpg', caption='Sunrise by the mountains')
st.balloons()
#st.image('a.png', caption='Sunrise by the mountains')
st.markdown('# page 2️⃣')
st.sidebar.markdown('# 🧛')
