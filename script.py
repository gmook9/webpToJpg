import os
from PIL import Image

# Define input and output directories
input_folder = "D:/repos/WebpToJPG/input"
output_folder = "D:/repos/WebpToJPG/output"

# Check if the input folder exists and contains WebP files
if not os.path.exists(input_folder):
    print("Input folder does not exist.")
else:
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input directory
    files = os.listdir(input_folder)
    webp_files = [f for f in files if f.lower().endswith(".webp")]

    if not webp_files:
        print("No WebP files found in the input folder.")
    else:
        for webp_file in webp_files:
            webp_path = os.path.join(input_folder, webp_file)
            jpg_filename = os.path.splitext(webp_file)[0] + ".jpg"
            jpg_path = os.path.join(output_folder, jpg_filename)

            # Convert WebP to JPG
            with Image.open(webp_path) as img:
                img.save(jpg_path, "JPEG")

            print(f"Converted: {webp_file} to {jpg_filename}")

print("Conversion complete.")
