import os
from PIL import Image, ImageFilter

def dilate_image(input_path, output_path):
    # Open the input image
    with Image.open(input_path) as img:
        # Dilate the image using a filter
        dilated_img = img.filter(ImageFilter.MaxFilter(size=3))

        # Save the dilated image with the same filename as the original
        output_filename = os.path.basename(input_path).replace(".tif", ".png")
        output_file = os.path.join(output_path, output_filename)
        dilated_img.save(output_file, format="PNG")

def main():
    input_dir = "kidney_test"
    output_dir = "kidney_train"

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Loop through the input directory and process each TIFF image
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".tif"):
            input_file = os.path.join(input_dir, filename)
            dilate_image(input_file, output_dir)

if __name__ == "__main__":
    main()
