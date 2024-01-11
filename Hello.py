import streamlit as st
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
import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(layout="wide", page_title="Image Background Remover")

st.write("## Remove background from your image")
st.write(
    ":dog: Try uploading an image to watch the background magically removed. Full quality images can be downloaded from the sidebar. This code is open source and available [here](https://github.com/tyler-simons/BackgroundRemoval) on GitHub. Special thanks to the [rembg library](https://github.com/danielgatis/rembg) :grin:"
)
st.sidebar.write("## Upload and download :gear:")

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload):
    image = Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("Fixed Image :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Download fixed image", convert_image(fixed), "fixed.png", "image/png")


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        fix_image(upload=my_upload)
else:
    fix_image("./zebra.jpg")
