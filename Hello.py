import streamlit as st
import tkinter as tk
from datetime import datetime
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

st.balloons()

st.markdown('# page 2️⃣')
st.sidebar.markdown('# 🧛')


def update_calendar():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    label.config(text="当前日期和时间: " + current_time)
    label.after(1000, update_calendar)  # 每1000毫秒（1秒）更新一次

root = tk.Tk()
root.title("实时更新日历")

label = tk.Label(root, font=('calibri', 20, 'bold'), background='purple', foreground='white')
label.pack(pady=20)

update_calendar()

root.mainloop()
