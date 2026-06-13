import streamlit as st
st.title('첫번째 웹 어플 만들기')
st.write('# 1. 마크다운 텍스트 작성하기')
import pandas as pd
import numpy as np

# 표(DataFrame) 표시하기
st.write('# 2. DataFrame 표시하기') 
df = pd.DataFrame({
    '이름': ['홍길동', '이순신', '강감찬'],
    '나이': [20, 45, 35]
}) 
st.dataframe(df)