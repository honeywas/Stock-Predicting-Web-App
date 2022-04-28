import streamlit as st  # pip install streamlit
from annotated_text import annotated_text
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import time
import requests


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://assets5.lottiefiles.com/packages/lf20_zzasoagh.json"
lottie_hello = load_lottieurl(lottie_url_hello)

def app():
 st.header(":mailbox: Contact Us")


 contact_form = """
 <form action="https://formsubmit.co/honeywas34@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
 </form>
 """

 st.markdown(contact_form, unsafe_allow_html=True)

 # Use Local CSS File
 def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


 local_css("style/style.css")

 st.write("---")
 with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
      st.header(' Developed By: :wave:')
      st.subheader("""
            GROUP NO. 36
            
            
            1.ARYAN(11018210010)
            
            
            2.JATIN SAINI(11018210021)
            
            
            3.PRABAL K BHARDWAJ(11018210038)
            """)
      with right_column:
       st_lottie(lottie_hello, key="hello")
            
            