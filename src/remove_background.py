#!/usr/bin/env python3
"""
Script to remove background from an image and make it transparent.
"""
from rembg import remove
from PIL import Image
import sys

def remove_background(input_path, output_path):
    """Remove background from image and save with transparency."""
    print(f"Reading image from: {input_path}")
    
    # Open the input image
    with open(input_path, 'rb') as input_file:
        input_data = input_file.read()
    
    # Remove background
    print("Removing background... (this may take a moment)")
    output_data = remove(input_data)
    
    # Save the output image
    print(f"Saving transparent image to: {output_path}")
    with open(output_path, 'wb') as output_file:
        output_file.write(output_data)
    
    print("✓ Background removed successfully!")

if __name__ == "__main__":
    # Define paths
    input_image = "docs/assets/img/profile_long.png"
    output_image = "docs/assets/img/profile_long.png"  # Will overwrite original
    
    # You can also save to a backup first
    backup_image = "docs/assets/img/profile_long_original.png"
    
    # Create backup
    print(f"Creating backup at: {backup_image}")
    img = Image.open(input_image)
    img.save(backup_image)
    
    # Remove background
    remove_background(input_image, output_image)
