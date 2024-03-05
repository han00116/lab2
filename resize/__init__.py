# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
from PIL import Image

def main(image_path: str) -> str:
    width = 1024
    height = 768
    try:
        img = Image.open(image_path)
        resized_img = img.resize((width, height))
        resized_img.save('resizedImage.jpg')
        return 'Image resized successfully.'
    except Exception as e:
        logging.error(f"Error resizing image: {e}")
        return 'Error resizing image.'
