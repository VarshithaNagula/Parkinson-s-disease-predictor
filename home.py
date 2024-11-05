"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Parkinson's Disease Predictor")

    # Add image to the home page
    st.image("https://www1.racgp.org.au/getattachment/dc82be1e-a791-46b6-8bc8-38a0531f227e/Diagnosis-and-management-of-Parkinsons.aspx")

    # Add brief describtion of your web app
    #st.markdown(
    #"""<p style="font-size:20px;">
    #    </p>
    #""", unsafe_allow_html=True)