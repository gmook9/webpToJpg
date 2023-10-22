import os
from PIL import Image

input_folder = "input"
output_folder = "output"

if not os.path.exists(input_folder):
    print("Input folder does not exist.")
else:
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    files = os.listdir(input_folder)
    webp_files = [f for f in files if f.lower().endswith(".webp")]

    if not webp_files:
        print("No WebP files found in the input folder.")
    else:
        for webp_file in webp_files:
            webp_path = os.path.join(input_folder, webp_file)
            jpg_filename = os.path.splitext(webp_file)[0] + ".jpg"
            jpg_path = os.path.join(output_folder, jpg_filename)

            with Image.open(webp_path) as img:
                img.save(jpg_path, "JPEG")

            print(f"Converted: {webp_file} to {jpg_filename}")
