import os
from PIL import Image

# Define paths
input_folder = 'input_images'
output_folder = 'output_images'
resize_size = (800, 800)  # width x height

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process all image files
for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        try:
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            img = img.resize(resize_size)

            new_name = os.path.splitext(filename)[0] + ".png"
            save_path = os.path.join(output_folder, new_name)
            img.save(save_path, "PNG")
            print(f"Saved: {save_path}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")
