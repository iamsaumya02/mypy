#Script to  parse the contents of a user provided folder
# and count the number of images in the folder.

import os
from PIL import Image

def count_images_in_folder(folder_path):
    # List to hold the file paths of detected images
    image_files = []

    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp')

    # Traverse the directory and check each file
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(image_extensions):
                try:
                    # Check if the file can be opened as an image
                    img = Image.open(os.path.join(root, file))
                    img.verify()  
                    image_files.append(file)
                except (IOError, SyntaxError):
                    print(f"File {file} is not a valid image.")

    # Return the count of valid image files
    return len(image_files)

if __name__ == "__main__":
    # the folder path
    folder_path = r"C:\Users\summa\OneDrive\Pictures\Screenshots"

    # Count the images in the folder
    image_count = count_images_in_folder(folder_path)

    # result
    print(f"The folder contains {image_count} image(s).")