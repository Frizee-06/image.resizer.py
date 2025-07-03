import os
from PIL import Image

input_folder = 'images'
output_folder = 'resized_images'
new_size = (300, 300)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith(('.jpg', '.png', '.jpeg','.webp')):
        try:
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            img_resized = img.resize(new_size)
            new_filename = os.path.splitext(filename)[0] + '.png'
            img_resized.save(os.path.join(output_folder, new_filename))
            print(f"{filename} resized and saved as {new_filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")