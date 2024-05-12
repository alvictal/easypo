import google.generativeai as genAi
from dotenv import load_dotenv
from utils.configs import *
import streamlit as st
import os

# Load Google Gemni
def loadGemini() -> None: 
    load_dotenv()
    genAi.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    

# Setup Google Gemni Model
def setupModel() -> genAi.GenerativeModel:
    
    generation_config = {
        "candidate_count" : 1,
        "temperature" : 0.7,
        "top_p": 0.90,
        "top_k" : 32
    }

    safety_settings = {
        "HARASSMENT" : "BLOCK_MEDIUM_AND_ABOVE",
        "HATE" : "BLOCK_MEDIUM_AND_ABOVE",
        "SEXUAL" : "BLOCK_MEDIUM_AND_ABOVE",
        "DANGEROUS" : "BLOCK_MEDIUM_AND_ABOVE"
    }
    return genAi.GenerativeModel(
        model_name=modelName,
        generation_config = generation_config,
        safety_settings = safety_settings
    )

# Load Streamlit Configs and Styles
def loadStreamlit() -> None:
    st.set_page_config(
        page_title="EasyPO",
        page_icon=":teacher:",
        layout="centered",
    )

    # Display the chatbot's title on the page
    st.markdown("<h1 style='text-align: center;'>Assistência no desenvolvimento de cards histórias \
                para desenvolvedores de software</h1>", unsafe_allow_html=True)

    # Create card layout with columns
    col1, col2 = st.columns([1, 2])

    # Display image in the left column
    with col1:
        st.image(mainImg, width=None)

    # Display text in the right column
    with col2:
        st.markdown(f"<p style='margin-top: 0.5em; font-size: 1em'>{headerText}</p>", 
                    unsafe_allow_html=True)

    # Display the divider
    st.divider()

def main() -> None:
    loadGemini()
    model = setupModel()

    loadStreamlit()

    # Input field for user's message
    userPrompt = st.chat_input(inputPlaceholderText)
    if userPrompt:
        sendPrompt = mainInstructions + "\n" + userPrompt
        geminiResponse =  model.generate_content(sendPrompt)
        st.markdown(geminiResponse.text)

        sendPrompt = subtasksInstructions + "\n" + geminiResponse.text
        geminiResponse =  model.generate_content(sendPrompt)
        st.markdown(geminiResponse.text)


# Running the project!
if __name__ == "__main__":
    main()

