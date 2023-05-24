import argparse
import datetime
import json

def check_coco_format(json_data):
    if 'annotations' in json_data and 'images' in json_data and 'categories' in json_data:
        return True
    return False

def convert_to_coco_format(json_data):
    # Add necessary fields for COCO format if they are missing
    if 'annotations' not in json_data:
        json_data['annotations'] = []
    if 'images' not in json_data:
        json_data['images'] = []
    if 'categories' not in json_data:
        json_data['categories'] = []

    return json_data

def main(input_file):
    # Read the input JSON file
    with open(input_file, 'r') as file:
        json_data = json.load(file)

    # Check if the JSON file is in COCO format
    if check_coco_format(json_data):
        print("COCO format, no need to change.")
        return

    # Convert the JSON data to COCO format
    converted_data = convert_to_coco_format(json_data)

    # Create the output file name based on the input file name and current date
    output_file = f"{input_file.split('.')[0]}_{datetime.date.today()}.json"

    # Write the converted JSON data to the output file
    with open(output_file, 'w') as file:
        json.dump(converted_data, file)

    print(f"Data converted to COCO format and saved as {output_file}.")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="JSON format converter")
    parser.add_argument("--input", help="Input JSON file")
    args = parser.parse_args()

    if args.input:
        main(args.input)
    else:
        print("Please provide the input JSON file using the --input argument.")
