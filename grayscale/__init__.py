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
    try:
        img = Image.open(image_path)
        grayscale_img = img.convert('L')
        grayscale_img.save('grayscale.jpg')
        return 'Image converted to grayscale successfully.'
    except Exception as e:
        logging.error(f"Error converting image to grayscale: {e}")
        return 'Error converting image to grayscale.'
