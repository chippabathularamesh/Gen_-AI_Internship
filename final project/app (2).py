import streamlit as st
import google.generativeai as ai
from PIL import Image
import matplotlib.pyplot as plt
#------------------------------------------------------------------------------------------------------

KEY = "AIzaSyCBxCLJLoZ-s2pO7aVgrTVir956Kj43hiI"
ai.configure(api_key=KEY)

#------------------------------------------------------------------------------------------------------

st.title("AI Powered Solution for Assisting")

#---------------------------------------------------------------------------------------------------------------
with st.sidebar:
    st.title("AI-Powered Solution for Assisting Visually Impaired Individuals")
    st.write("""
        **Key Features**:
        - **Real-Time Scene Understanding**: The application uses AI to describe the content of images in detail, offering real-time scene analysis to help users gain an understanding of their surroundings.
        - **Personalized Assistance for Daily Tasks**: The system provides task-specific guidance, such as recognizing items, reading labels, and offering context-specific information to assist users with daily tasks.
    """)

#------------------------------------------------------------------------------------------------------
options = st.multiselect(
    "Choose an option",
    ["Real-Time Scene Understanding", "Personalized Assistance for Daily Tasks"])

if options:
    st.write("You selected:", options)
else:
    st.warning("Please select an option to proceed.")

#-------------------------------------------------------------------------------------------------------

model = ai.GenerativeModel(model_name="models/gemini-1.5-flash")

#---------------------------------------------------------------------------------------------------------

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

#--------------------------------------------------------------------------------------------------------------------
real_time_prompt = "Describe the scene in the uploaded image in detail."

personalized_prompt = """
    Analyze the image and provide the following guidance:
    1. Identify the items in the image.
    2. If any labels are visible, read them.
    3. Provide context-specific information such as categorizing the items (e.g., food items, books, etc.) and suggesting tasks or actions related to them.
"""

#-------------------------------------------------------------------------------------------------------

def Real_Time_Scene_Understanding(uploaded_file,prompt):
    if uploaded_file:
        
        image = Image.open(uploaded_file)

        
        
        st.image(image, caption="Uploaded Image", use_column_width=True)
    
        responce =  model.generate_content([image,prompt])
    
        st.write(responce.text)

def Personalized_Assistance_for_Daily(uploaded_file,prompt):
    if uploaded_file:
        image = Image.open(uploaded_file)

        st.image(image, caption="Uploaded Image", use_column_width=True)

        responce = model.generate_content([image,prompt])

        st.write(responce.text)


if "Real-Time Scene Understanding" in options and uploaded_file:
    Real_Time_Scene_Understanding(uploaded_file,real_time_prompt)




if "Personalized Assistance for Daily Tasks" in options and uploaded_file:
    Personalized_Assistance_for_Daily(uploaded_file,personalized_prompt)