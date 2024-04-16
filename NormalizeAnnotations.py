import os
from PIL import Image

# Function to normalize coordinates
def normalize_coordinates(coord, width, height):
    x, y = coord
    return x / width, y / height

# Function to read annotations from a file and convert them
def convert_annotations(filename, image_path):
    with open(filename, 'r') as file:
        lines = file.readlines()

    converted_annotations = []

    # Open the image to get its dimensions
    with Image.open(image_path) as img:
        width, height = img.size

    for line in lines:
        line = line.strip().split(' ')
        class_index = line[0]
        coordinates = line[1:]

        converted_coords = []
        for coord in coordinates:
            coords_pair = coord.split(';')
            for pair in coords_pair:
                x, y = map(float, pair.split(','))
                normalized_x, normalized_y = normalize_coordinates((x, y), width, height)
                converted_coords.extend([normalized_x, normalized_y])

        converted_annotations.append((class_index, converted_coords))

    return converted_annotations


# Path to the folder containing annotation files
annotations_folder = "C:/Users/thend/Desktop/Pratik/Lower_jaw/text_annotations"
images_folder = "C:/Users/thend/Desktop/Pratik/Lower_jaw/Images"
output_folder = "C:/Users/thend/Desktop/Pratik/Lower_jaw/normalized_annotations"

# Iterate over each annotation file
for filename in os.listdir(annotations_folder):
    if filename.endswith(".txt"):
        filepath = os.path.join(annotations_folder, filename)
        image_name = os.path.splitext(filename)[0]
        image_path = os.path.join(images_folder, f"{image_name}.jpg")  # assuming images are in jpg format
        
        # Check if image exists
        if os.path.exists(image_path):
            converted_annotations = convert_annotations(filepath, image_path)
            
            # Write converted annotations to output file
            output_filename = os.path.join(output_folder, f"{image_name}.txt")
            with open(output_filename, 'w') as output_file:
                for class_index, coordinates in converted_annotations:
                    output_file.write(f"{class_index} {' '.join(map(str, coordinates))}\n")
        else:
            print(f"Image file '{image_path}' not found.")


