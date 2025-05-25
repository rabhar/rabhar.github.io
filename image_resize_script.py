from PIL import Image
import os

target_size_px = (1024, 900)

image_files = [
    "images/data-janitor.png",
    "images/data-librarian.jpeg",
    "images/data-miner.png",
    "images/data-plumber.png",
    "images/data-wrangler.png",
    "images/firefighter.png",
    "images/time-traveller.jpeg",
    "images/diplomat.jpeg",
    "images/data-mechanic.jpeg"
]

target_path = "images/high-resolution/"

def convert_image_size(image_path, target_size):
    """
    Converts an image to the specified size and saves it.

    Args:
        image_path (str): Path to the image file.
        target_size (tuple): Target size in pixels (width, height).
    """
    try:
        img = Image.open(image_path)
        img = img.convert("RGB")

        # Resize using high-quality resampling
        resized_img = img.resize(target_size, Image.LANCZOS)

        # Save to the target path
        filename = os.path.basename(image_path).split(".")[0]
        output_path = os.path.join(target_path, filename + ".jpg")

        # Save with high quality
        resized_img.save(output_path, format='JPEG', quality=100, optimize=True)

        # Save the resized image, overwriting the original file
        # img_resized.save(target_path + image_path.split("/")[-1].split(".")[0] + ".jpg")

        print(f"Image '{image_path}' successfully converted to {target_size} pixels.")

    except Exception as e:
        print(f"Error converting image '{image_path}': {e}")

# Process each image in the list
for image_file in image_files:
    convert_image_size(image_file, target_size_px)

print("All images processed.")
