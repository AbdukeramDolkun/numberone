import streamlit as st
import hydralit_components as hc
import datetime
st.markdown('# page one 🐈')#☠ 😹 🥷 ️ ⛹️‍♂️ 🧞‍♂️  👶  ☠ 💦
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


st.set_page_config(layout='wide')

menu_data = [
    {'icon': "far fa-copy", 'label':"Left End"},
    {'id':'Copy','icon':"🐙",'label':"Copy"},
    {'icon': "fa-solid fa-radar",'label':"Dropdown1", 'submenu':[{'id':' subid11','icon': "fa fa-paperclip", 'label':"Sub-item 1"},{'id':'subid12','icon': "💀", 'label':"Sub-item 2"},{'id':'subid13','icon': "fa fa-database", 'label':"Sub-item 3"}]},
    {'icon': "far fa-chart-bar", 'label':"Chart"},
    {'id':' Crazy return value 💀','icon': "💀", 'label':"Calendar"},
    {'icon': "fas fa-tachometer-alt", 'label':"Dashboard",'ttip':"I'm the Dashboard tooltip!"},
    {'icon': "far fa-copy", 'label':"Right End"},
    {'icon': "fa-solid fa-radar",'label':"Dropdown2", 'submenu':[{'label':"Sub-item 1", 'icon': "fa fa-meh"},{'label':"Sub-item 2"},{'icon':'🙉','label':"Sub-item 3",}]},
]

over_theme = {'txc_inactive': '#FFFFFF'}

menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    home_name='Home',
    login_name='Logout',
    hide_streamlit_markers=True,
    sticky_nav=True, 
    sticky_mode='pinned',
)

st.write(menu_id)
st.balloons()
st.image('a.png', caption='Sunrise by the mountains')
st.markdown('# page 2️⃣')
st.sidebar.markdown('# 🧛')
