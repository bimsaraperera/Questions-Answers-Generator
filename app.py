import streamlit as st
from pprint import pprint
from Model import main

st.title('Questions & Answers Generator')

paragraph = st.text_area("Input Paragraph",max_chars=20000)

payload = {
            "input_text": paragraph
        }
qg = main.QGen()
output = qg.predict_shortq(payload)

if st.button('Generate'):

    for i in output['questions']:
        st.text('Question : '+ i['Question'])
        st.text('Answer : ' + i['Answer'])
        st.markdown('---')