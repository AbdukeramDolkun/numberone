import pandas as pd
import streamlit as st
import numpy as np
import altair as alt
st.write('ئادەم')
st.header('what the hell')
if st.button ('click the button'):
    st.write('a')
else:
    st.write('b')
st.caption('*-*-ssss')

df = pd.DataFrame({
    'first column':[1,2,3,4],
    'secon column':[10,20,30,40]})
st.write(df)
df1= pd.DataFrame(
    np.random.randn(10,3,),
    columns=['a','b','c'])
st.write(df1)
c = alt.Chart(df1).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)
st.balloons()
