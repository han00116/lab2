# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
from PIL import Image, ImageDraw, ImageFont

def main(image_path: str) -> str:
    try:
        image = Image.open(image_path)
        width, height = image.size
        font_size = 12
        font = ImageFont.truetype("arial.ttf", font_size)
        draw = ImageDraw.Draw(image)
        text = "Watermark"
        text_width, text_height = draw.textsize(text, font=font)
        draw.text((0, height - text_height), text, fill=(0, 0, 0), font=font, anchor='ls')
        image.save('watermarked_image.jpg')
        return 'Image watermarked successfully.'
    except Exception as e:
        logging.error(f"Error watermarking image: {e}")
        return 'Error watermarking image.'

