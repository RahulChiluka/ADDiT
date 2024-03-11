from PIL import Image
import os

def resize_images_in_folder(folder_path, target_size=(32, 32)):
    """
    Resize all images in a folder to a specified size.

    Args:
    - folder_path (str): Path to the folder containing images.
    - target_size (tuple): The target size in pixels, as a tuple (width, height).
    """
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                try:
                    img_path = os.path.join(root, file)
                    img = Image.open(img_path)
                    img = img.resize(target_size, Image.LANCZOS)
                    img.save(img_path)
                    print(f'Resized {img_path}')
                except Exception as e:
                    print(f'Error resizing {img_path}: {e}')

# Replace 'path/to/your/dataset/folder' with the path to your dataset folder
dataset_folder = '/home/rahul/MTP/diffusion-classifier/diffusion/datasets/flowers-102/jpg'
resize_images_in_folder(dataset_folder)
