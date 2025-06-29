
import streamlit as st
from utils.image_analyzer import analyze_image
import openai
from PIL import Image

st.set_page_config(page_title='EMA.AI', page_icon='🧠')
st.image('logo.png', width=150)
st.title('EMA.AI - SƏ'nin AİYƏ'si süni zəka ilə intellektin')

user_input = st.text_input('Bir sual ver və ya mesaj yaz:')

if user_input:
    with st.spinner('Cavab hazırlanır...'):
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': user_input}]
        )
        st.success(response['choices'][0]['message']['content'])

uploaded_file = st.file_uploader("Əl ilə yüklə", type=['jpg', 'jpeg', 'png'])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption='Yüklədiyin AİYƏ kili', use_column_width=True)
    result = analyze_image(image)
    st.write("📄 Analiz nəticəsi:", result)
