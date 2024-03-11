import openai
import urllib.request
from PIL import Image
import streamlit as st

# Set your OpenAI API key
openai.api_key = "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"

def generate_image(image_description):
    try:
        img_response = openai.Image.create(
            prompt=image_description,
            n=1,
            size="512x512"
        )

        img_url = img_response['data'][0]['url']

        # Download the image
        urllib.request.urlretrieve(img_url, 'img.png')

        # Open the downloaded image using PIL
        img = Image.open("img.png")
        
        return img

    except Exception as e:
        st.error(f"Error occurred: {e}")
        return None

# Streamlit UI
st.title('DALL.E - Image Generation - OpenAI')

# Text input box for image description
img_description = st.text_input('Image Description')

# Button to trigger image generation
if st.button('Generate Image'):
    # Check if the description is provided
    if img_description:
        # Generate and display the image
        generated_img = generate_image(img_description)
        if generated_img:
            st.image(generated_img, caption='Generated Image')
    else:
        st.warning("Please provide an image description.")
