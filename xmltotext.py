#Uncomment to create annotaions in a single .txt file


# import xml.etree.ElementTree as ET

# def parse_xml(xml_file):
#     tree = ET.parse(xml_file)
#     root = tree.getroot()
#     annotations = []

#     for image in root.findall('image'):
#         image_name = image.get('name')
#         width = int(image.get('width'))
#         height = int(image.get('height'))
#         for polygon in image.findall('polygon'):
#             label = int(polygon.get('label'))
#             points = polygon.get('points').split(';')
#             # YOLO format requires normalized coordinates
#             x_center = (float(points[0].split(',')[0]) + float(points[2].split(',')[0])) / 2 / width
#             y_center = (float(points[0].split(',')[1]) + float(points[2].split(',')[1])) / 2 / height
#             box_width = abs(float(points[0].split(',')[0]) - float(points[2].split(',')[0])) / width
#             box_height = abs(float(points[0].split(',')[1]) - float(points[2].split(',')[1])) / height
#             annotations.append(f"{label} {x_center} {y_center} {box_width} {box_height}")

#     return annotations

# def save_to_txt(annotations, txt_file):
#     with open(txt_file, 'w') as f:
#         for annotation in annotations:
#             f.write(annotation + '\n')

# xml_file = 'C:/Users/thend/Desktop/Pratik/Lower_jaw/annotations.xml'
# txt_file = 'C:/Users/thend/Desktop/Pratik/Lower_jaw/annotations.txt'

# annotations = parse_xml(xml_file)
# save_to_txt(annotations, txt_file)




#Uncomment to create annotaions in seperate .txt files


import os
import xml.etree.ElementTree as ET

# Function to parse XML annotations and save as text files
def parse_xml_annotations(xml_file, annotations_folder):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Iterate through each image
    for image in root.findall('image'):
        image_name = image.get('name')
        image_id = image.get('id')

        # Create a text file corresponding to the image
        txt_file_path = os.path.join(annotations_folder, os.path.splitext(os.path.basename(image_name))[0] + ".txt")

        with open(txt_file_path, 'w') as txt_file:
            # Iterate through each polygon label in the image
            for polygon in image.findall('polygon'):
                label = polygon.get('label')
                points = polygon.get('points')

                # Write label and points to the text file
                txt_file.write(f'{label} {points}\n')

# Replace these paths with your image folder path and annotations folder path
image_folder = "C:/Users/thend/Desktop/Pratik/Lower_jaw/Image_dataset"
annotations_folder = "C:/Users/thend/Desktop/Pratik/Lower_jaw/text_annotations"
xml_file = "C:/Users/thend/Desktop/Pratik/Lower_jaw/annotations.xml"

# Parse XML annotations and save as text files
parse_xml_annotations(xml_file, annotations_folder)
