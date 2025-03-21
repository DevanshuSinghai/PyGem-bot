import os
import streamlit as st
from dotenv import load_dotenv
from streamlit_option_menu import option_menu
from PIL import Image
import google.generativeai as genai

#configuring API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# load gemini-pro model
def gemini_pro():
    model = genai.GenerativeModel('gemini-1.5-pro')
    return model

# Load gemini vision model
def gemini_vision():
    model = genai.GenerativeModel('gemini-pro-vision')
    return model

# get response from gemini model
def gemini_visoin_response(model, prompt, image):
    response = model.generate_content([prompt, image])
    return response.text


# Set page title and icon
st.set_page_config(
    page_title="Chat With Gemini",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded"
)

#setting sidebar of UI
with st.sidebar:
    user_picked = option_menu(
        "Gemini Chatbot",
        ["ChatBot", "Image Processing"],    
        menu_icon="robot",
        icons = ["chat-dots-fill", "image-fill"],
        default_index=0
    )


def roleForStreamlit(user_role):
    if user_role == 'model':
        return 'assistant'
    else:
        return user_role


if user_picked == 'ChatBot':
    model = gemini_pro()
    
    if "chat_history" not in st.session_state:
        st.session_state['chat_history'] = model.start_chat(history=[])

    st.title("🤖BoomBaasttic")

    #Display the chat history
    for message in st.session_state.chat_history.history:
        with st.chat_message(roleForStreamlit(message.role)):    
            st.markdown(message.parts[0].text)

    # Get user input
    user_input = st.chat_input("Message TalkBot:")
    if user_input:
        st.chat_message("user").markdown(user_input)
        reponse = st.session_state.chat_history.send_message(user_input)
        with st.chat_message("assistant"):
            st.markdown(reponse.text)

        
if user_picked == 'Image Processing':
    model = gemini_vision()

    st.title("🖼️Image Processing")

    image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

    user_prompt = st.text_input("Enter the prompt for image Processing:")

    if st.button("Generate"):
        load_image = Image.open(image)

        colLeft, colRight = st.columns(2)

        with colLeft:
            st.image(load_image.resize((800, 600)))

        caption_response = gemini_visoin_response(model, user_prompt, load_image)

        with colRight:
            st.info(caption_response)
