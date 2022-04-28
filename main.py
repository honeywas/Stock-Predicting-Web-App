import streamlit as st
from multiapp import MultiApp
from streamlit_option_menu import option_menu
from project import home, contact, learn # import your app modules here



app = MultiApp()

st.set_page_config(page_title='Stock Prediction Web App', page_icon=":crystal_ball:") 

st.title('Stock Predicting Web Application ')
#hide watermarks
hide_st_style = """
            <style>
            
            footer {visibility: hidden;}
            
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Basics   About   Stock Market", learn.app)
app.add_app("Contact us", contact.app)
# The main app
app.run()

