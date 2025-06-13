from PIL import Image
import os

def resize_image(input_path, output_path, size=(450, 450)):
    img = Image.open(input_path)
    img = img.resize(size, Image.Resampling.LANCZOS)  # Updated for Pillow ≥10
    img.save(output_path)
    print(f"Image saved to {output_path}")

# Example usage
resize_image("/home/eso8484/Downloads/photo_me.jpg", "output.jpg")
