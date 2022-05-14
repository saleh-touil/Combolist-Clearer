import streamlit as st  # pip3 install streamlit
import lapin
import os.path
import time

st.set_page_config(
    page_title='Cleaner',layout="centered",page_icon=":rabbit:",
    menu_items={'Get Help': None,'Report a bug': None,'About': None},initial_sidebar_state="auto")
title = st.title('Combolist Cleaner :rabbit:')
st.subheader('À vaillant coeur rien d’impossible. -Jacques Cœur')
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
#Upload fichier
todo = []
uploaded_file = st.file_uploader('Choisir un fichier txt ', type='txt')
def write_to_file(text):
      fb=open(os.path.join("results","base.txt"),"w",encoding="utf-8")
      for i in range(len(text)):
          fb.write(f"{todo[i]}\n")
      fb.close()
if uploaded_file:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode('utf-8')
    todo = data.rsplit('\r\n')
    write_to_file(todo)
    with st.spinner('Wait for it...'):
       tic = time.perf_counter()
       lapin.main()
       toc = time.perf_counter()
    st.success(f'Done in {toc-tic:0.1f} Seconds !')
    st.download_button(
     label="Download file",
     data=lapin.return_data(lapin.main.name),
     file_name=lapin.main.name,
     mime='text/plain')
